[CmdletBinding()]
param(
    [Parameter()]
    [string]$SkillPath,

    [Parameter()]
    [switch]$PackageOnly
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version 2.0

$RepositoryRoot = (Resolve-Path -LiteralPath (Join-Path $PSScriptRoot '..')).Path
if (-not $SkillPath) {
    $SkillPath = Join-Path $RepositoryRoot 'skills\marketing-practitioner'
}
$ResolvedSkillPath = (Resolve-Path -LiteralPath $SkillPath).Path
$Python = (Get-Command python -ErrorAction Stop).Source

function Invoke-Checked {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Label,

        [Parameter(Mandatory = $true)]
        [string[]]$Arguments
    )

    $Executable = $Arguments[0]
    $Tail = @()
    if ($Arguments.Count -gt 1) {
        $Tail = $Arguments[1..($Arguments.Count - 1)]
    }
    & $Executable @Tail
    $Code = $LASTEXITCODE
    if ($Code -ne 0) {
        Write-Error "$Label failed with exit code $Code"
        exit $Code
    }
    Write-Host "$Label`: PASS"
}

Push-Location -LiteralPath $RepositoryRoot
try {
    Invoke-Checked -Label 'repository package validator' -Arguments @(
        $Python,
        '-B',
        (Join-Path $RepositoryRoot 'scripts\validate_skill.py'),
        $ResolvedSkillPath
    )

    $ValidatorCandidates = @()
    if ($env:CODEX_HOME) {
        $ValidatorCandidates += Join-Path $env:CODEX_HOME 'skills\.system\skill-creator\scripts\quick_validate.py'
    }
    $ValidatorCandidates += Join-Path $env:USERPROFILE '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
    $ExternalValidator = $ValidatorCandidates |
        Where-Object { Test-Path -LiteralPath $_ -PathType Leaf } |
        Select-Object -First 1
    if ($ExternalValidator) {
        Invoke-Checked -Label 'current Codex validator' -Arguments @(
            $Python,
            '-B',
            $ExternalValidator,
            $ResolvedSkillPath
        )
    }
    else {
        Write-Host 'current Codex validator: SKIP (not installed or not discoverable)'
    }

    if ($PackageOnly) {
        exit 0
    }

    Invoke-Checked -Label 'knowledge routing mechanics' -Arguments @(
        $Python,
        '-B',
        (Join-Path $ResolvedSkillPath 'scripts\test-knowledge-routing.py')
    )
    Invoke-Checked -Label 'route and source validation' -Arguments @(
        $Python,
        '-B',
        (Join-Path $ResolvedSkillPath 'scripts\get-knowledge.py'),
        '--validate'
    )
    Invoke-Checked -Label 'Pressure Discovery pilot tests' -Arguments @(
        $Python,
        '-B',
        '-m',
        'unittest',
        'discover',
        '-s',
        'evals/pressure-discovery/pilot/tests',
        '-v'
    )
    Invoke-Checked -Label 'behavioral harness tests' -Arguments @(
        $Python,
        '-B',
        '-m',
        'unittest',
        'discover',
        '-s',
        'evals/behavioral/tests',
        '-v'
    )

    $Utf8 = New-Object System.Text.UTF8Encoding($false, $true)
    $TextExtensions = @(
        '.json', '.md', '.py', '.ps1', '.txt', '.yaml', '.yml'
    )
    $EncodingFailures = @()
    Get-ChildItem -LiteralPath $RepositoryRoot -Recurse -File | ForEach-Object {
        $Relative = $_.FullName.Substring($RepositoryRoot.Length).TrimStart('\')
        if ($Relative -match '(^|\\)\.git(\\|$)' -or
            $Relative -match '(^|\\)__pycache__(\\|$)' -or
            $Relative -match '^evals\\behavioral\\results(\\|$)') {
            return
        }
        if ($TextExtensions -notcontains $_.Extension.ToLowerInvariant()) {
            return
        }
        try {
            [void]$Utf8.GetString([System.IO.File]::ReadAllBytes($_.FullName))
        }
        catch {
            $EncodingFailures += $Relative
        }
    }
    if ($EncodingFailures.Count -gt 0) {
        Write-Error ('invalid UTF-8 files: ' + ($EncodingFailures -join ', '))
        exit 1
    }

    $GeneratedArtifacts = @(
        Get-ChildItem -LiteralPath $RepositoryRoot -Recurse -Force |
            Where-Object {
                $_.FullName -notmatch '(^|\\)\.git(\\|$)' -and
                ($_.Name -eq '__pycache__' -or $_.Extension -eq '.pyc')
            }
    )
    if ($GeneratedArtifacts.Count -gt 0) {
        Write-Error 'generated Python cache artifacts are present'
        exit 1
    }
    $TrackedResults = & git ls-files -- 'evals/behavioral/results'
    $GitCode = $LASTEXITCODE
    if ($GitCode -ne 0) {
        Write-Error "generated-artifact Git check failed with exit code $GitCode"
        exit $GitCode
    }
    if ($TrackedResults) {
        Write-Error 'generated behavioral results are tracked by Git'
        exit 1
    }

    $SkillText = [System.IO.File]::ReadAllText(
        (Join-Path $ResolvedSkillPath 'SKILL.md'),
        $Utf8
    )
    $NotEqualSentinel = [string][char]0x2260
    $ArrowSentinel = [string][char]0x2192
    if (-not $SkillText.Contains($NotEqualSentinel) -or -not $SkillText.Contains($ArrowSentinel)) {
        Write-Error 'UTF-8 sentinel characters are missing from SKILL.md'
        exit 1
    }
    Write-Host 'UTF-8 and generated-artifact hygiene: PASS'
    Write-Host 'repository verification: PASS'
}
finally {
    Pop-Location
}

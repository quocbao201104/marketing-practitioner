# Codex plugin

Marketing Practitioner can be distributed as a Codex plugin containing the existing agent skill. The repository root is the plugin root: [plugin.json](../.codex-plugin/plugin.json) points directly to `./skills/`. The standalone skill installation remains supported.

For browser use in Claude or ChatGPT, see the [web setup guide](web-setup.md). A successful local Codex installation does not establish web installation or account eligibility.

The plugin packages instructions and knowledge. It does not include an MCP server, external account connections, hooks, or a separate agent runtime. Python is optional for exact section retrieval; hosts can read the packaged files directly.

## Package contents

Distribute a folder named `marketing-practitioner` containing:

```text
marketing-practitioner/
  .codex-plugin/plugin.json
  assets/brand/                  # Referenced plugin logos and README banner
  skills/marketing-practitioner/   # Entire directory, including resources and scripts
  LICENSE
  THIRD_PARTY_NOTICES.md
```

Use the existing files as the source of truth. Do not maintain a second copy of the skill in the repository. Keep the plugin version aligned with the skill's `metadata.version` when preparing releases. A plugin package does not require `package.json` or an npm runtime.

The research reports and evaluation infrastructure remain in the repository for maintainers; they are not additional runtime skills. Do not include `.git`, local configuration, credentials, caches, or generated trial outputs in a distributed bundle.

## Install through a local catalog

This repository supplies the plugin package, not a public directory listing or a configured marketplace. Follow the current [OpenAI packaging instructions](https://developers.openai.com/plugins/build/plugins) to register it with a personal or team catalog.

For a separate local catalog, place the package at `plugins/marketing-practitioner` beneath the catalog root. Register an entry named `marketing-practitioner` whose local source path is `./plugins/marketing-practitioner`. Use `AVAILABLE` installation policy, `ON_INSTALL` authentication policy, and category `Productivity`; this skill-only package itself requires no account authentication.

For example, create `.agents/plugins/marketplace.json` under that separate catalog root:

```json
{
  "name": "marketing-local",
  "interface": { "displayName": "Marketing Local" },
  "plugins": [
    {
      "name": "marketing-practitioner",
      "source": {
        "source": "local",
        "path": "./plugins/marketing-practitioner"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

On a Codex CLI supporting `plugin add`, register the catalog root and install its entry:

```text
codex plugin marketplace add <local-catalog-root>
codex plugin add marketing-practitioner@<catalog-name>
```

Replace both placeholders with the actual catalog path and its declared name. The default personal catalog has its own discovery flow; see the official instructions before adding a second catalog. CLI and desktop availability can differ by version. Start a new task after installation so the host can discover the installed skill.

## Verify a package

1. Validate the plugin manifest with the current `plugin-creator/scripts/validate_plugin.py` from a Codex installation that includes that skill.
2. Run the repository's `scripts/verify.ps1 -PackageOnly` against the packaged skill using `-SkillPath`.
3. Run the packaged `scripts/get-knowledge.py --validate` to check route and source targets after relocation.
4. Confirm the host discovers Marketing Practitioner in a new task and can read a referenced handbook section. Use an approved-positioning writing request to check that the plugin leads to the existing skill.

Manifest validation, installation, resource integrity, and live agent behavior are separate checks. A successful install is not evidence that a model followed the marketing instructions correctly. Avoid enabling duplicate standalone and plugin installations of the same skill during a behavior check.

Packaging check on 2026-09-08: the manifest passed the installed Codex plugin validator, and a temporary catalog installed version 1.5.0 using an isolated Codex home. Every installed skill file matched the source bytes, and relocated retrieval validated 264 routes and 248 evidence sources. This check did not activate a live model task or publish the plugin.

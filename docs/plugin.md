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

## Install from the repository marketplace

The repository includes a native Codex catalog at [marketplace.json](../.agents/plugins/marketplace.json). Its local source `./` resolves from the repository root to the existing plugin. The separate Claude catalog remains available; both use the same skill files.

In the Codex app's marketplace controls, add `https://github.com/quocbao201104/marketing-practitioner.git`, then install Marketing Practitioner from the catalog. Menu labels vary by app version. This adds a user-selected marketplace, not an official directory listing.

On a compatible Codex CLI:

```text
codex plugin marketplace add https://github.com/quocbao201104/marketing-practitioner.git
codex plugin add marketing-practitioner@marketing-practitioner
```

Refresh or upgrade the marketplace and apply the plugin update when offered. An existing installation may still display the Claude-compatible catalog path until its marketplace registration is refreshed. Confirm the installed skill's `metadata.version` is `1.9.0`, then start a new task. Updating Git or downloading a release ZIP does not update the installed plugin cache.

See the [OpenAI marketplace format reference](https://learn.chatgpt.com/docs/enterprise/plugin-management#supported-formats) for native and compatible catalog layouts. For a separate local catalog, use a local source path relative to that catalog's root.

## Verify a package

1. Validate the plugin manifest with the current `plugin-creator/scripts/validate_plugin.py` from a Codex installation that includes that skill.
2. Run the repository's `scripts/verify.ps1 -PackageOnly` against the packaged skill using `-SkillPath`.
3. Run the packaged `scripts/get-knowledge.py --validate` to check route and source targets after relocation.
4. Confirm the host discovers Marketing Practitioner in a new task and can read a referenced handbook section. Use an approved-positioning writing request to check that the plugin leads to the existing skill.

Manifest validation, installation, resource integrity, and live agent behavior are separate checks. A successful install is not evidence that a model followed the marketing instructions correctly. Avoid enabling duplicate standalone and plugin installations of the same skill during a behavior check.

Packaging check on 2026-09-08: the manifest passed the installed Codex plugin validator, and a temporary catalog installed version 1.5.0 using an isolated Codex home. Every installed skill file matched the source bytes, and relocated retrieval validated 264 routes and 248 evidence sources. This check did not activate a live model task or publish the plugin.

Packaging check on 2026-09-09: the native repository marketplace installed v1.7.1 in an isolated Codex home. All installed skill files matched the repository bytes. The plugin manifest and full repository verification passed. This was an installation check, not a live model trial.
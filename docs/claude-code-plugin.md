# Claude Code marketplace

The repository is both a Claude Code marketplace and its single plugin. The catalog at [marketplace.json](../.claude-plugin/marketplace.json) points to the repository root, where [plugin.json](../.claude-plugin/plugin.json) declares the plugin. Claude Code discovers the existing `skills/marketing-practitioner/SKILL.md` through its default `skills/` directory. The Codex and Claude Code packages share the same runtime files.

After these manifests are pushed to GitHub, run inside Claude Code:

```text
/plugin marketplace add quocbao201104/marketing-practitioner
/plugin install marketing-practitioner@marketing-practitioner
```

Follow the installation prompt and reload plugins or restart the session if requested. Invoke the skill with:

```text
/marketing-practitioner:marketing-practitioner
```

For an existing marketplace installation, refresh the catalog before updating the plugin:

```text
/plugin marketplace update marketing-practitioner
/plugin update marketing-practitioner@marketing-practitioner
```

For testing unpushed files, add the local checkout path instead of the GitHub repository. Use the repository root, not the raw URL of `marketplace.json`: the catalog's relative source depends on the repository being available.

Validate both manifests from the repository root:

```text
claude plugin validate .claude-plugin/plugin.json
claude plugin validate .claude-plugin/marketplace.json
```

Keep the Claude Code and Codex plugin versions aligned with the skill version when releasing. The plugin manifest is the version source for this marketplace entry; no duplicate version is declared in the catalog.

This configures a user-added Claude Code marketplace. It does not publish an official directory listing or configure ChatGPT web. See the official [marketplace guide](https://code.claude.com/docs/en/plugin-marketplaces) and [plugin reference](https://code.claude.com/docs/en/plugins-reference).

# Local setup: apps and CLI

Choose one installation method per host. All methods use the same `skills/marketing-practitioner` directory. Installing through both a plugin and a standalone folder can create duplicate entries.

## Codex app: install manually with files

1. On the [repository page](https://github.com/quocbao201104/marketing-practitioner), select **Code > Download ZIP**, then extract the download.
2. Open the extracted `skills` folder. Copy the entire `marketing-practitioner` folder, including its subfolders.
3. Open your personal skills directory using File Explorer or Finder:

   | System | Directory |
   | --- | --- |
   | Windows | Paste `%USERPROFILE%\.agents\skills` into File Explorer's address bar |
   | macOS / Linux | Open `~/.agents/skills` in your file manager; on macOS use **Go > Go to Folder** |

4. Create `.agents` and `skills` if they do not exist, then paste the skill folder inside `skills`. The final file should be `.agents/skills/marketing-practitioner/SKILL.md` under your home directory, with the handbook and other resources beside it.
5. Start a new Codex task. If the skill does not appear in the skill picker, restart the app. Select Marketing Practitioner and give it your task.

These are Codex's documented [user-level local skill locations](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills). This installs the skill directly; no marketplace setup or terminal is needed. For the plugin variant, use the separate [Codex catalog instructions](plugin.md).

## Claude desktop: install through the app

1. Open **Customize > Plugins** (through Settings if that is where your app places Customize).
2. Select **+ / Add plugin > Add marketplace**. Some interfaces show **Create plugin** before **Add marketplace**.
3. Choose **Add from a Repository** and enter `https://github.com/quocbao201104/marketing-practitioner`.
4. Select **Sync/Add**, open **Marketing Practitioner** in the added marketplace, and select **Install**.
5. Complete any activation prompt and start a new task using the plugin.

Menu labels and availability depend on your account and app version. See [Claude's plugin instructions](https://support.claude.com/en/articles/13837440-use-plugins-in-claude). Adding the repository to chat context alone does not install it.

## CLI

For a compatible agent, run the skill installer and select the host and installation scope when prompted:

```bash
npx skills add quocbao201104/marketing-practitioner
```

For Claude Code's plugin interface, run inside Claude Code:

```text
/plugin marketplace add quocbao201104/marketing-practitioner
/plugin install marketing-practitioner@marketing-practitioner
```

See [Claude Code activation and updates](claude-code-plugin.md). Codex plugin installation uses its own [local catalog](plugin.md).

## Ask your agent to install

If the host provides installation tools, paste:

```text
Install Marketing Practitioner from
https://github.com/quocbao201104/marketing-practitioner
for this app. Use its supported installation method and confirm
where it was installed. Preserve any existing customizations.
```

Follow any host permission or scope prompts. Confirm the skill/plugin is available afterward; a successful repository download alone is not an installation check.

## Keep it updated

Check for updates periodically and before starting a major project. A monthly check is a practical starting point, not an automatic schedule. Review the [changelog](../CHANGELOG.md) and use the same installation method you started with:

| Installed through | Update action |
| --- | --- |
| Codex manual folder copy | Download the newer source, back up your existing skill if customized, then replace only its `marketing-practitioner` folder with the complete new folder |
| Claude app marketplace | Sync/refresh the marketplace, then apply the plugin update when offered |
| Claude Code marketplace | Run the marketplace and plugin update commands in the [Claude Code guide](claude-code-plugin.md) |
| Codex local catalog | Refresh the source package/catalog and reinstall the updated plugin as described in the [catalog guide](plugin.md) |
| Skill installer | Use that installer's update flow, or reinstall this repository for the same host and scope |
| Web skill upload | Upload the newer complete package through that product's skill-management flow; avoid retaining duplicate active copies |

You can also ask the agent to check and update this skill while preserving your customizations. Start a new task after updating and confirm the installed version. Updating a repository checkout does not necessarily refresh an installed plugin cache or a separately uploaded skill.

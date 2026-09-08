# Web setup: Claude and ChatGPT

Use this guide for browser installation. For local apps and CLI, see the [README](../README.md#local-apps-and-cli), [Claude Code marketplace](claude-code-plugin.md), or [Codex plugin guide](plugin.md). All packages use the same marketing skill and reference files.

Instructions checked on **2026-09-08**. Account permissions and menu labels can vary. Provider documentation establishes the installation mechanisms; it does not certify this skill's marketing outputs.

## Claude: add the repository marketplace

1. Open **Settings**, then **Customize**, and select **Plugins**.
2. Select **Add plugin** or **+**. In interfaces that show it, choose **Create plugin**, then **Add marketplace**. Other interfaces show **+ > Add marketplace** directly under Personal plugins.
3. Choose **Add from a Repository** and paste:

   ```text
   https://github.com/quocbao201104/marketing-practitioner
   ```

4. Select **Sync/Add** to load the repository's marketplace catalog.
5. Select **Marketing Practitioner** from that marketplace and choose **Install (+)**. Follow any review or activation prompt.
6. Start a conversation with the first-task example in the README.

The repository includes `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`; you do not need to create a plugin or edit JSON yourself. Adding a marketplace makes its catalog available; select and install the plugin afterward.

This sequence incorporates the maintainer's reported interface path. Anthropic documents **Customize > Plugins > Personal plugins (+) > Add marketplace**, including adding a GitHub repository or git URL. If your interface differs, use the current [Claude plugin instructions](https://support.claude.com/en/articles/13837440-use-plugins-in-claude). If the controls are missing, check account/workspace availability.

## ChatGPT: upload a personal skill

**Plan and workspace requirement:** OpenAI lists Skills for eligible **Business, Enterprise, Healthcare, and Edu** users, subject to product availability and workspace settings. Do not assume a Free, Plus, or Pro account has personal skill upload simply because it has ChatGPT or Codex access. Administrators can separately control skill creation, uploading, and installation.

1. Prepare the complete `marketing-practitioner` skill folder as described below.
2. In the ChatGPT sidebar, open **Plugins**.
3. Select the **Skills** tab.
4. Select **Create > Upload from your computer**.
5. Supply the skill in the format the uploader accepts, keeping its supporting resources together. Complete the scan/review and installation flow shown by your workspace.
6. Confirm it appears in your Skills list, then try the README's first-task example.

OpenAI documents these controls in [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt). That page does not specify an archive layout; acceptance of this repository's ZIP still needs confirmation in an eligible account. If the uploader rejects it, retain the exact error before changing the package.

There is no public Marketing Practitioner entry in the ChatGPT plugin directory from this project yet. This personal-skill upload path does not require such a listing. Adding a GitHub link to a conversation or connecting GitHub is not the same as installing the skill.

## Prepare files for manual skill upload

On the [repository page](https://github.com/quocbao201104/marketing-practitioner), choose **Code > Download ZIP** and extract it. Locate `skills/marketing-practitioner`. Keep that entire folder, including `SKILL.md`, the handbook, index, references, platforms, adaptations, and scripts.

For Claude's alternative custom-skill upload, compress that folder into a ZIP with `marketing-practitioner/SKILL.md` inside it, then upload through **Customize > Skills** and enable it. The outer repository and `skills/` folders should not wrap the skill in this ZIP. See [Claude's custom skill packaging instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

Maintainers can also use the [skill package builder](skill-package.md). The Codex plugin manifest and the full repository ZIP are different from this skill upload package. For ChatGPT, follow the uploader's accepted format rather than assuming Claude's ZIP layout is guaranteed to work.

## Check the setup

Confirm the skill/plugin is installed and enabled, then ask for a small marketing artifact using an approved price and product facts. Check that the assistant can read a relevant reference and preserves those facts. Installation, reference access, and useful marketing behavior are separate checks.

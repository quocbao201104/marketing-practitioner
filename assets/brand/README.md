# Repository and plugin branding

These assets are built from the approved [vector kit](../logo-vector-20260908/README.md):

- `banner.svg`: outlined name lockup on an ivory background for the repository README.
- `logo.png`: transparent color symbol, 512 px, for the Codex logo and composer icon.
- `logo-dark.png`: transparent white symbol, 512 px, for the Codex dark-mode logo.

Rebuild with `python -B scripts/build_brand_assets.py` from the repository root. Edit the vector kit's source and rebuild that kit before regenerating these derived assets. The kit includes the font license and editable source; the banner itself needs no installed font.

Codex declares these paths in `.codex-plugin/plugin.json`. The [Claude Code manifest schema](https://code.claude.com/docs/en/plugins-reference#plugin-manifest-schema) does not document an equivalent logo field, so no custom field is added to its manifest.

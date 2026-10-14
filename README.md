# Roukmoute's published blog

**English** · [Français](README.fr.md)

This repository contains the generated files for
[roukmoute.github.io](https://roukmoute.github.io/) and its Pages deployment.
French is the website default, with a complete English edition under `/en/`.

Article sources, drafts and their history are kept in the private
`roukmoute/blog-sources` repository. Edit content and publication dates there.
Only reviewed articles marked `scheduled` and due in Europe/Paris can be
exported here. All articles are currently drafts while the author revises them.

The private build checks publication eligibility every Wednesday at 10:17
Europe/Paris, and after main updates. A dedicated deploy key can update this
repository only. A public push triggers the Pages workflow, which packages
only the generated files listed in `blog-manifest.json`.

Keep `.github/` and these README files when synchronizing generated output.
Do not add Markdown articles, source history, private previews or credentials.

# Fixing or adding a card

1. Edit `data/stacks/<handle>.json` (or add one; see `data/SCHEMA.md`).
2. Every new or changed value needs a public `source` URL and a `seen` date. Quotes are copied verbatim.
3. Run `python3 data/validate.py`.
4. Open a pull request. If it's your own card, say so in the PR: we'll take your word for your own setup.

Removal requests: open an issue titled "Remove <name>", or email stacks@prehistoriq.com.

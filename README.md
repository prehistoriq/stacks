# Stacks: how engineers actually use coding agents

The data behind [prehistoriq.com/stacks](https://prehistoriq.com/stacks): one JSON file per person in
[`data/stacks/`](data/stacks/), describing the coding agents, models, harness, rules files, skills and
review habits they have **publicly** described, every claim with a link to the source and a date.

**Is this you?** Click "Edit this card on GitHub" on your card (or edit `data/stacks/<you>.json` here) and
open a pull request. We merge corrections from the person themselves without argument. Want your card
removed? Open an issue or email stacks@prehistoriq.com and it's gone.

## The rules
- **No source, no claim.** Every value has `source` (a public URL) and `seen` (when it was said).
- **Their own words.** Only first-person sources about their own setup; courses and product pitches
  don't count. Quotes are verbatim; `[brackets]` mark our fix of a mis-transcribed name.
- **Our readings are marked.** Anything we inferred (e.g. a model taken from commit co-author lines) has `"inferred": true`.
- **Recent or not shown.** Cards whose newest source is older than six months are not shown on the site.
- **Archetype and "one thing" are our editorial picks**, playful labels, not ratings.

The format is in [`data/SCHEMA.md`](data/SCHEMA.md). `python3 data/validate.py` checks every file; CI runs it on each PR.
[`card.md`](card.md) is the exact instruction your agent gets when you make your own card on the site.

## License
The compilation (structure, labels, selections) is [CC BY 4.0](LICENSE). Quotes belong to the people who said them.

Made by Prehistoriq. We're building a code review tool, which is why every card says how that person reviews agent code.

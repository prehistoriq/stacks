# Stack card data, schema v2

One file per person: `data/stacks/<handle>.json`. `handle` = their GitHub login, lowercase
(X handle if they have no GitHub).

**Inferred values:** if a value is your reading rather than their words (a model taken from commit
co-author lines, an order you chose, a number you derived), add `"inferred": true` to that object and say why
in `notes`. The page marks inferred values.

**Rule: no source, no field.** Every claim has `source` (a public URL that contains the claim) and
`seen` (ISO date the claim was made or published; for repo files, the date of the commit you read).
Quotes are verbatim, copied from the source, never paraphrased. If you cannot find a source, leave the
field `null`.

```jsonc
{
  "schema": 2,
  "handle": "simonw",
  "status": "ok",                  // "ok" (shown) | "stale" (newest source older than six months, set by data/sweep.py) | "insufficient" (fewer than 5 sourced fields among agents..signature)
  "checked": "2026-10-06",         // the day you researched
  "notes": "",                     // private: anything the editor should know (doubts, conflicts, what you could not verify). Never published.

  "name":   { "value": "Simon Willison", "source": "https://github.com/simonw" },  // the name people know them by
  "x":      { "value": "simonw", "source": "https://x.com/simonw" },              // or null
  "github": { "value": "simonw", "source": "https://github.com/simonw" },         // or null
  "site":   { "value": "https://simonwillison.net", "source": "https://github.com/simonw" }, // or null
  "avatar": { "value": "https://avatars.githubusercontent.com/u/9599?v=4", "source": "https://github.com/simonw" }, // GitHub avatar only, never other photos; null if no GitHub
  "known_for": { "value": "Datasette, LLM CLI, co-creator of Django", "source": "https://simonwillison.net/about/" }, // max ~32 chars

  // Coding agents they use, primary first. Max 3. `icon` = a key from icons/ or null.
  "agents": [
    {
      "name": "Claude Code", "icon": "claudecode",
      "role": "primary",            // short, optional: "primary", "plans and reviews", "for side projects"...
      "surface": "cli",             // REQUIRED when known: "cli" | "app" (desktop/mobile app) | "ide" (editor/IDE) | "web" (browser/cloud agent)
                                    // must be supported by the source; if the source does not say, null. A switch (CLI -> app) goes in history.
      "surface_source": { "source": "…", "seen": "…", "quote": "verbatim" },  // optional: when the surface comes from a different source than the agent's own quote
      "source": "https://…", "seen": "2026-09-30",
      "quote": "verbatim sentence from the source that shows they use it",
      "history": [                  // optional: earlier claims that changed, oldest first
        { "value": "Cursor", "surface": "ide", "source": "https://…", "seen": "2025-03-01", "quote": "verbatim" }
      ]
    }
  ],

  // Models, as they name them, most used first. Max 2. icon: "claude" | "openai" | "gemini" | … or null.
  "models": [
    { "name": "Claude Opus 4.6", "icon": "claude", "detail": "high effort",   // detail optional, short
      "source": "https://…", "seen": "2026-08-12", "quote": "verbatim", "history": [] }
  ],

  // How they review agent-written code. The product question; quote them.
  "review_style": { "value": "Reads every diff", "source": "…", "seen": "…", "quote": "verbatim",
                    "kind": "reads-all",    // REQUIRED: reads-all | spot-checks | agent-reviews (another model/agent reviews) | tests-only | no-review | unknown
                    "also": [ { "source": "…", "seen": "…", "quote": "verbatim" } ] },   // or null

  "harness":     { "value": "Terminal, tmux, git worktrees", "short": "worktrees",   // short = 1-2 words for the card
                   "source": "…", "seen": "…", "quote": "verbatim", "history": [] },      // or null
  "parallelism": { "value": 8, "short": "8 agents", "source": "…", "seen": "…", "quote": "verbatim", "history": [] }, // only a number they said; else null
  "rules_files": { "value": "CLAUDE.md", "short": "CLAUDE.md", "url": "link to the actual public file",
                   "source": "…", "seen": "…", "quote": "verbatim line from the file or post" },  // or null
  "skills":      { "value": ["name", "name"], "count": 12, "featured": ["max 3 names"],
                   "source": "…", "seen": "…" },                                          // or null
  "mcp_servers": { "value": ["playwright", "github"], "source": "…", "seen": "…", "quote": "verbatim" }, // or null
  "hooks":       { "value": ["pre-commit test runner"], "source": "…", "seen": "…", "quote": "verbatim" }, // or null

  // OUR pick: the one standout thing in their setup that makes it unlike anyone else's.
  // Must be something named in their own sources (a skill, hook, MCP server, tool, script, habit).
  "signature": { "value": "$autoreview", "kind": "skill",        // kind: skill | hook | mcp | tool | habit | rule
                 "caption": "before every commit",               // max ~28 chars, completes the value
                 "why": "one sentence, why this is their standout", "editorial": true,
                 "source": "…", "seen": "…", "quote": "verbatim" },

  // OUR label. One of: Orchestrator, Purist, Swarm Lord, Rules Lawyer, Skeptic, Vibe Maximalist, Toolsmith.
  "archetype": { "value": "Toolsmith", "editorial": true, "why": "one short sentence grounded in the fields above" },

  "signature_quote": { "value": "short verbatim quote about how they work with agents", "more": "optional next sentence",
                       "source": "…", "seen": "…" }
}
```

Icon keys available in `icons/`: amp, anthropic, claude, claudecode, cline, codex, cursor, deepseek,
gemini, geminicli, githubcopilot, grok, kimi, minimax, mistral, openai, opencode, qwen, windsurf, xai, zai.
Use `null` for anything else (for example Aider) and say so in `notes`.

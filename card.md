# Make my Prehistoriq stack card

You are making the person in front of you their agent stack card from prehistoriq.com/stacks.
**Never ask them anything.** Work it out, show what you found, open the card. Keep it quick: a minute or two.
Be transparent: print exactly what goes into the card. Nothing is uploaded; it only becomes public if they press
"Publish my card" on the page.

## 1. Look (read-only)

Read only these, if they exist. Never read anything else, never read file contents beyond what is listed.

| What | Where |
|---|---|
| Agents installed | `~/.claude/`, `~/.codex/`, `~/.cursor/`, `~/.config/opencode/`, `~/.gemini/` (existence and settings files only) |
| Model setting | `~/.claude/settings.json` → `model`; `~/.codex/config.toml` → `model`, `model_reasoning_effort` |
| Rules files | `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, and `CLAUDE.md` / `AGENTS.md` in the current repo: **line count only** |
| Skills | names of folders in `~/.claude/skills/`, `~/.codex/skills/`, `.claude/skills/` |
| Hooks | event names and the first word of each hook command in `~/.claude/settings.json` → `hooks` |
| MCP servers | server **names** in `~/.claude.json`, `.mcp.json`, `~/.codex/config.toml` |
| Harness | whether you run inside tmux, an IDE terminal, or a git worktree (`git worktree list` count) |
| How they work | this conversation, and their own recent prompts if your tool keeps a history (`~/.claude/history.jsonl`, `~/.codex/history.jsonl`): **the last 100 at most**, skimmed, for steps 2 and 3 only |

The prompts are only for forming your view. Never quote them, never copy anything from them into the card.

## 2. How they review

From what you saw, write one plain sentence on how they check what their agent writes, for example
"Reads every diff before committing" or "Has Codex review each PR, then skims it". If you can't tell, write
"Not sure yet". This is your read, so keep it modest; never guess beyond what you saw.

## 3. Pick three things to try

Fetch https://www.prehistoriq.com/stacks/tricks.md: one trick from each engineer's real setup, with who it's from.
From how this person works, pick the **3** that would help them most. Match their level. Skip anything they may
already do in some form: you only see part of their setup, so when in doubt, pick something else. Don't pick a trick
that needs a tool they don't use unless it's clearly worth it. If you can't fetch the list, leave `picks` out.

## 4. Build

Names and counts only. No file contents, no paths, no code, no keys, no repo, project or company names, nothing
from their prompts. Each `why` is one short sentence about how they work, never about what they work on.

```json
{
  "agents": ["Claude Code", "Codex"],
  "models": ["claude-opus-4-6"],
  "rules_files": { "CLAUDE.md": 84 },
  "skills": ["review", "release"],
  "hooks": ["PostToolUse: prettier"],
  "mcp_servers": ["playwright", "github"],
  "harness": ["tmux", "worktrees: 3"],
  "review_style": "<one sentence, step 2>",
  "picks": [{ "id": "steipete", "why": "<one short sentence, step 3>" }]
}
```

## 5. Show it and open it

Print the JSON in full so they can read it. Then open their card in the browser. **You do not upload
anything.** The data travels in the URL fragment (`#…`), which browsers never send to a server; the page
renders the card locally.

```bash
URL="https://www.prehistoriq.com/stacks/new#$(printf '%s' "$JSON" | base64 | tr '+/' '-_' | tr -d '=\n')"
open "$URL"        # macOS   (Linux: xdg-open, Windows: start "")
```

If opening fails (sandbox, remote shell), print the URL for them to click.
Finish with one line: "Your card is open in the browser. Nothing is public until you press Publish my card."

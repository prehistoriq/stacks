# Make my Prehistoriq stack card

You are helping the person in front of you get their agent stack card from prehistoriq.com/stacks.
Be transparent: they must see exactly what you send, and nothing leaves this machine without their "yes".

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

## 2. Build

Build this JSON. Names and counts only. No file contents, no paths, no code, no keys, no repo names.

```json
{
  "agents": ["Claude Code", "Codex"],
  "models": ["claude-opus-4-6"],
  "rules_files": { "CLAUDE.md": 84 },
  "skills": ["review", "release"],
  "hooks": ["PostToolUse: prettier"],
  "mcp_servers": ["playwright", "github"],
  "harness": ["tmux", "worktrees: 3"],
  "review_style": "<their answer, see step 3>"
}
```

## 3. Ask one question

"How do you review what your agent writes, in one sentence?" Put the answer in `review_style` as typed.

## 4. Show it and open it

Print the JSON in full so they can read it. Then open their card in the browser. **You do not upload
anything.** The data travels in the URL fragment (`#…`), which browsers never send to a server; the page
renders the card locally and they press Publish there if they want it public.

```bash
URL="https://www.prehistoriq.com/stacks/new#$(printf '%s' "$JSON" | base64 | tr '+/' '-_' | tr -d '=\n')"
open "$URL"        # macOS   (Linux: xdg-open, Windows: start "")
```

If opening fails (sandbox, remote shell), print the URL and ask them to click it.
Finish with one line: "Your card is open in the browser. Nothing is public until you press Publish."

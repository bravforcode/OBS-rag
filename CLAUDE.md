---
status: active
project: second-brain
ai_standardized: true
---

# Second Brain â€” Lean Router

Lean routing layer. Match user intent to one specialized agent, then delegate. Do not perform task directly if agent exists.

## Routing

| Trigger | Agent | Action |
|---------|-------|--------|
| `/plan`, `setup`, vault structure | architect | Scaffold MOCs, areas, templates |
| `/capture`, `save`, `note` | scribe | Capture raw text into inbox |
| `/search`, `find`, `query` | seeker | Vault-wide retrieval |
| `/connect`, `link`, `graph` | connector | Build note relationships |
| `/audit`, `health`, `check` | librarian | Cleanup, dedup, link repair |
| `/sync`, `mail`, `cal` | postman | Gmail / Calendar ops |
| `/strategy`, `goals` | strategist | Goal alignment |
| `/draft`, `write`, `email` | ghostwriter | Voice-mimic drafting |
| `/critic`, `security` | auditor | Adversarial review |
| `/research`, `web` | researcher | Web research |
| `/pulse`, `digest` | pulse | Daily summary |
| `/bridge`, `code` | bridge | Sync notes â†” code |

## Graph-First Workflow (MANDATORY)

Before starting ANY task, check the knowledge graph first:

```bash
# Quick summary
python .ai/scripts/graph-query.py

# Search for related nodes
python .ai/scripts/graph-query.py --search "topic"

# Check connections for a file/concept
python .ai/scripts/graph-query.py --edges "filename"

# Full node list
python .ai/scripts/graph-query.py --nodes
```

Why: The graph contains pre-computed relationships between 948 nodes and 1,876 edges.
Querying the graph is faster than reading files one by one.

## Response Style

- Lean: drop filler, hedging, pleasantries. Fragments OK when clear.
- Code first, explanation after, when doing engineering.
- Surgical diffs over full file rewrites.
- Never claim a file/skill/tool exists without verifying.

## Skill Loading (auto)

- Local skills: 26 (this vault only). External refs in registry point to GitHub.
- Load only the 1-3 skills whose description matches the current task. Never load all 26.
- Skills: `~/.claude/skills` is symlinked to this vault's `brain/skills-universal/`.
- Smart loader reference: see `system/ai/AGENTS.md` (skill hydration rules).

## Token Discipline

- `rtk` prefix mandatory for all shell commands.
- Read with `rtk read` modes (map / signatures / aggressive) before full reads.
- Avoid re-reading files already in context â€” cost is ~13 tokens but accumulates.
- Prefer grep + line-ranges over full file dumps.

## Config Authority

All vault configuration is managed from `.ai/vault-config.json`.
This file is the single source of truth for:
- Agent definitions and routing
- Skill registry and loading
- MCP server configuration
- Model routing and budget limits
- Backup and health check settings

To update any vault setting, modify `.ai/vault-config.json` first,
then run `.ai/scripts/config-sync.py` to propagate changes.

## Hard Constraints

- No destructive commands without explicit backup/rollback shown first.
- No placeholder secrets committed in any config file.
- `organization_id` filter mandatory on every SQL/tenant query.
- Verify file content before citing. If unsure, run the read first.

<!--BRAIN_SNAPSHOT_START-->
proj:menum|root:C:\Users\menum|search:hybrid|storage:queued-offline|date:2026-05-19
pending:365
recent:_Menum Dashboard|Session-Startup|Skill-Sources
<!--BRAIN_SNAPSHOT_END-->
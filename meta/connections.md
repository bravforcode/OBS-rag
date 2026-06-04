---
type: connections
status: active
last_updated: '2026-06-04'
---

# Connections

All integrations and connections for the Second Brain vault.

## Active Connections

| System | Status | Details |
|--------|--------|---------|
| GitHub | ✅ Connected | `bravforcode/OBS-rag.git` — 475 files, auto-sync |
| Gmail | ✅ Configured | MCP server enabled |
| Google Calendar | ✅ Configured | MCP server enabled |
| Claude Code | ✅ Active | CLAUDE.md router + 15 agents |
| Obsidian | ✅ Active | 9 community plugins |
| Git Backup | ✅ Automated | Daily 22:00 via Windows Task Scheduler |

## GitHub Repo

- **URL**: https://github.com/bravforcode/OBS-rag
- **Branch**: main
- **Files**: 475 tracked
- **Size**: ~940KB
- **Last Push**: 2026-06-04

## MCP Servers

| Server | Type | URL |
|--------|------|-----|
| Gmail | HTTP | https://gmail.mcp.claude.com/mcp |
| Google Calendar | HTTP | https://gcal.mcp.claude.com/mcp |

## How to Sync

### Push (vault → GitHub)
```bash
cd "C:\Users\menum\Documents\ObsidianVault\Second Brain"
git add -A && git commit -m "update: description" && git push
```

### Pull (GitHub → vault)
```bash
cd "C:\Users\menum\Documents\ObsidianVault\Second Brain"
git pull
```

### Automatic Backup
- **Schedule**: Daily at 22:00
- **Script**: `.ai/scripts/vault-backup.py`
- **Task**: `SecondBrain-DailyBackup` (Windows Task Scheduler)

## Excluded from Git

These are synced via Obsidian or manual copy:
- `skills/` — external skill repos (165MB)
- `brain/` — universal skills hub (42MB)
- `Backups/` — local backups
- `01-projects/*/delta/` — session logs
- `01-projects/*/sessions/` — session data

## Related
- [[dashboard]]
- [[master-ai-rules]]

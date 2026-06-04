---
type: changelog
status: active
---

# Changelog

All notable changes to the Second Brain vault.

## [2.0.0] - 2026-06-04

### Security
- Removed hidden VBScript (`Run-WatcherHidden.vbs`) and background watcher
- Created `MASTER_AI_RULES.md` with enterprise governance rules
- Fixed hardcoded Windows paths to relative paths
- Added comprehensive `.gitignore` for proper version control

### Structure
- Split `MOC-root-skills.md` (688KB → 4 organized sub-MOCs)
- Replaced `MOC-root-resources.md` (100KB → clean organized MOC)
- Fixed `Atlas.md` duplicate entries
- Fixed `skills/Index.md` removed UUID-based entries and duplicates
- Fixed `tag-taxonomy.md` (was truncated, now complete)
- Fixed `user-profile.md` (was empty, now populated)

### Governance
- Created `MASTER_AI_RULES.md` — single source of truth for all AI operations
- Created `CHANGELOG.md` — this file
- Updated `CLAUDE.md` and `01-projects/CLAUDE.md` with relative paths
- Updated `.gitignore` with proper exclusions

### Tooling
- Created `vault-backup.py` — automated backup script
- Created `vault-health-check.py` — vault diagnostics
- Created `.github/workflows/validate-graph.yml` — CI link checking

### Cleanup
- Removed 9 `.bak` files from vault
- Removed `__pycache__` directories
- Removed log files from `.ai/logs/`
- Removed empty `Untitled.canvas` and `split_moc.py` from root

## [1.0.0] - 2026-04-06

### Added
- Initial vault creation with PARA structure
- 15 templates across all life areas
- 12 specialized agents
- Smart Skill Loader system
- Multi-tool compatibility (Claude, Cursor, Windsurf, Codex, Copilot)
- MCP integration (Gmail, Google Calendar)
- Token discipline system (RTK prefix, read modes)

---
type: architecture
status: active
last_updated: '2026-06-04'
---

# Architecture

System architecture of the Second Brain vault.

## Overview

The Second Brain is an AI-powered knowledge management system built on Obsidian. It uses PARA methodology for organization, multi-agent architecture for automation, and cross-tool compatibility for maximum flexibility.

## Core Components

```
Second Brain/
├── MASTER_AI_RULES.md          # Global governance (source of truth)
├── CLAUDE.md                   # Claude Code router
├── Dashboard.md                # Main dashboard
├── Atlas.md                    # Navigation hub
├── .claude/                    # Claude Code config
│   ├── agents/                 # 15 agent definitions
│   ├── skills/                 # 17 vault-specific skills
│   ├── hooks/                  # Pre/post tool hooks
│   └── references/             # Agent orchestration docs
├── .ai/                        # AI automation
│   ├── scripts/                # Python/PowerShell tools
│   ├── model-router.json       # LLM provider routing
│   └── budget-config.json      # Token budget limits
├── .github/                    # GitHub integration
│   ├── copilot-instructions.md # Copilot/Codex config
│   ├── scripts/check_links.py  # Link validation
│   └── workflows/              # CI/CD
├── 00-Inbox/                   # Capture point
├── 01-projects/                # Active projects (PARA)
├── 02-areas/                   # Life areas (PARA)
├── 03-resources/               # Reference material (PARA)
├── 04-archive/                 # Completed content (PARA)
├── 05-people/                  # Contacts
├── 06-meetings/                # Meeting notes
├── 07-daily/                   # Daily notes
├── MOC/                        # Maps of Content
├── Meta/                       # Vault governance
├── Templates/                  # 15 note templates
├── System/                     # Identity, constraints, voice
├── Knowledge/                  # Playbooks, failure analyses
├── Intelligence/               # Strategic reports
├── skills/                     # Third-party skills
├── brain/                      # Universal skills hub
├── CRM/                        # Contact management
├── Journal/                    # Daily/weekly journals
└── Operations/                 # Tasks, submissions, opportunities
```

## Agent Architecture

```
User Input → CLAUDE.md (Router) → Agent Selection → Task Execution
                    ↓
            ┌───────────────┐
            │  Routing Table │
            ├───────────────┤
            │ /plan → architect │
            │ /capture → scribe │
            │ /search → seeker  │
            │ /connect → connector │
            │ /audit → librarian │
            │ /sync → postman │
            │ /strategy → strategist │
            │ /draft → ghostwriter │
            │ /critic → auditor │
            │ /research → researcher │
            │ /pulse → pulse │
            │ /bridge → bridge │
            └───────────────┘
```

## Data Flow

1. **Capture**: Scribe captures raw input to 00-Inbox/
2. **Process**: Sorter triages and moves to correct PARA folder
3. **Connect**: Connector builds wiki-links between notes
4. **Index**: MOC files provide navigation structure
5. **Search**: Seeker retrieves information across vault
6. **Maintain**: Librarian runs health checks and cleanup

## Security Model

- **Governance**: MASTER_AI_RULES.md (single source of truth)
- **Protection**: .claude/hooks/protect-system-files.sh blocks runtime modification
- **Validation**: .claude/hooks/validate-frontmatter.sh ensures frontmatter integrity
- **Credentials**: Stored in environment variables, never in files
- **Version Control**: Git with comprehensive .gitignore

## Multi-Tool Compatibility

| Tool | Config | Purpose |
|------|--------|---------|
| Claude Code | CLAUDE.md | Primary AI router |
| Cursor | .cursorrules | IDE integration |
| Windsurf | .windsurfrules | IDE integration |
| GitHub Copilot | .github/copilot-instructions.md | VS Code AI |
| Codex | .codex/ | OpenAI integration |
| Antigravity | .antigravity/ | IDE integration |

All tools read from the same vault, share the same skill system, and follow the same governance rules.

## Performance Considerations

- **File count**: ~5,443 markdown files (Obsidian degrades >10K)
- **MOC sizing**: Individual MOCs kept under 50KB
- **Skill loading**: Max 2000 tokens per session
- **Token budget**: 500K daily soft limit, 1M hard limit
- **Backup**: Automated daily backups via vault-backup.py

# GitHub Copilot / Codex Smart Skill Integration

## Overview
This repository uses a unified skill system from Obsidian vault.
**Location:** `C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal`

## Skill Auto-Loading

### When User Says:
- "use skills", "ใช้สกิล", "load skills"
- Task clearly matches skill pattern

### Auto-Detect by File Type:
| Extension | Skill to Load |
|-----------|---------------|
| .test.ts, .spec.ts | tdd-workflow |
| .test.py | tdd-workflow, python-testing |
| .tsx, .jsx | frontend-patterns |
| .py | backend-patterns, python-patterns |
| Dockerfile | docker-patterns, deployment-patterns |

### Auto-Detect by Keywords:
| Keyword | Skill |
|---------|-------|
| refactor | refactor-clean |
| deploy, CI/CD | deployment-patterns |
| test, coverage | tdd-workflow |
| api, endpoint | backend-patterns, api-design |
| ui, component | frontend-patterns, ui-ux-pro-max |
| security, auth | security-review |
| bug, debug | focused-fix |

## Skill Loading Protocol

### Step 1: Detect Context
- Read current file extension
- Check project path (graxia-os, vibecity, taskam)
- Match keywords in user request

### Step 2: Load from Registry
```
Read: C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-universal\skills-registry-compact.json
Select: Top 1-3 skills by relevance score
```

### Step 3: Apply Skill
```
Load: [skill-id]/SKILL.md
Execute: Follow skill instructions for current task
```

## Token Efficiency
- Load only selected skills (not all 1,390)
- Typical: 1 skill = ~1000 tokens
- Complex tasks: 2-3 skills = ~1500-2000 tokens

## Cross-Tool Sync
This copilot-instructions.md works alongside:
- `.cursorrules` (Cursor IDE)
- `.windsurfrules` (Windsurf)
- `CLAUDE.md` (Claude Code)
- All reading from same Obsidian vault

## Example Usage
```
User: "refactor this React component"
Copilot: [Load frontend-patterns, refactor-clean]
         "Using frontend patterns and clean refactoring..."
         [Executes refactor with skill guidance]
```


---

🔗 **Auto-Generated Links**

- [[CLAUDE]] - name_mentioned
- [[Work]] - name_mentioned
- [[CLAUDE]] - name_mentioned
- [[Project]] - name_mentioned
- [[Task]] - name_mentioned

📅 Auto-linked: 2026-04-28 18:30

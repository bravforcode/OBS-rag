---
status: unprocessed
project: TaskAm
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.213751'
---

---
project: TaskAm
type: moc
status: active
created: 2026-04-09
updated: 2026-04-09
source: auto-sync
tags:
  - area/work
  - type/project
  - taskam
  - status/active
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# TaskAm Dashboard

## Live Status

### Active Tasks (Code Sync)
```dataview
TASK FROM "01-projects/TaskAm/Active-Tasks"
WHERE !completed
SORT file.mtime DESC
```

### Recent ADRs
```dataview
TABLE adr-number, title, status, date
FROM "01-projects/TaskAm/Decisions"
WHERE type = "adr"
SORT adr-number DESC
LIMIT 5
```

### Recent AI Sessions
```dataview
TABLE session-date, agent, commit
FROM "Meta/agent-log/TaskAm"
SORT session-date DESC
LIMIT 7
```

### Recent Learnings
```dataview
TABLE topic, created
FROM "02-areas/Dev-Practice/TaskAm-Learnings"
SORT created DESC
LIMIT 5
```

## Architecture Quick Links
- [[System-Overview]] · [[Frontend-Map]] · [[Backend-Map]] · [[Data-Flow]]
- [[API-Call-Graph]] · [[Database-Schema]]

## Sync Health
```dataview
TABLE last-sync, annotations-found, drift-warnings
FROM "Meta/health"
WHERE project = "TaskAm"
SORT last-sync DESC
LIMIT 1
```

## Sprint Board
```dataview
TABLE status, week
FROM "01-projects/TaskAm/Sprints"
SORT week DESC
LIMIT 4
```

<!-- AUTO-SYNC:START gracia-dashboard -->
## Gracia Brain

### Startup Brief
![[preflight.md]]

### Commands
```dataviewjs
const cmds = JSON.parse(await dv.io.load("Meta/AI/context-cache/taskam/commands.json") || "[]");
dv.table(["Label","Kind","Risk","Command"], cmds.slice(0, 8).map(c => [c.label, c.kind, c.risk, `\`${c.command}\``]));
```

### Skills
```dataviewjs
const skills = JSON.parse(await dv.io.load("Meta/AI/context-cache/taskam/skills.json") || "[]");
dv.table(["Skill","Tokens","Summary"], skills.slice(0, 8).map(s => [s.skillName, s.tokens, (s.summary || '').slice(0, 90)]));
```

### Bundle Status
- Search mode: `fts-only`
- Storage mode: `online`
- Pending writes: `0`
- Estimated savings: `99%`
- Skills indexed: `0`
- Commands indexed: `30`
- Knowledge notes linked: `24`

### Knowledge Hubs
- [[AI Knowledge Hub|AI Knowledge Hub]]
- [[Agent Engineering|Agent Engineering]]
- [[Multi-Agent Orchestration|Multi-Agent Orchestration]]
- [[Sub-Agent Patterns|Sub-Agent Patterns]]
- [[Model Context Protocol|Model Context Protocol]]
- [[Evaluation & Observability|Evaluation & Observability]]
- [[GitHub Repos Watchlist|GitHub Repos Watchlist]]
- [[PubMed Research Watchlist|PubMed Research Watchlist]]

### Worktree Aliases
- _No worktree aliases registered._

### Quick Commands
```powershell
brain preflight --project taskam
brain context --project taskam --task "describe task"
brain run --project taskam --intent "run tests"
```
<!-- AUTO-SYNC:END gracia-dashboard -->

## 🔗 Semantic Connections
- [[_Menum Dashboard]]
- [[_VibeCity Dashboard]]
- [[Database-Schema]]

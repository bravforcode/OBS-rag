---
status: unprocessed
project: VibeCity
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.397083'
---

---
project: VibeCity
type: moc
status: active
source: gracia-brain
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# VibeCity Dashboard

<!-- AUTO-SYNC:START gracia-dashboard -->
## Gracia Brain

### Startup Brief
![[preflight.md]]

### Commands
```dataviewjs
const cmds = JSON.parse(await dv.io.load("Meta/AI/context-cache/vibecity/commands.json") || "[]");
dv.table(["Label","Kind","Risk","Command"], cmds.slice(0, 8).map(c => [c.label, c.kind, c.risk, `\`${c.command}\``]));
```

### Skills
```dataviewjs
const skills = JSON.parse(await dv.io.load("Meta/AI/context-cache/vibecity/skills.json") || "[]");
dv.table(["Skill","Tokens","Summary"], skills.slice(0, 8).map(s => [s.skillName, s.tokens, (s.summary || '').slice(0, 90)]));
```

### Bundle Status
- Search mode: `fts-only`
- Storage mode: `online`
- Pending writes: `0`
- Estimated savings: `97%`
- Skills indexed: `23`
- Commands indexed: `96`
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
- `C:\Users\menum\.cursor\worktrees\vibecity.live\bzk`
- `C:\Users\menum\.cursor\worktrees\vibecity.live\rme`

### Quick Commands
```powershell
brain preflight --project vibecity
brain context --project vibecity --task "describe task"
brain run --project vibecity --intent "run tests"
```
<!-- AUTO-SYNC:END gracia-dashboard -->

## 🔗 Semantic Connections
- [[_Menum Dashboard]]
- [[_TaskAm Dashboard]]
- [[preflight]]

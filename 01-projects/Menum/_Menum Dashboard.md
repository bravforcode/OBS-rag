---
status: unprocessed
project: Menum
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.154248'
---

---
project: Menum
type: moc
status: active
source: gracia-brain
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# Menum Dashboard

<!-- AUTO-SYNC:START gracia-dashboard -->
## Gracia Brain

### Startup Brief
![[Meta/AI/context-cache/menum/preflight.md]]

### Commands
```dataviewjs
const cmds = JSON.parse(await dv.io.load("Meta/AI/context-cache/menum/commands.json") || "[]");
dv.table(["Label","Kind","Risk","Command"], cmds.slice(0, 8).map(c => [c.label, c.kind, c.risk, `\`${c.command}\``]));
```

### Skills
```dataviewjs
const skills = JSON.parse(await dv.io.load("Meta/AI/context-cache/menum/skills.json") || "[]");
dv.table(["Skill","Tokens","Summary"], skills.slice(0, 8).map(s => [s.skillName, s.tokens, (s.summary || '').slice(0, 90)]));
```

### Bundle Status
- Search mode: `hybrid`
- Storage mode: `queued-offline`
- Pending writes: `361`
- Estimated savings: `100%`
- Skills indexed: `0`
- Commands indexed: `0`
- Knowledge notes linked: `24`

### Knowledge Hubs
- [[03-resources/AI-Knowledge/Maps/AI Knowledge Hub|AI Knowledge Hub]]
- [[03-resources/AI-Knowledge/Topics/Agent Engineering|Agent Engineering]]
- [[03-resources/AI-Knowledge/Topics/Multi-Agent Orchestration|Multi-Agent Orchestration]]
- [[03-resources/AI-Knowledge/Topics/Sub-Agent Patterns|Sub-Agent Patterns]]
- [[03-resources/AI-Knowledge/Topics/Model Context Protocol|Model Context Protocol]]
- [[03-resources/AI-Knowledge/Topics/Evaluation & Observability|Evaluation & Observability]]
- [[03-resources/AI-Knowledge/Maps/GitHub Repos Watchlist|GitHub Repos Watchlist]]
- [[03-resources/AI-Knowledge/Maps/PubMed Research Watchlist|PubMed Research Watchlist]]

### Worktree Aliases
- _No worktree aliases registered._

### Quick Commands
```powershell
brain preflight --project menum
brain context --project menum --task "describe task"
brain run --project menum --intent "run tests"
```
<!-- AUTO-SYNC:END gracia-dashboard -->

## 🔗 Semantic Connections
- [[_VibeCity Dashboard]]
- [[_TaskAm Dashboard]]
- [[Playbook-Suggestions]]

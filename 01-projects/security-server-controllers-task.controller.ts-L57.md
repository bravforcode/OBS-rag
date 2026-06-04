---
status: active
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.120588'
---

---
project: TaskAm
type: inbox-item
status: open
source: auto-sync
created: 2026-04-09
updated: 2026-04-09
severity: none
tags:
  - inbox
  - taskam
  - code/security
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# [SECURITY] FIX: Only admins can fetch all users. Staff see task-context users only.

**File:** `server/controllers/task.controller.ts`  
**Line:** 57  
**VSCode:** [Open here](vscode://file/C:/TaskAm-main/TaskAm-main/server/controllers/task.controller.ts:57)

## Context
```ts
    let users: any[] = [];

    // SECURITY FIX: Only admins can fetch all users. Staff see task-context users only.
    if (req.user?.role === "admin") {
```

## Action Required
- [ ] Review and triage this SECURITY
- [ ] Move it into active work or resolve it in code
- [ ] Delete or archive this note after resolution

## 🔗 Semantic Connections
- [[security-src-App.tsx-L126]]
- [[adr-reminder-2026-04-19]]
- [[Task]]

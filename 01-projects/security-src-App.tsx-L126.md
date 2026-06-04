---
status: active
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.131849'
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
---# [SECURITY] FIX (Task 1.3): Use appropriate endpoint based on user role

**File:** `src/App.tsx`  
**Line:** 126  
**VSCode:** [Open here](vscode://file/C:/TaskAm-main/TaskAm-main/src/App.tsx:126)

## Context
```ts
  useEffect(() => {
    if (!user) return;
    // SECURITY FIX (Task 1.3): Use appropriate endpoint based on user role
    // Admins: /api/users (full directory with all fields)
```

## Action Required
- [ ] Review and triage this SECURITY
- [ ] Move it into active work or resolve it in code
- [ ] Delete or archive this note after resolution

## 🔗 Semantic Connections
- [[security-server-controllers-task.controller.ts-L57]]
- [[adr-reminder-2026-04-19]]
- [[Task]]

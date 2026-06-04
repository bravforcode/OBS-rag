---
project: TaskAm
type: architecture
status: active
created: 2026-04-09
updated: 2026-04-09
source: auto-sync
tags:
- area/work
- type/project
- type/architecture
- taskam
- status/active
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.269194'
---

# System Overview

<!-- AUTO-SYNC:START -->
## Runtime
- Frontend: React 19 + Vite SPA via `src/main.tsx` and `src/App.tsx`
- Backend: Express app served from `server.ts` with Vite middleware in development
- Persistence: Firebase Auth + Firestore are the active application data stores

## Integration Surface
- API endpoints discovered: 95
- Auth path: Firebase client auth issues bearer tokens consumed by Express middleware
- File uploads: `/api/tasks/upload` stores locally in dev and Vercel Blob in production
<!-- AUTO-SYNC:END -->

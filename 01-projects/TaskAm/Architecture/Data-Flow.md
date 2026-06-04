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
last_audit: '2026-04-25T19:53:49.241268'
---

# Data Flow

<!-- AUTO-SYNC:START -->
## Request Flow
- React components call service modules under `src/services/*`.
- Service modules use the shared API client in `src/services/apiClient.ts` or direct `fetch` for uploads.
- Requests hit Express routers mounted from `server/routes/index.ts` under `/api`.
- Controllers and database query modules resolve data from Firestore and selected auxiliary services.

## Auth Flow
- Auth-related endpoints discovered: 6
- Firebase client tokens are attached to API requests and validated by backend middleware.

## Data Stores
- Firestore collections are used across controllers and query modules.
- Firestore rules and indexes are the primary schema/control artifacts for the live app.
<!-- AUTO-SYNC:END -->

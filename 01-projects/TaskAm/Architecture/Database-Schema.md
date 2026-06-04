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
last_audit: '2026-04-25T19:53:49.250076'
---

# Database Schema

<!-- AUTO-SYNC:START -->
> Last synced: 2026-04-20T10:32:59.517Z

## Firestore Collections

| Collection | Sample Doc Paths | Used In |
|------------|------------------|---------|
| _None detected_ |  |  |

## Type Shapes

### `Account`
> `tests/e2e/fixtures.ts`

| Field | Type |
|-------|------|
| `email` | `string` |
| `password` | `string` |
| `role` | `"admin" | "staff"` |
| `displayName` | `string` |

### `CreateTestAppOptions`
> `tests/setup/app.ts`

| Field | Type |
|-------|------|
| `notificationQueries` | `NotificationQueries` |

### `TestAppFactory`
> `tests/setup/app.ts`

| Field | Type |
|-------|------|
| `app` | `Express` |
| `testUsers` | `Map<string` |

### `TestUser`
> `tests/setup/app.ts`

| Field | Type |
|-------|------|
| `id` | `string` |
| `userId` | `string` |
| `authId` | `string` |
| `email` | `string | null` |
| `username` | `string` |
| `role` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `department_id` | `string | null` |
| `position` | `string | null` |
| `created_at` | `string` |

### `TestUser`
> `tests/setup/auth-helper.ts`

| Field | Type |
|-------|------|
| `id` | `string` |
| `userId` | `string` |
| `authId` | `string` |
| `email` | `string | null` |
| `username` | `string` |
| `role` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `department_id` | `string | null` |
| `position` | `string | null` |
| `created_at` | `string` |

### `TestUser`
> `tests/setup/mock-auth.ts`

| Field | Type |
|-------|------|
| `id` | `string` |
| `userId` | `string` |
| `authId` | `string` |
| `email` | `string | null` |
| `username` | `string` |
| `role` | `string` |
| `first_name` | `string` |
| `last_name` | `string` |
| `department_id` | `string | null` |
| `position` | `string | null` |
| `created_at` | `string` |

## Firestore Artifacts

- `firestore.rules`
- `firestore.indexes.json`
<!-- AUTO-SYNC:END -->

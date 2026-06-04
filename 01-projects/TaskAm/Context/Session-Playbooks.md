---
status: unprocessed
project: TaskAm
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:49.315544'
---

---
project: TaskAm
type: playbook
status: active
created: 2026-04-09
updated: 2026-04-09
source: manual
tags:
  - area/work
  - type/meta
  - taskam
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# Session Playbooks

## Auth Work
match: auth, login, logout, session, permission, role, jwt, token
skills:
- playwright
rules:
- Read API call graph and backend map for auth-related flows first.
checklist:
- Identify caller and route
- Confirm auth middleware / guard path
- Verify frontend redirect or session refresh behavior
note-hints:
- auth
- login
- token
- session
category-boosts:
- architecture: 16
- security: 10
- task: 6

## UI Implementation
match: ui, layout, component, design, page, responsive, css, frontend
skills:
- playwright
- ui-ux-pro-max
rules:
- Read frontend map and existing page/component patterns first.
checklist:
- Confirm target page/component
- Preserve existing design language unless asked to change it
- Verify desktop and mobile behavior
note-hints:
- frontend
- component
- page
- layout
category-boosts:
- architecture: 10
- overview: 6

## Data / Schema Work
match: database, schema, firestore, supabase, migration, query, collection
skills:
- backend-patterns
rules:
- Read database schema and infra manifest before changing data flow.
checklist:
- Identify affected collection/table
- Confirm read/write path
- Check migration or schema implications
note-hints:
- database
- schema
- collection
- query
category-boosts:
- architecture: 18
- resource: 8

## 🔗 Semantic Connections
- [[Global-Session-Playbooks]]
- [[Playbook-Suggestions]]
- [[Preferred-Skills]]

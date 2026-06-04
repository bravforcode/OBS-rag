---
status: unprocessed
project: unknown
area: unknown
ai_standardized: true
last_audit: '2026-04-25T19:53:50.259200'
---

---
project: TaskAm
type: resource
status: active
created: 2026-04-09
updated: 2026-04-09
source: auto-sync
tags:
  - area/work
  - type/resource
  - taskam
ai_reconnected: true
reconnected_at: 2026-04-25 19:48:41
---# TaskAm Infra Manifest

<!-- AUTO-SYNC:START -->
> Last synced: 2026-04-20T10:32:59.524Z

## Environment Variables Checklist

> Values are intentionally omitted. This note stores key names only.

### Configuration
- [ ] `ALLOWED_ORIGIN`
- [ ] `ANTHROPIC_MODEL`
- [ ] `ENABLE_QUICK_ROLE_LOGIN`
- [ ] `ENCRYPTION_KEY`
- [ ] `FIREBASE_CLIENT_EMAIL`
- [ ] `FIREBASE_PROJECT_ID`
- [ ] `FIREBASE_STORAGE_BUCKET`
- [ ] `GRACIA_VAULT_ROOT`
- [ ] `LINE_ADMIN_USER_ID`
- [ ] `NODE_ENV`
- [ ] `PORT`
- [ ] `REDIS_URL`
- [ ] `SEED_STAFF_EMAIL`
- [ ] `SEED_STAFF_FIRST_NAME`
- [ ] `SEED_STAFF_LAST_NAME`
- [ ] `SEED_STAFF_POSITION`
- [ ] `SEED_STAFF_USERNAME`
- [ ] `SESSION_FILES`
- [ ] `SESSION_PROMPT_SUMMARY`
- [ ] `SESSION_SUMMARY`
- [ ] `SMOKE_BASE_URL`
- [ ] `TRELLO_BOARD_ID`
- [ ] `VITE_APP_ENV`
- [ ] `VITE_ENABLE_QUICK_LOGIN`
- [ ] `VITE_FIREBASE_APP_ID`
- [ ] `VITE_FIREBASE_MESSAGING_SENDER_ID`
- [ ] `VITE_FIREBASE_PROJECT_ID`
- [ ] `VITE_FIREBASE_STORAGE_BUCKET`
- [ ] `VITE_QUICK_LOGIN_ADMIN_EMAIL`
- [ ] `VITE_QUICK_LOGIN_STAFF_EMAIL`

### Secrets
- [ ] `ANTHROPIC_API_KEY` 🔐
- [ ] `BLOB_READ_WRITE_TOKEN` 🔐
- [ ] `CRON_SECRET` 🔐
- [ ] `CSRF_SECRET` 🔐
- [ ] `FIREBASE_PRIVATE_KEY` 🔐
- [ ] `JWT_SECRET` 🔐
- [ ] `LINE_CHANNEL_ACCESS_TOKEN` 🔐
- [ ] `LINE_CHANNEL_SECRET` 🔐
- [ ] `TRELLO_API_KEY` 🔐
- [ ] `TRELLO_TOKEN` 🔐
- [ ] `VITE_FIREBASE_API_KEY` 🔐
- [ ] `VITE_FIREBASE_AUTH_DOMAIN` 🔐
- [ ] `VITE_QUICK_LOGIN_ADMIN_PASSWORD` 🔐
- [ ] `VITE_QUICK_LOGIN_STAFF_PASSWORD` 🔐

## Deploy / Build Scripts
- `npm run build` → `npm run build --workspace=frontend`
- `npm run build:be` → `npm run build --workspace=backend`
- `npm run deploy:production` → `bash scripts/deploy-production.sh`
- `npm run verify:deployment` → `bash scripts/deploy-verify.sh`
- `npm run orchestrate:deployment` → `bash scripts/complete-deployment-orchestrator.sh`

## Config Files Present
- `vercel.json`
- `firestore.rules`
- `firestore.indexes.json`
- `.env.example`

## Pre-Deploy Checklist
- [ ] Required environment variables are configured
- [ ] `npm run build` succeeds locally
- [ ] Firestore / Supabase permissions reviewed
- [ ] CORS origins reflect the production domain
- [ ] No secrets are committed into the repository
<!-- AUTO-SYNC:END -->

## 🔗 Semantic Connections
- [[TaskAm-Tech-Stack]]
- [[Database-Schema]]
- [[Active-Tasks]]

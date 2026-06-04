---
type: playbook
status: active
topic: deployment
---

# Deployment Playbook

How to deploy projects reliably.

## Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Build succeeds
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Rollback plan documented

## Deployment Steps
1. Pull latest changes
2. Run build
3. Run tests
4. Deploy to staging
5. Verify staging
6. Deploy to production
7. Monitor for issues

## Post-Deployment
- Verify health checks
- Check error logs
- Monitor performance metrics
- Notify team

## Rollback Procedure
1. Revert to previous version
2. Run database rollback if needed
3. Verify system stability
4. Document what went wrong

## Related
- [[knowledge/playbooks/index|Playbooks]]
- [[01-projects/backend/overview|Backend]]

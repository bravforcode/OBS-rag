---
description: Daily vault maintenance workflow - inbox triage, orphaned file detection, MOC updates
---

# Vault Maintenance Workflow

**Trigger:** `/maintenance` or `/daily-cleanup`

## Steps

1. **Check Vault Status**
   ```bash
   vault status
   ```
   // turbo: true

2. **Process Inbox**
   ```bash
   vault process-inbox --auto
   ```
   // turbo: true

3. **Check Link Integrity**
   ```bash
   vault check-links
   ```
   // turbo: true

4. **Update MOCs**
   ```bash
   vault update-mocs
   ```
   // turbo: true

5. **Generate Report**
   - Update [[📊 SYSTEM-STATUS]]
   - Log to [[📈 ANALYTICS-DASHBOARD]]
   - Update [[🔗 CONNECTION-MAP]] if major changes

## Output

- **Daily Report** with:
  - Files processed
  - Links fixed
  - MOCs updated
  - Health score

## Success Criteria

- [x] Inbox < 5 files
- [x] No broken links
- [x] All MOCs updated
- [x] Health score > 90

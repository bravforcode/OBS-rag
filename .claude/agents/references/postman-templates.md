# Postman — Note Templates

## Email with Action Required

```markdown
---
type: email-action
date: {{email date}}
from: "{{Sender Name}} <{{email}}>"
subject: "{{subject}}"
tags: [email, action-required, {{topic-tags}}]
status: inbox
priority: {{high/medium/low}}
priority-score: {{numeric score}}
created: {{timestamp}}
source-email-id: "{{message-id}}"
thread-length: {{number of messages in thread}}
---

# {{Email subject — reformulated as a clear title}}

**From**: [[{{Sender Name}}]] ({{email}})
**Date**: {{date}}
**Original subject**: {{subject}}
**Thread**: {{X messages — latest development summary if thread}}

## Request

{{Clear synthesis of the request or action required, in 2-4 lines}}

## Context

{{Context information from the email, synthesized. If part of a thread, include relevant history.}}

## Actions To Do

- [ ] {{First required action}}
- [ ] {{Additional action if any}}

**Deadline**: {{if present, otherwise "to be defined"}}

---
*Imported from {{source}} on {{today}}*
```

## Email with Deadline or Important Date

```markdown
---
type: email-deadline
date: {{email date}}
from: "{{Sender Name}} <{{email}}>"
subject: "{{subject}}"
tags: [email, deadline, {{topic-tags}}]
status: inbox
deadline: {{deadline date in YYYY-MM-DD}}
priority: {{high/medium/low}}
created: {{timestamp}}
---

# Deadline: {{brief description of the deadline}}

**From**: {{Name}} — {{email}}
**Email date**: {{date}}
**Deadline**: {{formatted deadline date}}

## Details

{{Synthesis of email content focusing on the deadline}}

## Actions

- [ ] {{What to do before the deadline}}

---
*Imported from {{source}} on {{today}}*
```

## Informational Email

```markdown
---
type: email-info
date: {{email date}}
from: "{{Sender Name}} <{{email}}>"
subject: "{{subject}}"
tags: [email, info, {{topic-tags}}]
status: inbox
created: {{timestamp}}
---

# {{Descriptive title}}

**From**: {{Name}} — {{email}}
**Date**: {{date}}

## Summary

{{Key information extracted from the email, well organized}}

---
*Imported from {{source}} on {{today}}*
```

## Invoice / Receipt

```markdown
---
type: email-financial
date: {{email date}}
from: "{{Sender Name}} <{{email}}>"
subject: "{{subject}}"
tags: [email, finance, {{invoice/receipt}}, {{topic-tags}}]
status: inbox
amount: "{{amount with currency}}"
due-date: {{due date in YYYY-MM-DD if applicable}}
created: {{timestamp}}
---

# {{Invoice/Receipt}}: {{vendor/service}} — {{amount}}

**From**: {{Name}} — {{email}}
**Date**: {{date}}
**Amount**: {{amount with currency}}
**Due date**: {{if applicable}}
**Payment status**: {{paid/pending/overdue}}

## Details

{{What this invoice/receipt is for. Line items if available.}}

## Actions

- [ ] {{Pay by due date / File for records / Submit for reimbursement}}

---
*Imported from {{source}} on {{today}}*
```

## Travel Information

```markdown
---
type: email-travel
date: {{email date}}
from: "{{Sender Name}} <{{email}}>"
subject: "{{subject}}"
tags: [email, travel, {{topic-tags}}]
status: inbox
created: {{timestamp}}
---

# Travel: {{destination}} — {{travel date}}

**From**: {{Name}} — {{email}}
**Date**: {{date}}

## Itinerary

{{Flight/hotel/transit details}}

## Important Information

{{Confirmation numbers, addresses, contact info}}

## Actions

- [ ] {{Pre-travel prep items}}

---
*Imported from {{source}} on {{today}}*
```

## Meeting / Event Invitation

```markdown
---
type: email-meeting
date: {{email date}}
from: "{{Sender Name}} <{{email}}>"
subject: "{{subject}}"
tags: [email, meeting, {{topic-tags}}]
status: inbox
created: {{timestamp}}
event-date: {{event date in YYYY-MM-DD}}
---

# {{Meeting title}}

**Date/time**: {{when}}
**Location/link**: {{where}}
**Participants**: {{who}}

## Agenda

{{From email body}}

## Pre-Meeting Notes

{{Context from vault, related projects}}

## Post-Meeting Action Items

- [ ] {{To be filled in after meeting}}

---
*Imported from {{source}} on {{today}}*
```

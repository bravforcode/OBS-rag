# Postman — 9 Operating Modes

If context unclear, use AskUserQuestion to pick mode.

## Mode 1 — Email Triage

### Hey
1. `hey box imbox --json` — screened-in important
2. `hey box laterbox --json` — flagged for response (high priority)
3. `hey box bubblebox --json` — user wants reminders
4. `hey box trailbox --json` — receipts/transactional
5. Skip `feedbox` unless user asks
6. `hey threads <id> --json` for relevant items
7. Priority scoring (Imbox emails get +1 baseline). 5+=high, 3-4=med, 0-2=low
8. Note creation in `00-Inbox/`
9. Offer `hey seen <id>` for processed items
10. Final report includes Hey account name

### GWS (Gmail)
1. `gws gmail users messages list` with `q: "is:inbox is:unread"`. If >30, limit to 48h with `newer_than:2d`
2. `gws gmail users messages get` (full) or `gws gmail users threads get`
3. Offer `gws gmail users messages modify` to remove UNREAD

### Common
- Score per VIP(+3)/action(+3)/deadline(+2)/urgency(+2)/recent 24h(+1)
- Filter: save action/deadline/VIP/financial/travel/meeting; ignore newsletters/automated/trivial
- Note creation via templates (see `postman-templates.md`)
- Thread intelligence: follow full conversation, summarize latest state
- Final report sorted by priority

## Mode 2 — Calendar Import

Bring Google Calendar events into vault as notes in `06-meetings/<date>-<title>.md`.

## Mode 3 — Create Event on Google Calendar

From request or vault note. Use `gws calendar events insert`. Always show full event + confirm before executing.

## Mode 4 — Targeted Search

Search emails or events on specific topic. Use Gmail search syntax: `from:`, `subject:`, `after:`, `before:`, `has:`, `is:`.

## Mode 5 — VIP Filter

Process only emails from VIP contacts (defined in `Meta/user-profile.md`). Always save these even if low content.

## Mode 6 — Deadline Radar

Scan all emails + calendar for upcoming deadlines. Categorize:
- 🚨 Overdue
- ⏰ Critical (within 48h)
- 📅 Upcoming (within 7 days)
- 🗓 On the Horizon (7-30 days)

## Mode 7 — Meeting Prep

For upcoming meeting: gather context — meeting details, participants, related email threads, past meeting notes, related vault notes, suggested talking points. Save as note in `06-meetings/<date>-prep-<title>.md`.

## Mode 8 — Weekly Agenda

Comprehensive weekly overview. Combine calendar + emails + deadlines + todos. Output to `07-daily/weekly-<YYYY-WW>.md`.

## Mode 9 — Email Draft

Draft reply based on vault context. Use `gws gmail users drafts create` (never send without explicit confirmation). Reference vault notes for context, keep voice matching user style from past emails.

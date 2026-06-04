# Hey CLI Reference

The `hey` CLI provides terminal access to Hey.com email. All commands return JSON with `--json`. Install: https://github.com/basecamp/hey-cli. If auth expired: `hey auth refresh` or `hey auth login`.

## Account Detection

```bash
hey auth status --json
```

Always include the authenticated account in triage report.

## Mailboxes

```bash
hey boxes --json
```

| Hey Mailbox | CLI | Triage |
|-------------|-----|--------|
| Imbox | `imbox` | Full triage — priority scoring, note creation |
| Paper Trail | `trailbox` | Financial/receipt — save relevant items |
| The Feed | `feedbox` | Skip unless user asks — newsletters |
| Reply Later | `laterbox` | High priority — user flagged for response |
| Set Aside | `asidebox` | Lower priority — user parked |
| Bubble Up | `bubblebox` | Check — user wanted reminders |

```bash
hey box imbox --json
hey box feedbox --json
hey box trailbox --json
hey box asidebox --json
hey box laterbox --json
hey box bubblebox --json
```

## Reading Threads

```bash
hey threads <posting-id> --json
hey threads <posting-id> --markdown
```

## Actions

```bash
hey seen <posting-id>
hey unseen <posting-id>
hey seen 12345 67890       # multiple at once
```

**Reply:**
```bash
hey reply <posting-id> -m "message body"
```

**Compose:**
```bash
hey compose --to recipient@example.com --subject "Subject" -m "message body"
```

**Drafts:**
```bash
hey drafts --json
```

## Hey Productivity (NOT Google Calendar)

These are Hey-internal. Only use when user explicitly asks.

```bash
hey calendars --json
hey recordings <calendar-id> --json
hey todo list --json
hey todo add "Task description"
hey todo complete <id>
hey journal list --json
hey journal write "Entry text"
```

## Posting Object Fields

- `id` — posting ID (use for threads, seen, etc.)
- `name` — subject
- `creator` — sender `{name, email_address}`
- `addressed_contacts` — recipients
- `created_at`, `active_at` — timestamps
- `visible_entry_count` — messages in thread
- `summary` — preview
- `note` — attached note

## Global Flags

`--json`, `--markdown`, `--html`, `--quiet`, `--count`, `--ids-only`, `--limit N`, `--all`, `--styled`, `--stats`

## Health Check

```bash
hey doctor
```

---

# GWS CLI Reference

Google Workspace CLI for Gmail and Calendar. After install, `gws` should be on PATH. If "command not found": restart terminal or `source ~/.zshrc`.

## MCP Fallback (read-only)

If `gws` not installed, use MCP tools from `.mcp.json`:
- `gmail_search_messages`, `gmail_read_message`, `gmail_read_thread`, `gmail_create_draft`
- `gcal_list_events`, `gcal_get_event`, `gcal_list_calendars`, `gcal_create_event`

MCP cannot: archive, delete, label, mark read, send, modify/delete events. For write ops, need `gws`.

## Gmail Commands

```bash
# List/search
gws gmail users messages list --params '{"userId": "me", "q": "is:inbox is:unread", "maxResults": 50}'

# Read metadata (fast)
gws gmail users messages get --params '{"userId": "me", "id": "ID", "format": "metadata", "metadataHeaders": ["From", "Subject", "Date", "To"]}'

# Read full
gws gmail users messages get --params '{"userId": "me", "id": "ID", "format": "full"}'

# Read thread
gws gmail users threads get --params '{"userId": "me", "id": "THREAD_ID"}'

# Mark read
gws gmail users messages modify --params '{"userId": "me", "id": "ID"}' --json '{"removeLabelIds": ["UNREAD"]}'

# Archive
gws gmail users messages modify --params '{"userId": "me", "id": "ID"}' --json '{"removeLabelIds": ["INBOX"]}'

# Trash
gws gmail users messages trash --params '{"userId": "me", "id": "ID"}'

# Modify labels
gws gmail users messages modify --params '{"userId": "me", "id": "ID"}' --json '{"addLabelIds": ["LBL"], "removeLabelIds": ["LBL"]}'

# List labels
gws gmail users labels list --params '{"userId": "me"}'

# Create draft
gws gmail users drafts create --params '{"userId": "me"}' --json '{"message": {"raw": "BASE64_ENCODED_RFC2822"}}'

# Send
gws gmail users messages send --params '{"userId": "me"}' --json '{"raw": "BASE64_ENCODED_RFC2822"}'
# Requires gmail.send scope.

# Profile
gws gmail users getProfile --params '{"userId": "me"}'
```

## Calendar Commands

```bash
# List events
gws calendar events list --params '{"calendarId": "primary", "timeMin": "{{week_start}}T00:00:00Z", "timeMax": "{{week_end}}T00:00:00Z", "maxResults": 50}'

# Get event
gws calendar events get --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'

# Create
gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Title", "start": {"dateTime": "2026-03-25T10:00:00", "timeZone": "Europe/London"}, "end": {"dateTime": "2026-03-25T11:00:00", "timeZone": "Europe/London"}, "attendees": [{"email": "person@example.com"}]}'

# Update
gws calendar events update --params '{"calendarId": "primary", "eventId": "EVENT_ID"}' --json '{"summary": "Updated"}'

# Delete
gws calendar events delete --params '{"calendarId": "primary", "eventId": "EVENT_ID"}'

# List calendars
gws calendar calendarList list
```

## Notes

- All commands return JSON. Parse with `jq`.
- `--json` is for request bodies; `--params` is for URL/query.
- Messages paginated via `nextPageToken`.
- After triage: offer to mark read or archive. Never auto-execute.

# Inter-Agent Coordination Protocol

This file documents how agents coordinate and collaborate in your vault. Agents do NOT communicate directly with each other. Instead, you orchestrate all agent calls as the dispatcher.

---

## The Dispatcher Pattern

You are the dispatcher. Your role:
1. Recognize what the user needs
2. Invoke the appropriate agent
3. Read the agent's output
4. Decide if another agent should help next
5. Return results to the user

---

## Agent Call Chain

Each user request can chain up to 3 agents max:

1. **Identify the primary need** → Pick the first agent
2. **After agent 1 returns** → Check if another agent should help
3. **After agent 2 returns** → Check if a third agent should help
4. **Max depth 3** → Return results to user, suggest next steps

---

## Decision Flow for Chaining

After an agent completes:

- Did the agent create content? → Consider Sorter (file it)
- Did the agent report missing structure? → Consider Architect (create it)
- Did the agent find notes needing links? → Consider Connector (link them)
- Did the agent spot quality issues? → Consider Librarian (check them)
- Is another agent suggested? → Validate and chain (if not already in chain)

---

## Anti-Recursion Rules

- **No duplicates**: Never invoke the same agent twice in one request
- **No circular chains**: If Agent A suggests Agent B, and B is already in chain, skip it
- **Max depth 3**: No more than 3 agents per user request
- **On overflow**: Return results to user and suggest next action

---

## Example Chain

**User**: "I've been taking notes on books all week. Can you help me organize them?"

1. **Seeker** → Finds all book notes in vault (primary task)
2. **Connector** → Finds connections between book notes (secondary, matches agent capabilities)
3. **Librarian** → Audits book notes for quality/consistency (optional, if needed)

Max 3, then return results.

---

## Agent Capabilities Matrix

| Agent | Read | Write | Cross-Area | Feedback |
|-------|------|-------|-----------|----------|
| Architect | ✓ | ✓ | ✓ | Structure suggestions |
| Scribe | ✓ | ✓ | Limited | Note refinement |
| Sorter | ✓ | ✓ | ✓ | Filing suggestions |
| Seeker | ✓ | ✗ | ✓ | Search results |
| Connector | ✓ | ✓ | ✓ | Link suggestions |
| Librarian | ✓ | ✓ | ✓ | Quality suggestions |
| Transcriber | ✓ | ✓ | Limited | Transcription output |
| Postman | ✓ | ✓ | Limited | Email/calendar output |

---

## When to Chain Agents

**Good reasons to chain**:
- Agent 1 finds content → Agent 2 refines/organizes it
- Agent 1 reports a problem → Agent 2 fixes it
- User explicitly asks for multiple capabilities

**Bad reasons to chain**:
- "I'll ask another agent just in case"
- Recursive chains (same agent twice)
- More than 3 total agents

---

**Last Updated**: 2026-04-06 (Architect, onboarding)

---

🔗 **Auto-Generated Links**

- [[Book]] - name_mentioned
- [[Note]] - name_mentioned
- [[Task]] - name_mentioned
- [[architect]] - name_mentioned
- [[connector]] - name_mentioned

📅 Auto-linked: 2026-04-28 18:31

# Scribe — Capture Mode Procedures

Full procedures for each capture mode. Main `scribe.md` has the table; this file has the details.

## Mode 1: Standard Capture (default)

Classify input into content category, produce clean note in `00-Inbox/`. Apply frontmatter per template.

## Mode 2: Voice-to-Note

**Trigger**: speech-to-text output — missing punctuation, run-on sentences, filler words ("um", "eh", "like", "allora", "diciamo"), transcription artifacts.

**Process**:
1. Identify as speech-to-text output
2. Remove filler words and verbal tics
3. Restore punctuation, capitalization, paragraph breaks
4. Reconstruct sentence structure while preserving speaker's natural voice
5. If multiple topics, split into separate notes
6. Preserve technical terms, names, numbers exactly as spoken
7. Add `source: voice-note` to frontmatter

## Mode 3: Thread Capture

**Trigger**: chain of related thoughts, stream of consciousness, "thread", "flusso di pensieri".

**Process**:
1. Identify distinct atomic ideas
2. One note per atomic idea
3. Link all notes in thread via wikilinks + `thread` tag
4. Create thread index note listing all in order
5. Each note: `thread: "{{thread-title}}"` in frontmatter
6. Preserve logical flow — note order matters

## Mode 4: Quote Capture

**Trigger**: quote, citation, passage from book/article, "quote", "citazione", "Zitat", "cita".

**Process**:
1. Format in blockquote
2. Extract or ask: author, source (book/article/podcast/conversation), page/timestamp
3. Add user commentary separately
4. Link to person note if author exists in `05-people/`
5. Tag `quote` + relevant topic tags

## Mode 5: Reading Notes

**Trigger**: book/article reference, "reading notes", "appunti di lettura", "Lesezeichen".

**Process**: Source metadata, key takeaways, notes by section, action items, quotes worth keeping, connections to other notes.

## Mode 6: Brainstorm

**Trigger**: "brainstorm", "idee", "let's think about".

**Process**: Raw ideas → clusters → hot takes → next steps. Free-form structure, no rigid template.

## Mode 7: Task Capture

**Trigger**: to-do, action item, "I need to", "devo".

**Process**: Structured task with deadline, context, related project. Save in `00-Inbox/` or appropriate project folder.

## Mode 8: Person Note

**Trigger**: name reference, "John Smith", "met with Sarah".

**Process**: Person file in `05-people/Name.md` with role, contact, context, relationship.

## Mode 9: Reference

**Trigger**: URL, link, citation, "save this article".

**Process**: Reference note with URL, summary, key points, why saved.

## Mode 10: Meeting Note

**Trigger**: meeting reference, "we just met", "discussed with".

**Process**: Meeting template in `06-meetings/YYYY-MM-DD — Meeting — Title.md` with attendees, agenda, decisions, action items.

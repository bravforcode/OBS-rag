# Obsidian Performance Fix

## Problem
Vault has 7,500+ notes + 165MB of external skill repos.
Obsidian indexes ALL files, causing lag.

## Solution: Exclude Heavy Folders

### Automatic (already applied)
The `.obsidian/app.json` now excludes these folders from indexing:
- `brain/skills-universal/` (1,390 files)
- `brain/skills-universal-master/` (1,390 files)
- `brain/github-skills/`
- `brain/skills-archive/`
- `skills/` (165MB)
- `Backups/`
- `.git/`
- `.ai/scripts/`
- `.claude/`
- `.github/`

### Manual (if still slow)
1. Open Obsidian Settings → Files & Links
2. Add to "Excluded folders":
   - `brain/skills-universal`
   - `skills`
   - `Backups`
3. Disable Graph View when not needed (Ctrl+G to toggle)

### Files Still Accessible
These files are NOT deleted — they're just not indexed by Obsidian.
- Agents can still read them via file system
- CLI tools can still access them
- Manual file access works fine

### If You Need to Search Excluded Folders
Use the file system directly:
```bash
ls brain/skills-universal/
find skills/ -name "*.md"
```

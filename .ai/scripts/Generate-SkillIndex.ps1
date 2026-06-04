$ErrorActionPreference = "Stop"

$skillDirs = @(
    "C:\Users\menum\.agents\skills",
    "C:\Users\menum\.claude\skills",
    "C:\Users\menum\Documents\ObsidianVault\Second Brain\brain\skills-consolidated"
)

$outputFile = "C:\Users\menum\.ai\AVAILABLE_SKILLS.md"
$skills = @()

foreach ($dirPath in $skillDirs) {
    if (Test-Path $dirPath) {
        $subdirs = Get-ChildItem -Path $dirPath -Directory
        foreach ($dir in $subdirs) {
            $skillFile = Join-Path $dir.FullName "SKILL.md"
            if (Test-Path $skillFile) {
                try {
                    $content = Get-Content -Raw $skillFile
                    
                    $name = $null
                    $description = $null
                    
                    if ($content -match '(?s)^---\s*\n(.*?)\n---') {
                        $yaml = $Matches[1]
                        if ($yaml -match '(?m)^name:\s*(.*)') {
                            $name = $Matches[1].Trim(' "')
                        }
                        if ($yaml -match '(?m)^description:\s*(.*)') {
                            $description = $Matches[1].Trim(' "')
                        }
                    }
                    
                    if (!$name) { $name = $dir.Name }
                    if (!$description) { $description = "No description provided." }
                    
                    # Avoid duplicates
                    $existing = $skills | Where-Object { $_.Name -eq $name }
                    if (!$existing) {
                        $skills += [PSCustomObject]@{
                            Name        = $name
                            Description = $description
                            Path        = $skillFile
                        }
                    }
                } catch {
                    Write-Warning "Failed to parse $($skillFile): $_"
                }
            }
        }
    }
}

$markdown = @"
# Universal AI Skills Index (Superpowers)

This document lists ALL specialized skills available to AI agents (Claude, Gemini, Codex).
I have 100% full access to these skills.

## Protocol for AIs
1. **Discover:** Search this table for a skill relevant to the user's request.
2. **Load:** To execute a skill, you MUST read its detailed instructions from the provided path.
3. **Execute:** Strictly follow the SOP and tool schemas defined in the skill's `SKILL.md` file.

| Skill Name | Description | Absolute Path |
|------------|-------------|---------------|
"@

foreach ($skill in ($skills | Sort-Object Name)) {
    # Sanitize markdown table cells
    $desc = $skill.Description -replace "\|", "\|" -replace "`n", " "
    $markdown += "`n| $($skill.Name) | $desc | $($skill.Path) |"
}

[System.IO.File]::WriteAllText($outputFile, $markdown, (New-Object System.Text.UTF8Encoding($true)))

Write-Host "Generated skill index: $outputFile ($($skills.Count) skills)"

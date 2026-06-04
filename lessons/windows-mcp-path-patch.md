# Lesson Learned: Windows MCP Path Patching (2026-05-15)

**Related:** [[Intelligence/Strategic_Engineering_Report_2026|MCP Ecosystem]] | [[Dashboard]] | [[Knowledge/Index|Knowledge Hub]]

## Related
- [[system/ai/Index|System AI Index]]
- [[Meta/AI/Index|Meta AI Index]]

## Problem
MCP servers attempting to spawn shell scripts (.sh) on Windows via spawn('scripts/xyz.sh') fail because Windows doesn't natively handle shebangs or .sh execution without an explicit interpreter.

## Hardcore Solution
Patch the server.mjs (or equivalent entry point) to:
1. Detect process.platform === 'win32'.
2. Check for the existence of C:\Program Files\Git\bin\bash.exe.
3. Prepend interpreting command: spawn('bash', ['scripts/xyz.sh', ...args]).
4. Manually inject known tool paths (like ~/.local/bin for uv) into process.env.PATH because Windows shells often inherit a restricted environment in MCP contexts.

## Verification
- Run 	oken_reduce_measure or any tool that spawns a bash sub-process.
- Ensure isError: false and JSON output is returned.

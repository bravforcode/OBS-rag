---
type: playbook
status: active
topic: debugging
---

# Debugging Playbook

Systematic approach to finding and fixing bugs.

## Step 1: Reproduce
- Write a minimal reproduction case
- Document the exact steps
- Note the environment (OS, versions, config)

## Step 2: Isolate
- Narrow down the problem area
- Use binary search (comment out half the code)
- Check logs and error messages

## Step 3: Hypothesize
- Form a hypothesis about the root cause
- Predict what you expect to see
- Design a test for your hypothesis

## Step 4: Fix
- Implement the minimal fix
- Verify the fix resolves the issue
- Check for regressions

## Step 5: Prevent
- Write a test that catches this bug
- Document the lesson in `lessons/`
- Update relevant playbooks

## Common Patterns
- **Null reference**: Check for null before access
- **Race condition**: Add synchronization
- **Memory leak**: Profile and trace allocations
- **Config issue**: Verify environment variables

## Related
- [[knowledge/failure-analyses/index|Failure Analyses]]
- [[lessons/index|Lessons]]

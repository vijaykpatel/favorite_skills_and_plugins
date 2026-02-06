# PR Review Handler Examples

Complete examples of handling different PR review scenarios.

## Example 1: Simple Bot Review Fix

**Scenario:** Cursor Bugbot found an unused variable.

**Comment:**
```
File: src/lib/helper.ts
Line: 15
Comment by cursor[bot]:
Unused variable `tempResult` at line 15
```

**Actions:**
1. Checkout branch: `git checkout feature/new-api`
2. Read file: `src/lib/helper.ts`
3. Remove unused variable
4. Commit: `git commit -m "Remove unused variable per Cursor Bugbot feedback"`
5. Push: `git push origin feature/new-api`
6. Respond:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/123456/replies \
     -f body="Fixed in abc1234. Removed unused tempResult variable."
   ```

## Example 2: Critical Security Issue

**Scenario:** Devin AI found SQL injection vulnerability.

**Comment:**
```
File: src/api/users.ts
Line: 45
Comment by devin-ai-integration[bot]:
🔴 SQL injection vulnerability - user input not sanitized
```

**Actions:**
1. Checkout branch
2. Read file and understand the vulnerability
3. Implement parameterized query
4. Test the fix locally
5. Commit: `git commit -m "Fix: SQL injection vulnerability in user query per Devin AI"`
6. Push changes
7. Respond:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/789012/replies \
     -f body="Fixed in def5678. Switched to parameterized queries to prevent SQL injection. Tested with malicious input and confirmed safe."
   ```

## Example 3: Human Reviewer Asks Question

**Scenario:** Reviewer asks why you chose a specific approach.

**Comment:**
```
File: src/components/Form.tsx
Line: 67
Comment by alice:
Why use useCallback here instead of useMemo?
```

**Actions:**
1. Analyze the code
2. Respond with explanation:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/345678/replies \
     -f body="useCallback is needed here because this function is passed to child components as a prop. useCallback memoizes the function reference itself, preventing unnecessary re-renders. useMemo would memoize the return value, which isn't what we need in this case."
   ```

No code change needed, just clarification.

## Example 4: Multiple Related Comments

**Scenario:** Three reviewers all commented on error handling being insufficient.

**Comments:**
```
File: src/api/fetch.ts
Line: 23
Comment by alice: Missing error handling for network failures

File: src/api/fetch.ts
Line: 45
Comment by bob: What happens if the API returns 500?

File: src/api/fetch.ts
Line: 67
Comment by charlie: Should add retry logic for transient failures
```

**Actions:**
1. Checkout branch
2. Read file and assess all error handling gaps
3. Implement comprehensive error handling:
   - Add try-catch blocks
   - Handle specific HTTP error codes
   - Add retry logic with exponential backoff
4. Commit: `git commit -m "Add comprehensive error handling and retry logic per review feedback"`
5. Push changes
6. Respond to all three comments:
   ```bash
   # Alice's comment
   gh api -X POST repos/owner/repo/pulls/42/comments/111111/replies \
     -f body="Fixed in ghi9012. Added try-catch blocks for network failures with specific error messages."

   # Bob's comment
   gh api -X POST repos/owner/repo/pulls/42/comments/222222/replies \
     -f body="Fixed in ghi9012. Added handling for 500 errors with fallback behavior."

   # Charlie's comment
   gh api -X POST repos/owner/repo/pulls/42/comments/333333/replies \
     -f body="Fixed in ghi9012. Implemented retry logic with exponential backoff for transient failures."
   ```

## Example 5: Disagreement with Reviewer

**Scenario:** Reviewer suggests refactoring that would break existing API contract.

**Comment:**
```
File: src/api/users.ts
Line: 12
Comment by bob:
This function should return a Promise instead of using callbacks
```

**Actions:**
1. Assess the suggestion
2. Determine it would break backward compatibility
3. Respond with reasoning:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/444444/replies \
     -f body="This function is part of our public API used by external consumers. Changing to Promise would be a breaking change. I can add a parallel Promise-based version (getUserAsync) in a follow-up PR if that would help. Thoughts?"
   ```

Wait for response before proceeding. No code change yet.

## Example 6: Out-of-Scope Refactoring Request

**Scenario:** Reviewer suggests large refactoring during bug fix PR.

**Comment:**
```
File: src/utils/validation.ts
Line: 89
Comment by alice:
While you're here, this whole validation module should be refactored to use Zod instead of custom validators
```

**Actions:**
1. Acknowledge the suggestion
2. Propose separate PR:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/555555/replies \
     -f body="Agreed that moving to Zod would be cleaner. I'll create a separate issue for that refactoring to keep this PR focused on the urgent bug fix. Does that work?"
   ```

No code change in this PR.

## Example 7: Mixed Bot and Human Feedback

**Scenario:** Cursor Bugbot found duplicated code, human reviewer found logic bug.

**Comments:**
```
Comment 1 by cursor[bot]:
Duplicated code at lines 45-67 should be extracted to helper function

Comment 2 by alice:
Line 78: off-by-one error in loop condition
```

**Actions:**
1. Checkout branch
2. Fix critical bug first (off-by-one error)
3. Extract duplicated code second
4. Commit both: `git commit -m "Fix off-by-one error and extract duplicated code per review feedback"`
5. Push changes
6. Respond to both:
   ```bash
   # Bot comment
   gh api -X POST repos/owner/repo/pulls/42/comments/666666/replies \
     -f body="Fixed in jkl3456. Extracted duplicated logic to calculateTotal helper function."

   # Alice's comment
   gh api -X POST repos/owner/repo/pulls/42/comments/777777/replies \
     -f body="Fixed in jkl3456. Changed loop condition from i <= items.length to i < items.length. Good catch!"
   ```

## Example 8: Need Clarification Before Fixing

**Scenario:** Bot suggests fix but it's unclear if it applies to this case.

**Comment:**
```
File: src/components/List.tsx
Line: 34
Comment by cursor[bot]:
Use React.memo to prevent unnecessary re-renders
```

**Actions:**
1. Analyze the component
2. Determine if memoization is beneficial here
3. If unclear, ask reviewer:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/888888/replies \
     -f body="This component only renders when its parent data changes, and the parent already memoizes the data. Would React.memo provide additional benefit here, or is this a false positive?"
   ```

Wait for response before implementing.

## Example 9: Test Failure After Fix

**Scenario:** Implemented fix but tests fail.

**Actions:**
1. Implement fix based on comment
2. Run tests: `npm test`
3. Tests fail
4. Debug and fix tests
5. Commit fix + test updates: `git commit -m "Fix validation logic and update tests per review feedback"`
6. Push changes
7. Respond:
   ```bash
   gh api -X POST repos/owner/repo/pulls/42/comments/999999/replies \
     -f body="Fixed in mno7890. Updated validation logic as suggested and adjusted tests to match new behavior. All tests passing now."
   ```

## Example 10: Batch Response After Multiple Commits

**Scenario:** Made several commits addressing different review comments.

**Actions:**
1. Fix issue A → commit abc1234
2. Fix issue B → commit def5678
3. Fix issue C → commit ghi9012
4. Push all commits
5. Respond to all comments in batch:
   ```bash
   # Comment 1
   gh api -X POST repos/owner/repo/pulls/42/comments/111111/replies \
     -f body="Fixed in abc1234."

   # Comment 2
   gh api -X POST repos/owner/repo/pulls/42/comments/222222/replies \
     -f body="Fixed in def5678."

   # Comment 3
   gh api -X POST repos/owner/repo/pulls/42/comments/333333/replies \
     -f body="Fixed in ghi9012."
   ```

All responses sent after pushing, referencing specific commits.

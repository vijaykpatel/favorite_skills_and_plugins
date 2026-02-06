# PR Review Handler

Systematically handle pull request review feedback through automated workflows.

## Overview

The PR Review Handler skill provides a structured approach to managing PR reviews by automating comment fetching, implementing fixes with proper commits, responding to reviewers appropriately, and pushing updates.

## Key Features

- **Automated Comment Fetching**: Uses `gh` CLI to fetch PR reviews and line-specific comments
- **Priority Categorization**: Organizes feedback by critical, high, medium, and low priority
- **Actionability Analysis**: Identifies actionable items, questions, discussions, and informational comments
- **Bot Review Support**: Specialized handling for Devin AI and Cursor Bugbot feedback
- **Response Templates**: Pre-built templates for common response scenarios
- **Workflow Automation**: Complete flow from fetch to push with verification

## When to Use

Use this skill when:
- Working on an existing open PR with review feedback
- Addressing automated bot reviews (Devin AI, Cursor Bugbot)
- Responding to human reviewer feedback
- Coordinating multiple reviewers with potentially conflicting feedback
- Need systematic tracking of which comments have been addressed

## Workflow

### 1. Fetch PR Information
```bash
gh pr view <number> --json reviews
gh api repos/<owner>/<repo>/pulls/<number>/comments
```

### 2. Analyze Feedback
Categorize each comment by:
- **Priority**: Critical → High → Medium → Low
- **Actionability**: Actionable, Question, Discussion, Informational
- **Source**: Bot vs Human reviewer

### 3. Plan Changes
- Group related comments
- Identify dependencies between fixes
- Separate code changes from discussion items

### 4. Implement Fixes
- Checkout PR branch
- Implement changes in priority order
- Create atomic commits per fix or related fix group
- Run tests/build to verify

### 5. Respond to Comments
```bash
gh api -X POST repos/<owner>/<repo>/pulls/<number>/comments/<comment-id>/replies \
  -f body="Fixed in <sha>. <explanation>"
```

### 6. Push and Verify
- Push all commits to PR branch
- Check CI status
- Summarize work completed

## Response Templates

**Fixed**:
```
Fixed in abc1234. <One sentence explaining what changed>
```

**Won't fix with reason**:
```
Keeping as-is because <reasoning>. <Alternative if applicable>
```

**Clarification**:
```
<Answer to question>. <Additional context if helpful>
```

**Scope discussion**:
```
Good point. I'll address this in a follow-up PR to keep this change focused on <original scope>.
```

## Common Patterns

### Pattern 1: Bot Review Fixes
1. Fetch all bot comments
2. Assess validity of each suggestion
3. Implement valid fixes (group related ones)
4. Respond with commit references
5. Push once after addressing all bot feedback

### Pattern 2: Mixed Human + Bot
1. Address critical human feedback first
2. Handle bot feedback second
3. Respond to questions/discussions
4. Push changes with all responses

### Pattern 3: Conflicting Feedback
1. Acknowledge both perspectives
2. Make reasoned decision
3. Explain to both reviewers
4. Offer synchronous discussion if needed

## Examples

Complete examples covering different scenarios are available in the skill's `references/examples.md` file:
- Simple bot review fixes
- Critical security issues
- Human reviewer questions
- Multiple related comments
- Disagreements with reviewers
- Out-of-scope refactoring requests
- Mixed bot and human feedback
- Clarification needs before fixing
- Test failures after implementing fixes
- Batch responses after multiple commits

## Installation

```bash
npx skills add vijaykpatel/favorite_skills_and_plugins@pr-review-handler
```

Or symlink manually:
```bash
ln -s /path/to/favorite_skills_and_plugins/skills/pr-review-handler ~/.claude/skills/pr-review-handler
```

## Files

- `SKILL.md` - Main workflow and instructions
- `references/examples.md` - 10 complete scenario examples

## Best Practices

- Always fetch and read all comments before starting
- Commit atomically (each commit = coherent change set)
- Respond to every comment (even if just "Fixed in <sha>")
- Be professional: thank reviewers, explain decisions, admit mistakes
- Verify builds/tests pass before pushing
- Update PR description if changes significantly alter scope
- Re-request review after addressing feedback

## Requirements

- `gh` CLI installed and authenticated
- Git configured with proper permissions
- Access to the repository and PR

## License

MIT

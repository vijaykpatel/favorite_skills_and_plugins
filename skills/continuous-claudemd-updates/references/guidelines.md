# CLAUDE.md Content Guidelines

## Core Principle

CLAUDE.md serves as a concise orientation guide for AI agents working on the codebase. It should contain **only essential procedural knowledge** that helps agents understand how to work effectively in this specific codebase.

## When to Include in CLAUDE.md

Include information that:
- Explains non-obvious conventions or patterns
- Describes essential workflows (deployment, testing, development)
- Documents critical constraints or requirements
- Clarifies the project's structure and organization
- Provides context that would prevent common mistakes

## When to Move to docs/

Move content to docs/ when:
- Information exceeds 3-4 paragraphs
- Content includes extensive code examples (>20 lines)
- Details are reference material rather than procedural
- Information is domain-specific deep-dive
- Content will rarely be needed but should be available

## Content Quality Standards

### Be Concise
- Use bullet points over paragraphs
- Prefer examples over explanations
- Remove redundant information
- Assume AI agents are competent

### Be Current
- Remove outdated information immediately after changes
- Update references when files are renamed/moved
- Verify configuration references match actual state
- Delete obsolete workflows or patterns

### Be Specific
- Link to actual file paths when referencing code
- Use concrete examples rather than abstract descriptions
- Include exact command syntax for important operations
- Reference specific line numbers for critical patterns

## Linking to docs/

When creating docs/ notes, follow this pattern:

```markdown
## Component Architecture

Components follow a compound pattern with composition. For detailed examples and advanced patterns, see [docs/component-patterns.md](docs/component-patterns.md).

Key principles:
- Single responsibility per component
- Composition over prop drilling
- TypeScript strict mode required
```

The CLAUDE.md entry should:
1. Provide the essential principle (1-2 sentences)
2. Link to detailed docs/
3. Include minimal example if helpful

## Section Organization

Organize CLAUDE.md with clear headers:

```markdown
# Project Name

Brief 1-2 sentence description

## Development Workflow
## Architecture
## Testing
## Deployment
## Key Conventions
## Common Pitfalls
```

Avoid:
- Long introductions
- Historical context
- Personal notes
- Duplicate information

## Examples

### ✅ Good CLAUDE.md Entry

```markdown
## CSS Conventions

- **No inline CSS** - Use Tailwind classes or CSS modules
- **CSS variables for tokens** - Check globals.css before creating new variables
- See [docs/css-architecture.md](docs/css-architecture.md) for variable naming
```

Concise, actionable, links to details.

### ❌ Bad CLAUDE.md Entry

```markdown
## CSS Conventions

This project uses CSS in a specific way that we've found works really well for our team. We've adopted a pattern where we avoid using inline styles because it makes the code harder to maintain and violates our separation of concerns. Instead, we use Tailwind CSS classes which provide utility-first styling...

[continues for several paragraphs]

Here's an example of how to use CSS variables:
[50 lines of code examples]
```

Too verbose, should be split with details in docs/.

## Maintenance Workflow

After each commit:
1. Review what changed in the codebase
2. Identify if CLAUDE.md needs updates
3. Check for outdated references
4. If adding >3 paragraphs, create docs/ note instead
5. Remove information that is no longer true
6. Commit CLAUDE.md updates with descriptive message

## Red Flags

Watch for these issues:
- CLAUDE.md over 200 lines (likely too verbose)
- Sections with >5 paragraphs (split to docs/)
- Code blocks over 30 lines (move to docs/)
- Historical information ("previously we...", "we used to...")
- Information duplicated from README or other docs
- References to deleted/renamed files
- Outdated configuration mentions

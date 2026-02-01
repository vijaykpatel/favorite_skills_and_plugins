# CLAUDE.md Examples: Good vs Bad

## Example 1: Configuration Changes

### ❌ Bad (Too Verbose)

```markdown
## Build Configuration

Our build process has evolved over time. We started with webpack but migrated to Vite for better performance and developer experience. The configuration is complex because we need to support multiple entry points and optimize for production.

Here's our complete vite.config.ts:

```typescript
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
// ... 40 more lines of config
```

When you need to modify the build:
1. First, understand what you're trying to change
2. Read the Vite documentation
3. Make your changes carefully
4. Test in development first
5. Then test in production build
```

### ✅ Good (Concise + Link)

```markdown
## Build Configuration

Using Vite with React. Key settings in `vite.config.ts`:
- Multi-entry for main app + admin panel
- Custom alias: `@/` maps to `src/`

For configuration details: [docs/build-setup.md](docs/build-setup.md)
```

---

## Example 2: Component Patterns

### ❌ Bad (Over-explained)

```markdown
## Component Structure

We use a specific component structure that follows React best practices and our team conventions. Each component should be in its own directory with the following files:

- ComponentName.tsx - The main component file
- ComponentName.module.css - Styles for the component
- ComponentName.test.tsx - Unit tests
- index.ts - Re-exports the component for cleaner imports

This structure helps us maintain consistency across the codebase and makes it easier to find related files. When creating a new component, always follow this pattern. For example, if you're creating a Button component, you would create:

```
components/
  Button/
    Button.tsx
    Button.module.css
    Button.test.tsx
    index.ts
```

The Button.tsx file should export a default function...
[continues with more explanation]
```

### ✅ Good (Example-driven)

```markdown
## Component Structure

Components follow this structure:
```
components/
  ComponentName/
    ComponentName.tsx       # Main component
    ComponentName.module.css  # Styles
    ComponentName.test.tsx  # Tests
    index.ts                # Re-export
```

See existing components in `src/components/` for patterns.
```

---

## Example 3: API Conventions

### ❌ Bad (Duplicate Information)

```markdown
## API Integration

All API calls go through our centralized API client located in `src/lib/api.ts`. This client handles authentication, error handling, retry logic, and response transformation. We use this pattern to ensure consistency across the application.

The API client exports these methods:
- get(url, options)
- post(url, data, options)
- put(url, data, options)
- delete(url, options)

Each method returns a Promise that resolves with the response data or rejects with an error object.

Authentication is handled automatically by the client. It reads the token from localStorage and includes it in the Authorization header. If the token is expired, the client will attempt to refresh it before making the request.

Error handling is centralized. All errors are transformed into a consistent format with:
- status: HTTP status code
- message: User-friendly error message
- code: Application-specific error code

[continues with more details about error types, retry logic, etc.]
```

### ✅ Good (Reference Implementation)

```markdown
## API Integration

All API calls use `src/lib/api.ts` client:

```typescript
import { api } from '@/lib/api'

const users = await api.get('/users')
const created = await api.post('/users', { name: 'John' })
```

Client handles auth, errors, and retries. See [docs/api-client.md](docs/api-client.md) for error handling patterns.
```

---

## Example 4: Testing Requirements

### ❌ Bad (Unnecessary Context)

```markdown
## Testing Philosophy

We believe strongly in testing. Tests help us catch bugs early, document expected behavior, and enable confident refactoring. Our testing approach has evolved as the team has grown and the codebase has matured.

We use Jest as our test runner because it provides a great developer experience with features like snapshot testing, mocking, and code coverage. We also use React Testing Library for component tests because it encourages testing from the user's perspective rather than implementation details.

When writing tests, you should:
- Test behavior, not implementation
- Use meaningful test descriptions
- Keep tests focused and isolated
- Mock external dependencies
- Aim for high coverage but don't obsess over 100%

Here's an example of a good test:

```typescript
describe('LoginForm', () => {
  it('should submit credentials when form is valid', async () => {
    // ... 30 lines of test code
  })
})
```
```

### ✅ Good (Requirements Only)

```markdown
## Testing

Requirements:
- Tests required for all new features
- Run `npm test` before committing
- Min 80% coverage for new code

Use Jest + React Testing Library. See [docs/testing-patterns.md](docs/testing-patterns.md) for examples.
```

---

## Example 5: Handling Major Changes

### Scenario: Authentication system was refactored from custom JWT to NextAuth.js

### ❌ Bad (Historical Context)

```markdown
## Authentication

Previously, we used a custom JWT authentication system with tokens stored in localStorage. However, we migrated to NextAuth.js for better security and OAuth support. The old system can still be found in git history if you need to reference it.

Current authentication uses NextAuth.js...
```

### ✅ Good (Current State Only)

```markdown
## Authentication

Using NextAuth.js with session-based auth:
- Config: `pages/api/auth/[...nextauth].ts`
- Session access: `useSession()` hook
- Providers: Google, GitHub, Email

See [docs/auth-setup.md](docs/auth-setup.md) for provider configuration.
```

---

## Example 6: When to Create docs/ Notes

### Trigger: Adding database schema information (50+ lines)

### ❌ Bad (Everything in CLAUDE.md)

```markdown
## Database Schema

We use PostgreSQL with Prisma ORM. Here's the complete schema:

```prisma
// ... 100 lines of schema
```

And here are the relationships between tables:
[Detailed explanations of each table, relationships, indexes, etc.]
```

### ✅ Good (Summary + Link)

```markdown
## Database

PostgreSQL with Prisma ORM. Schema in `prisma/schema.prisma`.

Key tables: users, posts, comments. See [docs/database-schema.md](docs/database-schema.md) for relationships and indexes.

Migrations: `npm run db:migrate`
```

### docs/database-schema.md

```markdown
# Database Schema Reference

## Overview
Complete schema documentation with relationships, indexes, and query patterns.

## Tables

### users
[Detailed table documentation]

### posts
[Detailed table documentation]

...
```

---

## Key Takeaways

1. **CLAUDE.md = Quick Reference**: Essential info only
2. **docs/ = Deep Dives**: Detailed documentation
3. **Remove Historical Context**: Only current state matters
4. **Show, Don't Tell**: Examples over explanations
5. **Link Generously**: Point to details rather than including everything
6. **Update Ruthlessly**: Delete outdated info immediately

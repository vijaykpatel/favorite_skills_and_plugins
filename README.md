# Favorite Skills and Plugins

A curated collection of agent skills and plugins for enhancing Claude Code and other AI agents.

## Structure

```
favorite_skills_and_plugins/
├── skills/          # Claude Code skills and agent capabilities
├── plugins/         # MCP servers and plugin integrations
├── examples/        # Example configurations and usage patterns
├── docs/           # Detailed documentation for created skills
└── .github/        # GitHub Actions and repository automation
```

## Created Skills

Custom skills built specifically for this repository.

### continuous-claudemd-updates

Automatically maintains CLAUDE.md documentation in sync with codebase changes through commit analysis and periodic audits.

**Key features**: Automatic git commit analysis, conciseness enforcement, staleness detection, audit capabilities, auto-commit functionality.

**[Read full documentation →](docs/continuous-claudemd-updates.md)**

## Imported Skills

Curated skills from the community and leading developers.

| Skill Name | Source |
|------------|--------|
| Find Skills | [skills.sh](https://skills.sh/vercel-labs/skills/find-skills) |
| Web Design Guidelines | [skills.sh](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines) |
| Frontend Design | [skills.sh](https://skills.sh/anthropics/skills/frontend-design) |
| Agent Browser | [skills.sh](https://skills.sh/vercel-labs/agent-browser/agent-browser) |
| Skill Creator | [skills.sh](https://skills.sh/anthropics/skills/skill-creator) |
| React Composition Patterns | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-composition-patterns) |
| Vercel React Best Practices | [skills.sh](https://skills.sh/vercel-labs/agent-skills/vercel-react-best-practices) |
| Next Best Practices | [skills.sh](https://skills.sh/vercel-labs/next-skills/next-best-practices) |
| AI SDK | [skills.sh](https://skills.sh/vercel/ai/ai-sdk) |
| SEO Audit | [skills.sh](https://coreyhaines31/marketingskills/seo-audit) |
| Technical & SEO Website Audit | [skills.sh](https://skills.sh/squirrelscan/skills/audit-website) |
| Programmatic SEO | [skills.sh](https://skills.sh/coreyhaines31/marketingskills/programmatic-seo) |
| Performance Optimization | [skills.sh](https://skills.sh/addyosmani/web-quality-skills/performance) |
| Core Web Vitals | [skills.sh](https://skills.sh/addyosmani/web-quality-skills/core-web-vitals) |
| PDF Parsing | [skills.sh](https://skills.sh/anthropics/skills/pdf) |
| Webapp Testing | [skills.sh](https://skills.sh/anthropics/skills/webapp-testing) |
| MCP Builder | [skills.sh](https://skills.sh/anthropics/skills/mcp-builder) |
| Theme Factory | [skills.sh](https://skills.sh/anthropics/skills/theme-factory) |
| Algorithmic Art | [skills.sh](https://skills.sh/anthropics/skills/algorithmic-art) |
| Using Git Worktrees | [skills.sh](https://skills.sh/obra/superpowers/using-git-worktrees) |
| UI-UX Pro Max | [skills.sh](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) |
| Ralph (PRD to Tasks) | [skills.sh](https://skills.sh/snarktank/ralph/ralph) |
| Ryan Carson PRD Generator | [skills.sh](https://skills.sh/snarktank/ralph/prd) |

## Plugins & Toolsets

Complete plugin packages and comprehensive toolsets from the community.

### Collections

- **[Obra's Superpowers](https://github.com/obra/superpowers)** - Jesse Vincent's curated collection of essential agent skills
- **[Superpowers Lab](https://github.com/obra/superpowers-lab)** - Experimental and advanced agent skills
- **[Anthropic Skills](https://github.com/anthropics/skills/tree/main/skills)** - Official skills from Anthropic
- **[Vercel Skills](https://github.com/vercel-labs/agent-skills/tree/main/skills)** - Frontend and Next.js focused skills
- **[Ryan Carson's Skills](https://github.com/snarktank/amp-skills/tree/main)** - Practical agent skills collection

### Complete Plugins

- **[Every Compound Engineering](https://github.com/EveryInc/compound-engineering-plugin/tree/main)** - Comprehensive plugin with subagents and workflow automation
- **[Ryan Carson Ralph Plugin](https://github.com/snarktank/ralph)** - Convert PRDs into actionable tasks
- **[Compound Product Scripts](https://github.com/snarktank/compound-product/tree/main)** - Product development workflow automation

## Installation

All skills in this repository are **symlinked** to `~/.claude/skills/` for easy management and updates.

To install a skill:
```bash
ln -s /path/to/favorite_skills_and_plugins/skills/skill-name ~/.claude/skills/skill-name
```

**Benefit**: Updates to skills in this repository are immediately reflected in Claude Code without file copying.

## Skills vs Plugins

Understanding when to use skills versus plugins (MCP servers) is key to building effective AI workflows.

### Core Differences

| Aspect | Skills | Plugins (MCP Servers) |
|--------|--------|----------------------|
| **Layer** | Prompt/Knowledge Layer | Connectivity/Tooling Layer |
| **Purpose** | Teach Claude *how* to do something | Give Claude *access* to external systems |
| **Best For** | Workflows, procedures, domain expertise | Database access, API integrations, tool connectivity |
| **Format** | Markdown files with instructions | Executable programs with protocol interface |

### When to Use Skills

Use **Skills** when you need to:
- ✅ Define repeatable workflows and procedures
- ✅ Provide domain-specific expertise (SEO best practices, design guidelines)
- ✅ Teach Claude specialized knowledge (coding patterns, composition techniques)
- ✅ Create automated, context-driven behaviors

**Example**: React best practices, SEO audit workflows, git procedures

### When to Use Plugins (MCP Servers)

Use **Plugins** when you need to:
- ✅ Connect to external databases (PostgreSQL, SQLite)
- ✅ Integrate with third-party APIs (GitHub, Slack, Calendar)
- ✅ Access file systems and cloud storage
- ✅ Provide real-time data from external sources

**Example**: GitHub integration, database queries, file system operations

### Using Together

**Skills and plugins are complementary** - they work best together:

```
MCP Server: GitHub (provides access to repos, PRs, issues)
    +
Skill: Code Review Best Practices (teaches how to review code)
    =
Automated, expert code reviews with direct GitHub integration
```

> **Key Principle**: If you're explaining how to use a tool → Skill. If you need Claude to access databases/APIs → MCP.

## Official Documentation

### Claude Code
- [Skills Documentation](https://code.claude.com/docs/en/skills)
- [MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Agent Skills Overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [Complete Guide to Building Skills](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

### Cursor AI
- [Agent Skills Documentation](https://cursor.com/docs/context/skills)
- [Agent Best Practices](https://cursor.com/blog/agent-best-practices)
- [Cursor Docs](https://cursor.com/docs)

### Community Resources
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [Awesome Agent Skills](https://github.com/VoltAgent/awesome-agent-skills)
- [Model Context Protocol](https://modelcontextprotocol.io/)

## Contributing

Add your own skills:
1. Create a new directory in `skills/`
2. For created skills, add detailed documentation in `docs/`
3. Update this README with a brief description
4. Commit and push changes

## License

MIT License - See LICENSE file for details.

# Favorite Skills and Plugins

A curated collection of agent skills and plugins for enhancing Claude Code and other AI agents.

## Structure

```
favorite_skills_and_plugins/
├── skills/          # Claude Code skills and agent capabilities
├── plugins/         # MCP servers and plugin integrations
├── examples/        # Example configurations and usage patterns
├── docs/           # Documentation and guides
└── .github/        # GitHub Actions and repository automation
```

## Skills

The `skills/` directory contains reusable agent skills that extend Claude Code's capabilities. Each skill is typically defined in a `SKILL.md` file with instructions, triggers, and workflows.

### What are Skills?

Skills are modular, reusable "task packs" that teach Claude a repeatable workflow. They are folders containing:

- **SKILL.md** - The entrypoint with YAML frontmatter and instructions
- **Templates** - Optional example files and resources
- **Scripts** - Optional executable scripts for automation
- **Domain Knowledge** - Specialized instructions for specific tasks

**Key Features:**

1. **Progressive Loading** - Claude loads skills dynamically when relevant, not upfront
2. **Context Efficiency** - Skills are loaded in stages as needed, reducing context usage
3. **Automatic Invocation** - Claude can invoke skills automatically based on context, or you can call them directly with `/skill-name`
4. **Cross-Platform** - Skills follow the Agent Skills open standard, working across Claude Code, Cursor, and other AI tools

**Types of Skills:**

- **Anthropic Skills** - Created and maintained by Anthropic (e.g., document creation for Excel, Word, PowerPoint, PDF)
- **Community Skills** - Created by the community for specialized workflows
- **Custom Skills** - Your own organization-specific skills for domain tasks

### Available Skills

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

### Installation

All skills in this repository are **symlinked** to `~/.claude/skills/` for easy management and updates.

To install a skill:
1. Navigate to the skill's source directory
2. Create a symlink: `ln -s /path/to/favorite_skills_and_plugins/skills/skill-name ~/.claude/skills/skill-name`
3. Restart Claude Code or reload skills
4. Invoke with the appropriate trigger phrase or slash command

**Benefit of symlinks**: Any updates you make to skills in this repository are immediately reflected in Claude Code without needing to copy files.

## Plugins

The `plugins/` directory will contain MCP (Model Context Protocol) servers that extend Claude Code's capabilities by providing structured access to external systems and data sources.

### What are MCP Servers?

MCP servers are programs that expose specific capabilities to AI applications through the standardized Model Context Protocol. They act as universal adapters enabling Claude Code to interact with tools, databases, APIs, and services.

**MCP servers provide three main building blocks:**

1. **Tools** - Enable Claude to perform actions (e.g., file operations, API calls, database queries)
2. **Resources** - Expose data from files, APIs, databases, or other sources for context
3. **Prompts** - Provide reusable, parameterized templates for domain-specific tasks

**Common examples include:**
- File system servers for document access
- Database servers (PostgreSQL, SQLite) for data queries
- GitHub servers for repository, PR, and issue management
- Slack servers for team communication
- Calendar servers for scheduling

### Available Plugins

| Plugin Name | Source |
|-------------|--------|
| *No plugins yet* | - |

### Installation

MCP servers can be configured in `~/.claude/config.json` or installed as part of Claude Code plugins. They can run locally alongside Claude Code or remotely on separate servers.

For more information, see:
- [Claude Code MCP Documentation](https://code.claude.com/docs/en/mcp)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Awesome Claude Code Plugins](https://github.com/ccplugins/awesome-claude-code-plugins)

## Skills vs Plugins: When to Use Each

Understanding when to use skills versus plugins (MCP servers) is key to building effective AI workflows.

### Core Differences

| Aspect | Skills | Plugins (MCP Servers) |
|--------|--------|----------------------|
| **Layer** | Prompt/Knowledge Layer | Connectivity/Tooling Layer |
| **Purpose** | Teach Claude *how* to do something | Give Claude *access* to external systems |
| **Best For** | Workflows, procedures, domain expertise | Database access, API integrations, tool connectivity |
| **Loading** | Dynamic, context-driven | Always available when configured |
| **Format** | Markdown files with instructions | Executable programs with protocol interface |

### When to Use Skills

Use **Skills** when you need to:

- ✅ Define repeatable workflows and procedures
- ✅ Provide domain-specific expertise (e.g., SEO best practices, design guidelines)
- ✅ Teach Claude specialized knowledge (e.g., coding patterns, composition techniques)
- ✅ Create automated, context-driven behaviors
- ✅ Package instructions that should activate without manual invocation

**Example Use Cases:**
- React best practices and composition patterns
- SEO audit workflows
- Frontend design guidelines
- Git workflow procedures

### When to Use Plugins (MCP Servers)

Use **Plugins/MCP Servers** when you need to:

- ✅ Connect to external databases (PostgreSQL, SQLite)
- ✅ Integrate with third-party APIs (GitHub, Slack, Calendar)
- ✅ Access file systems and cloud storage
- ✅ Provide real-time data from external sources
- ✅ Execute operations on external systems

**Example Use Cases:**
- GitHub repository, PR, and issue management
- Database queries and operations
- File system operations
- Slack messaging and team communication

### Using Skills and Plugins Together

**Skills and plugins are complementary** - they work best when used together:

**The Power Combo:**
1. **MCP provides the connectivity** - Secure access to your databases, APIs, and external tools
2. **Skills provide the knowledge** - Instructions on how to use those tools effectively

**Real-World Example:**

```
MCP Server: GitHub MCP (provides access to repos, PRs, issues)
    +
Skill: Code Review Best Practices (teaches Claude how to review code)
    =
Automated, expert code reviews with direct GitHub integration
```

**Another Example:**

```
MCP Server: PostgreSQL MCP (provides database access)
    +
Skill: Data Migration Workflow (teaches safe migration procedures)
    =
Automated database migrations with safety checks and rollback plans
```

### Key Principle

> **If you're explaining how to use a tool or follow procedures → Skill**
>
> **If you need Claude to access databases/APIs in the first place → MCP**

Use both together for maximum effectiveness: MCP for connectivity, Skills for procedural knowledge.

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

## Getting Started

1. Clone this repository:
   ```bash
   git clone <repo-url> favorite_skills_and_plugins
   cd favorite_skills_and_plugins
   ```

2. Browse available skills and plugins
3. Follow individual installation instructions
4. Customize for your workflow

## Contributing

Add your own skills and plugins:
1. Create a new directory in `skills/` or `plugins/`
2. Include a README.md with usage instructions
3. Document dependencies and configuration
4. Commit and push changes

## License

MIT License - See LICENSE file for details

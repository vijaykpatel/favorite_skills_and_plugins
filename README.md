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

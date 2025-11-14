# Claude Configuration for PatternFly

This directory contains Claude Code configurations for the PatternFly repository.

## 📁 Directory Structure

```
.claude/
├── README.md                      # This file
├── QUICK-REFERENCE.md             # Quick reference card
├── COMMANDS-README.md             # Slash commands documentation
├── HOW-TO-USE-A11Y-AGENT.md      # Agent usage guide
├── commands/
│   └── a11y-docs.md              # Accessibility docs command
└── agents/
    └── a11y-docs.md              # Accessibility docs agent
```

## 🎯 Quick Start

### Generate Accessibility Documentation

**Fastest way - Use the slash command:**
```bash
/a11y-docs ComponentName
```

**Or ask Claude conversationally:**
```
"Generate accessibility documentation for Dropdown"
```

**Or use the Python script:**
```bash
python3 scripts/generate_a11y_docs.py ComponentName
```

## 📚 Available Commands

### `/a11y-docs` - Accessibility Documentation Generator

Generate comprehensive accessibility documentation for PatternFly components.

**Usage:**
- `/a11y-docs ComponentName` - Generate full documentation
- `/a11y-docs --list` - List components missing docs
- `/a11y-docs --analyze ComponentName` - Analyze requirements only
- `/a11y-docs help` - Show usage help

**See:** `.claude/COMMANDS-README.md` for full documentation

## 🤖 Available Agents

### a11y-docs - Accessibility Documentation Agent

An AI-powered agent that generates comprehensive accessibility documentation by analyzing existing patterns and creating consistent, high-quality guidelines.

**Invoke by:**
- Using the `/a11y-docs` slash command (recommended)
- Asking Claude conversationally about accessibility documentation
- Running the Python scripts in `scripts/`

**See:** `.claude/agents/a11y-docs.md` for full agent documentation

## 📖 Documentation

| File | Description | Best For |
|------|-------------|----------|
| `QUICK-REFERENCE.md` | One-page quick reference | Quick lookup |
| `COMMANDS-README.md` | Command documentation | Learning commands |
| `HOW-TO-USE-A11Y-AGENT.md` | Agent usage guide | Using the agent |
| `../scripts/QUICKSTART-A11Y-GENERATOR.md` | Script quick start | Command-line usage |
| `../scripts/README-A11Y-GENERATOR.md` | Complete documentation | Deep dive |
| `../A11Y-DOCS-GENERATOR-SUMMARY.md` | System overview | Understanding the system |

## 🚀 Getting Started

### 1. Start with the Quick Reference
```bash
cat .claude/QUICK-REFERENCE.md
```

### 2. Try a Command
```bash
/a11y-docs --list
```

### 3. Generate Your First Doc
```bash
/a11y-docs ComponentName
```

### 4. Review the Output
```
packages/documentation-site/patternfly-docs/content/accessibility/{component-name}/{component-name}.md
```

## 💡 Tips

1. **Use slash commands** for the fastest results
2. **Ask conversationally** when you need discussion or iteration
3. **Use Python scripts** for automation and batch processing
4. **Always review** generated content for accuracy
5. **Test with assistive tech** before submitting

## 🆘 Getting Help

**For command help:**
```bash
/a11y-docs help
```

**For agent help:**
```
"How do I use the accessibility documentation agent?"
```

**For script help:**
```bash
python3 scripts/generate_a11y_docs.py --help
```

## 🔗 Related Files

### Scripts Directory
- `../scripts/generate_a11y_docs.py` - Main Python script
- `../scripts/demo_a11y_generator.py` - Demo script
- `../scripts/generate-a11y-docs.js` - JavaScript version

### Documentation
- `../A11Y-DOCS-GENERATOR-SUMMARY.md` - Complete system summary

## 🎓 Learn More

**About Accessibility Documentation:**
- See existing docs in `packages/documentation-site/patternfly-docs/content/accessibility/`
- Review examples like `button/`, `modal/`, `accordion/`

**About ARIA Patterns:**
- [W3C ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)

**About WCAG:**
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)

**About PatternFly Accessibility:**
- [PatternFly Accessibility](https://www.patternfly.org/accessibility/about-accessibility)

## ✨ Features

The accessibility documentation system provides:

- ✅ AI-powered content generation
- ✅ Pattern recognition from existing docs
- ✅ WCAG 2.1 Level AA compliance
- ✅ W3C ARIA APG pattern mapping
- ✅ Interactive testing checklists
- ✅ React and HTML/CSS documentation
- ✅ Multiple usage modes (command/agent/script)
- ✅ Batch processing capabilities
- ✅ Demo mode for testing

## 📊 Current Status

- **Existing Docs:** 40 components have accessibility documentation
- **Total Components:** ~52 components in PatternFly
- **Missing Docs:** Run `/a11y-docs --list` to see current gaps

## 🤝 Contributing

When using the generated documentation:

1. **Review thoroughly** - AI generates good content but needs human review
2. **Test completely** - Use keyboard, screen readers, and other AT
3. **Verify accuracy** - Check props/attributes match the component
4. **Enhance as needed** - Add component-specific details
5. **Submit for review** - Get peer review from accessibility experts

## 🎉 Quick Wins

Try these commands right now:

```bash
# See what needs documentation
/a11y-docs --list

# Run the demo
python3 scripts/demo_a11y_generator.py

# Read the quick reference
cat .claude/QUICK-REFERENCE.md
```

---

**Ready to generate accessibility documentation?** Start with `/a11y-docs --list` to see what's needed!

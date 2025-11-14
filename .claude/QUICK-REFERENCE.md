# A11y Documentation Generator - Quick Reference Card

## 🚀 Three Ways to Generate Documentation

### 1️⃣ Slash Command (Fastest - Use This!)

```bash
# Generate docs for a component
/a11y-docs Dropdown

# List missing documentation
/a11y-docs --list

# Analyze without generating
/a11y-docs --analyze Select

# Get help
/a11y-docs help
```

**When to use:** Quick generation, immediate results, interactive in Claude Code

---

### 2️⃣ Conversational (Most Flexible)

```
Just ask Claude:
"Generate accessibility documentation for Dropdown"
"Which components need a11y docs?"
"Review the Button accessibility documentation"
"What keyboard navigation should Dropdown have?"
```

**When to use:** Need discussion, want to iterate, have questions

---

### 3️⃣ Python Scripts (For Automation)

```bash
# One-time setup
pip install anthropic
export ANTHROPIC_API_KEY='your-key'

# Generate
python3 scripts/generate_a11y_docs.py Dropdown

# List missing
python3 scripts/generate_a11y_docs.py --list-missing

# Demo (no API key needed)
python3 scripts/demo_a11y_generator.py
```

**When to use:** Batch processing, CI/CD integration, automation

---

## 📋 Common Tasks

### Generate Documentation
```bash
/a11y-docs Dropdown
```
Creates: `packages/.../accessibility/dropdown/dropdown.md`

### Find What's Missing
```bash
/a11y-docs --list
```
Shows: Components without accessibility docs

### Understand Requirements
```bash
/a11y-docs --analyze Dropdown
```
Shows: What accessibility features are needed (doesn't generate file)

### Review Existing Docs
```
"Review the Modal accessibility documentation and suggest improvements"
```

---

## 📝 What Gets Generated

Every accessibility doc includes:

```markdown
---
id: ComponentName
section: components
---

## Accessibility
- 3-5 implementation guidelines

## Testing
- 5-7 interactive checkboxes

## React customization
- Props table

## HTML/CSS customization
- Attributes table

## Additional considerations
- Edge cases (if needed)

## Further reading
- W3C ARIA links
```

---

## ✅ Quality Checklist

Before submitting generated docs:

- [ ] Read through entire document
- [ ] Test keyboard navigation (Tab, arrows, Enter, Escape)
- [ ] Test with screen reader (NVDA, JAWS, or VoiceOver)
- [ ] Verify all props/attributes exist in component
- [ ] Check ARIA pattern link works
- [ ] Confirm PatternFly v6 classes (.pf-v6-c-*)
- [ ] Review with accessibility expert

---

## 🎯 Examples

### Example 1: Quick Generation
```bash
/a11y-docs Select
```
Result: Full accessibility doc in 30 seconds

### Example 2: Batch Generate
```bash
for component in Dropdown Select Toolbar; do
  /a11y-docs $component
done
```

### Example 3: With Context
```
"Generate accessibility docs for Dropdown. Note that it supports
multi-select and grouped items."
```

---

## 🆘 Troubleshooting

| Problem | Solution |
|---------|----------|
| Command not found | Check `.claude/commands/a11y-docs.md` exists |
| Generic content | Provide more component context |
| Wrong props | Review component source, update manually |
| API error | Check `ANTHROPIC_API_KEY` is set |

---

## 📚 Documentation

| File | Purpose |
|------|---------|
| `.claude/QUICK-REFERENCE.md` | This card |
| `.claude/COMMANDS-README.md` | Command details |
| `.claude/HOW-TO-USE-A11Y-AGENT.md` | Agent guide |
| `scripts/QUICKSTART-A11Y-GENERATOR.md` | Script quick start |
| `scripts/README-A11Y-GENERATOR.md` | Full documentation |
| `A11Y-DOCS-GENERATOR-SUMMARY.md` | Complete overview |

---

## 🔗 Resources

- [W3C ARIA APG](https://www.w3.org/WAI/ARIA/apg/) - ARIA patterns
- [WCAG 2.1](https://www.w3.org/WAI/WCAG21/quickref/) - Guidelines
- [PatternFly A11y](https://www.patternfly.org/accessibility/about-accessibility) - PF docs

---

## 💡 Pro Tips

1. **Use the slash command** - It's the fastest way
2. **Always test with real AT** - Screen readers catch issues docs miss
3. **Review existing examples** - Check similar components first
4. **Iterate freely** - Ask for refinements
5. **Start with high-priority** - Interactive components first

---

## 🎬 Getting Started (30 seconds)

1. Try the demo:
   ```bash
   python3 scripts/demo_a11y_generator.py
   ```

2. List what's missing:
   ```bash
   /a11y-docs --list
   ```

3. Generate your first doc:
   ```bash
   /a11y-docs [ComponentName]
   ```

4. Review and test!

---

**Need help?** Ask Claude or check the documentation files listed above.

**Ready to go?** Run `/a11y-docs --list` to see what needs documentation!

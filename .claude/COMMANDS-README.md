# Claude Commands for PatternFly

## Accessibility Documentation Command

### `/a11y-docs` - Generate Accessibility Documentation

Generate comprehensive accessibility documentation for PatternFly components.

#### Usage

**Generate documentation for a component:**
```
/a11y-docs Dropdown
/a11y-docs Select
/a11y-docs Button
```

**List components missing documentation:**
```
/a11y-docs --list
/a11y-docs list
/a11y-docs missing
```

**Analyze a component's accessibility requirements:**
```
/a11y-docs --analyze Dropdown
/a11y-docs analyze Select
```

**Get help:**
```
/a11y-docs
/a11y-docs help
```

#### What It Does

When you run `/a11y-docs ComponentName`, it will:

1. ✓ Read existing accessibility documentation examples
2. ✓ Find the component's documentation (if available)
3. ✓ Identify the appropriate ARIA pattern
4. ✓ Generate comprehensive accessibility guidelines
5. ✓ Create testing criteria with checkboxes
6. ✓ Document React props and HTML attributes
7. ✓ Add additional considerations if needed
8. ✓ Link to W3C ARIA APG patterns
9. ✓ Save to the correct location

#### Output Location

Generated files are saved to:
```
packages/documentation-site/patternfly-docs/content/accessibility/{component-name}/{component-name}.md
```

#### Generated Sections

Each document includes:

- **Frontmatter** - Component ID and section
- **Imports** - Required PatternFly React components
- **Accessibility** - Implementation guidelines (3-5 items)
- **Testing** - Manual testing criteria with checkboxes (5-7 items)
- **React customization** - Props table with accessibility properties
- **HTML/CSS customization** - Attributes and PatternFly classes table
- **Additional considerations** - Edge cases and special notes (optional)
- **Further reading** - Links to W3C ARIA APG patterns

#### Examples

##### Example 1: Generate Dropdown Documentation

```bash
/a11y-docs Dropdown
```

**Output:**
```
Generating accessibility documentation for Dropdown...

✓ Read 4 example accessibility docs
✓ Found component documentation
✓ Identified ARIA Menu pattern
✓ Generated 5 accessibility guidelines
✓ Created 7 testing criteria
✓ Documented 4 React props
✓ Listed 6 HTML/CSS attributes
✓ Added focus management considerations

File saved to:
packages/documentation-site/patternfly-docs/content/accessibility/dropdown/dropdown.md

Next steps:
1. Review the generated documentation
2. Test with screen readers (NVDA, JAWS, VoiceOver)
3. Verify props and attributes exist in component
4. Submit for peer review
```

##### Example 2: List Missing Documentation

```bash
/a11y-docs --list
```

**Output:**
```
Analyzing accessibility documentation coverage...

✓ Found 40 existing accessibility docs
✓ Found 52 total components

Components missing accessibility documentation (12):

High Priority:
  - Dropdown - Interactive menu component
  - Select - Form selection component
  - Table - Data display component

Medium Priority:
  - Drawer - Side panel component
  - Toolbar - Action bar component
  - DataList - List display component
  - Popover - Contextual overlay

Low Priority:
  - EmptyState - Placeholder component
  - Gallery - Image grid component
  - InputGroup - Composite input component
  - FormSelect - Native select wrapper
  - List - Basic list component

Recommendation: Start with high-priority interactive components.
```

##### Example 3: Analyze Component

```bash
/a11y-docs --analyze Dropdown
```

**Output:**
```
Analyzing accessibility requirements for Dropdown component...

Component Type: Interactive Menu
ARIA Pattern: Menu / Listbox
Complexity: High

Key Accessibility Requirements:

1. Keyboard Navigation:
   - Tab/Shift+Tab: Navigate to/from dropdown
   - Enter/Space: Open dropdown
   - ↓/↑: Navigate menu items
   - Home/End: First/last item
   - Escape: Close dropdown
   - Type-ahead: Jump to items by typing

2. ARIA Attributes:
   - role="menu" or role="listbox" on menu
   - role="menuitem" on items
   - aria-expanded on trigger
   - aria-haspopup on trigger
   - aria-activedescendant for focus management

3. Focus Management:
   - Focus trap when open
   - Return focus to trigger on close
   - Visual focus indicators required
   - Manage focus on arrow key navigation

4. Screen Reader Support:
   - Announce menu open/close state
   - Announce selected items
   - Announce item count if helpful
   - Describe menu purpose with label

5. Special Considerations:
   - Multi-select variant needs different pattern
   - Grouped items need proper structure
   - Disabled items should be announced
   - Loading state needs announcement

Recommended W3C Pattern:
https://www.w3.org/WAI/ARIA/apg/patterns/menu/

Ready to generate full documentation? Run:
/a11y-docs Dropdown
```

#### Tips for Best Results

1. **Use Exact Component Names**: Match the component name exactly as it appears in PatternFly
   - Good: `Dropdown`, `Select`, `Button`
   - Bad: `dropdown`, `select button`, `Btn`

2. **Review Generated Content**: Always review for accuracy
   - Verify props exist in the component
   - Check ARIA pattern links work
   - Test keyboard navigation matches
   - Validate with screen readers

3. **Provide Context for Complex Components**: Mention variants or special features
   - `/a11y-docs Dropdown (note: includes multi-select variant)`
   - `/a11y-docs Select (grouped options support)`

4. **Iterate as Needed**: Refine the generated documentation
   - Ask for more detail on specific sections
   - Request additional testing criteria
   - Add edge case considerations

#### Integration with Scripts

This command complements the standalone scripts:

**Use `/a11y-docs` when:**
- You want interactive generation in Claude Code
- You need to discuss and refine requirements
- You want immediate feedback and iteration

**Use Python scripts when:**
- You need batch processing
- You want CI/CD integration
- You prefer command-line automation

```bash
# Python script equivalent
python3 scripts/generate_a11y_docs.py Dropdown
python3 scripts/generate_a11y_docs.py --list-missing
```

#### Quality Standards

All generated documentation follows:

- ✅ WCAG 2.1 Level AA compliance
- ✅ W3C ARIA Authoring Practices Guide patterns
- ✅ PatternFly v6 naming conventions
- ✅ Consistent format with existing docs
- ✅ Actionable testing criteria
- ✅ Accurate prop and attribute documentation

#### Troubleshooting

**Issue**: Command not found
**Solution**: Ensure you're in the PatternFly repo and `.claude/commands/a11y-docs.md` exists

**Issue**: Generic content generated
**Solution**: Provide more context about the component's specific features

**Issue**: Props don't match component
**Solution**: Review component source and update the generated documentation

**Issue**: ARIA pattern link incorrect
**Solution**: Check W3C ARIA APG for the correct pattern name and update

#### Related Documentation

- `.claude/agents/a11y-docs.md` - Agent documentation
- `.claude/HOW-TO-USE-A11Y-AGENT.md` - Agent usage guide
- `scripts/README-A11Y-GENERATOR.md` - Script documentation
- `A11Y-DOCS-GENERATOR-SUMMARY.md` - Complete system overview

#### Quick Reference

| Command | Purpose |
|---------|---------|
| `/a11y-docs ComponentName` | Generate full documentation |
| `/a11y-docs --list` | List missing documentation |
| `/a11y-docs --analyze ComponentName` | Analyze requirements only |
| `/a11y-docs help` | Show usage instructions |

---

**Ready to generate accessibility documentation!** Run `/a11y-docs ComponentName` to get started.

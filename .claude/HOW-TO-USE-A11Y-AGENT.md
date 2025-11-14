# How to Use the Accessibility Documentation Agent

## Quick Start

The a11y-docs agent is now available in your Claude Code environment. Simply invoke it by name in your conversations.

## Invoking the Agent

### Method 1: Direct Request
```
User: "Generate accessibility documentation for the Dropdown component"
```

Claude will automatically invoke the a11y-docs agent if appropriate.

### Method 2: Agent-Specific Invocation
If you have multiple agents, you can specifically request the a11y-docs agent:
```
User: "Use the a11y-docs agent to create documentation for Select"
```

## Common Use Cases

### 1. Generate New Documentation
```
Generate accessibility documentation for Dropdown
Create a11y docs for the Select component
I need accessibility documentation for the Toolbar component
```

### 2. Find Missing Documentation
```
Which components are missing accessibility documentation?
List all components that need a11y docs
Show me components without accessibility documentation
```

### 3. Analyze Components
```
Analyze the accessibility requirements for the Dropdown component
What accessibility features should the Modal have?
Review the accessibility needs for the Table component
```

### 4. Update Existing Documentation
```
Update the Button accessibility documentation
Review and enhance the Modal a11y docs
Improve the Accordion accessibility documentation
```

### 5. Get Help with Specific Aspects
```
What keyboard navigation should the Dropdown support?
What ARIA attributes does the Select component need?
How should focus be managed in a Modal?
```

## What the Agent Does

When you invoke the agent, it will:

1. ✓ Read existing accessibility documentation examples
2. ✓ Analyze the component you specify
3. ✓ Find relevant component documentation
4. ✓ Generate comprehensive accessibility guidelines
5. ✓ Create testing criteria with checkboxes
6. ✓ Document React props and HTML attributes
7. ✓ Add additional considerations if needed
8. ✓ Link to appropriate W3C ARIA patterns
9. ✓ Save the file to the correct location

## Output Location

Generated files are saved to:
```
packages/documentation-site/patternfly-docs/content/accessibility/{component-name}/{component-name}.md
```

For example:
- Dropdown → `accessibility/dropdown/dropdown.md`
- Select → `accessibility/select/select.md`
- Toolbar → `accessibility/toolbar/toolbar.md`

## What Gets Generated

Each accessibility documentation file includes:

### Frontmatter
```yaml
---
id: ComponentName
section: components
---
```

### Imports
```javascript
import { Checkbox, List, ListItem } from '@patternfly/react-core';
```

### Accessibility Section
High-level guidelines (3-5 items) for implementing the component accessibly:
- Keyboard navigation requirements
- Screen reader support
- Focus management
- ARIA attributes
- Component-specific best practices

### Testing Section
Interactive checkboxes (5-7 items) for manual accessibility testing:
- Keyboard navigation tests
- ARIA attribute verification
- Focus management tests
- Screen reader tests
- User experience tests

### React Customization Section
Table of accessibility-related React props:
- `aria-label`, `aria-labelledby`, `aria-describedby`
- Component-specific props
- When each prop is required vs optional

### HTML/CSS Customization Section
Table of HTML attributes and PatternFly classes:
- ARIA attributes
- Role attributes
- PatternFly v6 classes (.pf-v6-c-*)
- Semantic HTML requirements

### Additional Considerations (Optional)
Special cases and edge cases:
- Focus trap management
- Custom implementations
- Performance considerations

### Further Reading
Links to W3C ARIA APG patterns and related resources

## Example Interaction

```
You: Generate accessibility documentation for Dropdown

Agent: I'll generate comprehensive accessibility documentation for the Dropdown component.

[Agent analyzes existing documentation]
[Agent reads about-modal, button, accordion examples]
[Agent searches for Dropdown component docs]
[Agent generates content following the established pattern]

Generated documentation includes:
✓ 5 accessibility implementation guidelines
✓ 7 testing criteria with checkboxes
✓ 4 React props for accessibility
✓ 6 HTML/CSS attributes
✓ Focus management considerations
✓ Link to ARIA Menu pattern

File saved to: packages/documentation-site/patternfly-docs/content/accessibility/dropdown/dropdown.md

Please review the documentation and test with screen readers (NVDA, JAWS, VoiceOver).
```

## Tips for Best Results

1. **Be Specific**: Provide the exact component name
   - Good: "Generate docs for Dropdown"
   - Better: "Generate accessibility docs for the Dropdown component"

2. **Provide Context**: If the component has unique features, mention them
   - "Generate docs for Dropdown, which supports multi-select"

3. **Review Output**: Always review and test the generated documentation
   - Verify ARIA patterns are correct
   - Test with actual screen readers
   - Ensure props and attributes exist in the component

4. **Iterate**: Ask for refinements if needed
   - "Add more detail about keyboard navigation"
   - "Include testing for error states"

5. **Reference Examples**: Mention similar components
   - "Generate docs for Select, similar to Dropdown"

## Agent Capabilities

The agent understands:
- ✓ PatternFly component architecture
- ✓ WCAG 2.1 Level AA guidelines
- ✓ W3C ARIA Authoring Practices Guide patterns
- ✓ PatternFly v6 class naming conventions
- ✓ React component prop patterns
- ✓ Common accessibility testing approaches
- ✓ Screen reader behavior
- ✓ Keyboard navigation standards

## Quality Assurance

After the agent generates documentation:

1. **Read Through**: Review for accuracy and completeness
2. **Check Links**: Verify W3C ARIA APG links work
3. **Test Keyboard**: Follow the keyboard testing criteria
4. **Test Screen Reader**: Verify with NVDA, JAWS, or VoiceOver
5. **Verify Props**: Ensure all mentioned props exist in the component
6. **Check Classes**: Confirm PatternFly classes are correct
7. **Refine**: Ask the agent to enhance any sections that need work

## Integration with Scripts

The agent complements the Python/JavaScript scripts:

### Use the Agent When:
- You want interactive, conversational generation
- You need to analyze and discuss requirements
- You want to iterate and refine documentation
- You need help understanding accessibility patterns

### Use the Scripts When:
- You want batch processing of multiple components
- You need command-line automation
- You want to integrate with CI/CD
- You prefer a non-interactive workflow

### Commands for Scripts:
```bash
# Python (with Claude API)
python3 scripts/generate_a11y_docs.py Dropdown

# List missing docs
python3 scripts/generate_a11y_docs.py --list-missing

# Demo (no API needed)
python3 scripts/demo_a11y_generator.py
```

## Common Questions

**Q: Will the agent overwrite existing documentation?**
A: The agent will check if documentation exists and warn you before overwriting.

**Q: How accurate is the generated content?**
A: The agent generates high-quality content based on patterns and standards, but always review for component-specific accuracy.

**Q: Can I customize the output format?**
A: Yes, you can ask the agent to adjust sections, add more detail, or change the format.

**Q: What if my component doesn't have documentation?**
A: The agent can still generate documentation based on the component name and common patterns. Provide additional context for better results.

**Q: Can it update existing docs?**
A: Yes, ask the agent to "update" or "enhance" existing documentation with specific requirements.

## Troubleshooting

**Issue**: Agent generates generic content
**Solution**: Provide more context about the component's unique features and functionality

**Issue**: ARIA pattern link is incorrect
**Solution**: Review and correct the link, or ask the agent to use a different pattern

**Issue**: Props don't match the actual component
**Solution**: Review the component implementation and ask the agent to update specific props

**Issue**: Testing criteria are too vague
**Solution**: Ask the agent to make testing criteria more specific and actionable

## Support

For more information:
- See `.claude/agents/a11y-docs.md` for full agent documentation
- See `scripts/README-A11Y-GENERATOR.md` for script documentation
- See `scripts/QUICKSTART-A11Y-GENERATOR.md` for quick reference
- Review existing docs in `packages/documentation-site/patternfly-docs/content/accessibility/`

## Examples to Try

Get started with these examples:

```
# List what needs documentation
"Which components are missing accessibility documentation?"

# Generate for a specific component
"Generate accessibility documentation for Dropdown"

# Analyze requirements
"What accessibility features does the Select component need?"

# Update existing docs
"Review the Button accessibility docs and suggest improvements"

# Get help with specific aspects
"What keyboard navigation pattern should a menu component use?"
```

---

**The a11y-docs agent is ready to help!** Just start a conversation with your accessibility documentation needs.

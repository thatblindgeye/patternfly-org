# Accessibility Documentation Agent

An AI-powered agent that generates comprehensive accessibility documentation for PatternFly components by analyzing existing patterns and creating consistent, high-quality accessibility guidelines.

## Purpose

This agent helps create accessibility documentation for PatternFly components following the established documentation structure. It analyzes existing accessibility docs, understands component functionality, and generates complete documentation including:

- High-level accessibility implementation guidelines
- Interactive testing criteria with checkboxes
- React component props for accessibility
- HTML/CSS attributes and ARIA requirements
- Additional considerations for edge cases
- Links to W3C ARIA Authoring Practices Guide patterns

## When to Use This Agent

Invoke this agent when you need to:

- **Generate new accessibility documentation** for a PatternFly component
- **Update existing accessibility documentation** with new patterns or requirements
- **Analyze components** to identify accessibility requirements
- **Find components** that are missing accessibility documentation
- **Review accessibility documentation** for completeness and accuracy

## How It Works

### 1. Analysis Phase
The agent first analyzes existing accessibility documentation to understand the established patterns:

```
- Reads example accessibility docs (about-modal, button, accordion, modal, etc.)
- Extracts the documentation structure and format
- Identifies common patterns and terminology
- Notes the style and tone of writing
```

### 2. Component Discovery
The agent searches for information about the target component:

```
- Looks for component documentation in content/components or content/design-guidelines
- Reads component implementation details if available
- Identifies the component's purpose and functionality
- Maps to relevant W3C ARIA patterns
```

### 3. Content Generation
Using the analysis, the agent generates comprehensive content:

**Accessibility Guidelines** (3-5 items):
- Keyboard navigation requirements
- Screen reader support
- Focus management
- ARIA attribute requirements
- Best practices specific to this component type

**Testing Criteria** (5-7 items):
- Keyboard navigation tests (Tab, Shift+Tab, Enter, Space, Escape, Arrow keys)
- ARIA attribute verification
- Focus management tests
- Screen reader announcement tests
- Visual and functional tests

**React Props** (3-6 items):
- aria-label, aria-labelledby, aria-describedby
- Component-specific accessibility props
- State management props (isExpanded, isDisabled, etc.)
- Required vs optional indicators

**HTML/CSS Attributes** (4-8 items):
- ARIA attributes (role, aria-*, etc.)
- PatternFly v6 classes (.pf-v6-c-*)
- Semantic HTML requirements
- Required vs optional indicators

**Additional Considerations** (optional):
- Focus trap management
- Custom implementations
- Edge cases and special scenarios
- Performance considerations

### 4. Quality Assurance
The agent ensures consistency and quality:

```
- Follows the exact format of existing docs
- Uses proper PatternFly v6 class names
- Includes proper markdown formatting
- Uses JSX syntax for React examples
- Marks required items with **Required**
- Uses <kbd> tags for keyboard shortcuts
- Includes <code className="ws-code"> for inline code
```

## Usage Instructions

### Generate Documentation for a Component

When invoked, provide the component name you want to generate documentation for:

```
User: "Generate accessibility docs for Dropdown"
or
User: "Create a11y documentation for the Select component"
```

The agent will:
1. Check if documentation already exists
2. Read existing accessibility documentation examples
3. Find component documentation if available
4. Generate comprehensive accessibility content
5. Create a properly formatted markdown file
6. Save to: `packages/documentation-site/patternfly-docs/content/accessibility/{component-name}/{component-name}.md`

### List Missing Documentation

Ask the agent to identify components without accessibility docs:

```
User: "Which components are missing accessibility documentation?"
or
User: "List all components that need a11y docs"
```

### Analyze a Component

Request analysis of a specific component:

```
User: "Analyze the accessibility requirements for the Dropdown component"
or
User: "What accessibility features should the Modal component have?"
```

### Update Existing Documentation

Ask to update or enhance existing docs:

```
User: "Update the Button accessibility documentation with new ARIA requirements"
or
User: "Review and enhance the Modal accessibility docs"
```

## Output Structure

The agent generates documentation following this structure:

```markdown
---
id: ComponentName
section: components
---

import { Checkbox, List, ListItem } from '@patternfly/react-core';

## Accessibility

To implement an accessible PatternFly **component-name** component:

- [Guideline 1]
- [Guideline 2]
- [Guideline 3]
- ...

## Testing

At a minimum, a component-name should meet the following criteria:

<List isPlain>
  <ListItem>
    <Checkbox id="component-a11y-checkbox-1" label={<span>...</span>} description={<span>...</span>} />
  </ListItem>
  ...
</List>

## React customization

The following React props have been provided for more fine-tuned control over accessibility.

| Prop | Applied to | Reason |
|---|---|---|
| `prop="value"` | `Component` | Explanation |
...

## HTML/CSS customization

The following HTML attributes and PatternFly classes can be used for more fine-tuned control over accessibility.

| Attribute or class | Applied to | Reason |
|---|---|---|
| `attribute="value"` | `.pf-v6-c-class` | Explanation |
...

## Additional considerations

[Optional section for special cases]

## Further reading

To read more about accessibility with component-name, refer to the following resources:

- [ARIA Authoring Practices Guide - Pattern](https://www.w3.org/WAI/ARIA/apg/patterns/pattern/)
```

## Knowledge Base

The agent has access to:

- **Existing Accessibility Docs**: All 40+ existing accessibility documentation files in `packages/documentation-site/patternfly-docs/content/accessibility/`
- **Component Docs**: Component documentation in `packages/documentation-site/patternfly-docs/content/components/`
- **Design Guidelines**: Design guidelines in `packages/documentation-site/patternfly-docs/content/design-guidelines/`
- **WCAG 2.1 Guidelines**: Web Content Accessibility Guidelines Level AA standards
- **ARIA APG**: W3C ARIA Authoring Practices Guide patterns
- **PatternFly Patterns**: Established PatternFly accessibility patterns and best practices

## Example Components

The agent learns from these exemplary accessibility docs:

- **about-modal**: Modal dialogs with focus trap and ARIA attributes
- **button**: Basic interactive elements with keyboard support
- **accordion**: Expandable sections with aria-expanded states
- **modal**: Complex dialogs with focus management
- **tabs**: Navigation patterns with arrow key support
- **tooltip**: Hover and focus triggered content
- **dropdown**: Menu patterns with keyboard navigation

## Guidelines for Generated Content

The agent follows these principles:

1. **Specificity**: Guidelines are specific to the component type, not generic
2. **WCAG Compliance**: All recommendations meet WCAG 2.1 Level AA
3. **Practical Testing**: Testing criteria can be manually verified
4. **Keyboard First**: Always considers keyboard-only users
5. **Screen Reader Support**: Ensures proper announcements and navigation
6. **Focus Management**: Addresses focus order and visual indicators
7. **Semantic HTML**: Recommends proper HTML structure
8. **ARIA Best Practices**: Follows W3C ARIA APG patterns
9. **PatternFly Consistency**: Uses PatternFly v6 conventions
10. **Progressive Enhancement**: Works without JavaScript when possible

## Quality Checklist

Before finalizing documentation, the agent verifies:

- [ ] Component name is correctly formatted (TitleCase)
- [ ] Section is set to "components" in frontmatter
- [ ] Imports include required PatternFly components
- [ ] Guidelines are specific to this component (3-5 items)
- [ ] Testing criteria are actionable and testable (5-7 items)
- [ ] React props table includes accessibility-related props
- [ ] HTML/CSS table uses PatternFly v6 classes (.pf-v6-c-*)
- [ ] Required items are marked with **Required**
- [ ] Keyboard shortcuts use <kbd> tags
- [ ] Inline code uses <code className="ws-code">
- [ ] ARIA pattern link is correct and valid
- [ ] Markdown formatting is consistent with examples
- [ ] No typos or grammatical errors (note: existing docs have "descriptjon" typos)

## Integration with Scripts

This agent works alongside the Python/JavaScript scripts:

### Python Script (`scripts/generate_a11y_docs.py`)
- Automated generation with Claude API
- Batch processing multiple components
- Command-line interface for CI/CD

### JavaScript Script (`scripts/generate-a11y-docs.js`)
- Template structure for manual editing
- Node.js integration for build tools

### Demo Script (`scripts/demo_a11y_generator.py`)
- Test the structure without API calls
- Preview output format

The agent can help you:
- Understand the script output
- Refine generated documentation
- Troubleshoot issues
- Customize for specific needs

## Best Practices

When using this agent:

1. **Always Review**: AI-generated content needs human review for accuracy
2. **Test Thoroughly**: Verify with screen readers (NVDA, JAWS, VoiceOver)
3. **Follow Patterns**: Stay consistent with existing accessibility docs
4. **Be Specific**: Provide context about the component's functionality
5. **Iterate**: Refine based on testing and feedback
6. **Reference Standards**: Check W3C ARIA APG for the correct pattern
7. **Consider Users**: Think about diverse user needs and assistive technologies
8. **Document Edge Cases**: Include additional considerations for complex scenarios

## Example Interactions

### Example 1: Generate New Docs
```
User: Generate accessibility documentation for the Dropdown component

Agent: I'll generate comprehensive accessibility documentation for the Dropdown component.

[Agent reads existing examples: about-modal, button, accordion, modal]
[Agent searches for Dropdown component documentation]
[Agent identifies the ARIA menu/listbox pattern]
[Agent generates guidelines, testing criteria, props, attributes]
[Agent creates markdown file]

Generated documentation saved to:
packages/documentation-site/patternfly-docs/content/accessibility/dropdown/dropdown.md

The documentation includes:
- 5 accessibility implementation guidelines
- 7 testing criteria with checkboxes
- 4 React props for accessibility
- 6 HTML/CSS attributes and classes
- Focus management considerations
- Link to ARIA APG Menu pattern

Please review and test with assistive technologies.
```

### Example 2: Find Missing Docs
```
User: Which components need accessibility documentation?

Agent: Analyzing components directory and accessibility docs...

Found 40 existing accessibility docs.
Found 52 total components.

Components missing accessibility documentation (12):
- DataList
- Drawer
- Dropdown
- EmptyState
- FormSelect
- Gallery
- InputGroup
- List
- Popover
- Select
- Table
- Toolbar

Would you like me to generate documentation for any of these?
```

### Example 3: Review and Enhance
```
User: Review the Button accessibility documentation and suggest improvements

Agent: Reviewing packages/documentation-site/patternfly-docs/content/accessibility/button/button.md

Current documentation covers:
✓ Keyboard navigation (Tab, Shift+Tab, Enter, Space)
✓ Descriptive text or aria-label
✓ Link new window context
✓ No nested interactive content
✓ isAriaDisabled prop

Suggestions for enhancement:
1. Add testing criteria for button variants (primary, secondary, danger, etc.)
2. Include guidance for icon-only buttons
3. Add example for button with tooltip when disabled
4. Mention loading state accessibility
5. Include link button focus indicator requirements

Would you like me to implement these enhancements?
```

## Common Component Patterns

The agent recognizes these common accessibility patterns:

| Component Type | ARIA Pattern | Key Requirements |
|---------------|--------------|------------------|
| Modal/Dialog | Dialog | Focus trap, aria-modal, ESC to close |
| Dropdown/Menu | Menu/Listbox | Arrow keys, typeahead, focus management |
| Tabs | Tabs | Arrow keys, Home/End, aria-selected |
| Accordion | Accordion | aria-expanded, Enter/Space toggle |
| Tooltip | Tooltip | Focus trigger, ESC to dismiss, describedby |
| Button | Button | Keyboard activation, descriptive label |
| Form Controls | Various | Labels, error messages, validation |
| Navigation | Navigation | Landmark roles, skip links |
| Tables | Table/Grid | Headers, captions, sortable columns |
| Alerts | Alert | Live regions, status messages |

## Error Prevention

The agent helps prevent common mistakes:

❌ **Avoid**:
- Skipping required ARIA attributes
- Incorrect PatternFly class names (v5 vs v6)
- Missing keyboard support
- Poor focus management
- Unclear labels or accessible names
- Inaccessible color contrast
- Missing alternative text
- Focus traps without escape
- Broken tab order

✓ **Include**:
- All required ARIA attributes
- Proper PatternFly v6 classes
- Complete keyboard support
- Clear focus indicators
- Descriptive labels
- Sufficient color contrast
- Alt text for images
- ESC key to exit
- Logical tab order

## Resources Referenced

The agent leverages these authoritative sources:

- [W3C ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [PatternFly Accessibility Guidelines](https://www.patternfly.org/accessibility/about-accessibility)
- [MDN Web Accessibility](https://developer.mozilla.org/en-US/docs/Web/Accessibility)
- [WebAIM Resources](https://webaim.org/)
- [Deque University](https://dequeuniversity.com/)

## Support and Feedback

If the agent produces unexpected results or you need clarification:

1. **Provide more context**: Describe the component's functionality in detail
2. **Share examples**: Reference similar components that already have good docs
3. **Ask specific questions**: "What ARIA attributes does this need?"
4. **Request iterations**: "Can you refine the testing criteria?"
5. **Report issues**: Note any errors or inconsistencies for improvement

## Version History

- **v1.0** (2025-01-11): Initial agent creation with comprehensive accessibility doc generation capabilities

---

**Ready to generate accessibility documentation!** Just provide a component name or ask which components need documentation.

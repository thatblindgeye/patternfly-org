# PatternFly Accessibility Documentation Generator

An AI-powered agent that generates comprehensive accessibility documentation for PatternFly components using Claude AI.

## Overview

This tool analyzes existing accessibility documentation patterns and uses Claude AI to generate new accessibility docs for PatternFly components. It follows the established documentation structure including:

- High-level accessibility guidelines
- Testing criteria with checkboxes
- React component props
- HTML/CSS attributes and classes
- Additional considerations
- Links to W3C ARIA APG patterns

## Features

- **AI-Powered Generation**: Uses Claude Sonnet 4.5 to analyze components and generate comprehensive accessibility guidelines
- **Pattern Recognition**: Learns from existing accessibility docs to maintain consistency
- **Component Analysis**: Finds and analyzes existing component documentation
- **Missing Doc Detection**: Lists components that don't have accessibility documentation
- **Structured Output**: Generates documentation following PatternFly's established format

## Installation

### Prerequisites

- Python 3.7+ (for Python version)
- Node.js 14+ (for JavaScript version)
- Anthropic API key (for AI-powered generation)

### Setup

1. Install required Python packages:
```bash
pip install anthropic
```

2. Set your Anthropic API key:
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Or create a `.env` file in the repository root:
```
ANTHROPIC_API_KEY=your-api-key-here
```

## Usage

### Python Version (Recommended)

#### Generate documentation for a specific component:
```bash
python scripts/generate_a11y_docs.py Dropdown
```

#### List components missing accessibility documentation:
```bash
python scripts/generate_a11y_docs.py --list-missing
```

#### Analyze a component without generating docs:
```bash
python scripts/generate_a11y_docs.py --analyze Dropdown
```

#### Overwrite existing documentation:
```bash
python scripts/generate_a11y_docs.py Dropdown --force
```

#### Use a custom API key:
```bash
python scripts/generate_a11y_docs.py Dropdown --api-key sk-ant-...
```

### JavaScript Version

#### Generate documentation for a specific component:
```bash
node scripts/generate-a11y-docs.js Dropdown
```

Note: The JavaScript version provides a template structure. For AI-powered generation, use the Python version.

## How It Works

### 1. Analysis Phase
The agent analyzes existing accessibility documentation to understand the pattern:
- Reads 3 example accessibility docs as reference
- Extracts the documentation structure
- Identifies common patterns and terminology

### 2. Component Discovery
- Searches for existing component documentation
- Extracts component functionality and features
- Identifies related ARIA patterns from W3C APG

### 3. Content Generation
Using Claude AI, the agent generates:
- **Guidelines** (3-5 items): High-level accessibility implementation guidance
- **Testing Criteria** (5-7 items): Specific checkboxes for manual testing
- **React Props** (3-6 items): Accessibility-related component props
- **HTML/CSS Attributes** (4-8 items): ARIA attributes and PatternFly classes
- **ARIA Pattern**: Corresponding W3C ARIA APG pattern name
- **Additional Considerations** (optional): Special cases and edge cases

### 4. Documentation Assembly
The agent assembles a complete markdown file following the established structure:
```markdown
---
frontmatter
---

imports

## Accessibility
guidelines...

## Testing
checkboxes...

## React customization
props table...

## HTML/CSS customization
attributes table...

## Additional considerations
special cases...

## Further reading
W3C links...
```

### 5. File Output
Saves the documentation to:
```
packages/documentation-site/patternfly-docs/content/accessibility/{component-name}/{component-name}.md
```

## Generated Documentation Structure

### Frontmatter
```yaml
---
id: ComponentName
section: components
---
```

### Accessibility Guidelines
High-level guidance for implementing accessible components:
- Keyboard navigation requirements
- Screen reader support
- Focus management
- ARIA attribute requirements

### Testing Criteria
Interactive checkboxes for manual accessibility testing:
- Keyboard navigation tests
- ARIA attribute verification
- Focus management tests
- Screen reader announcement tests

### React Customization
Table of React props affecting accessibility:
- `aria-label`, `aria-describedby`, etc.
- Component-specific accessibility props
- When each prop is required vs optional

### HTML/CSS Customization
Table of HTML attributes and PatternFly classes:
- ARIA attributes
- Role attributes
- PatternFly v6 classes (`.pf-v6-c-*`)
- Required vs optional indicators

### Additional Considerations (Optional)
Special cases and important notes:
- Focus trap management
- Custom implementations
- Edge cases
- Performance considerations

### Further Reading
Links to related resources:
- W3C ARIA Authoring Practices Guide patterns
- Related WCAG guidelines

## Examples

### Example 1: Generate docs for Select component
```bash
python scripts/generate_a11y_docs.py Select
```

Output:
```
============================================================
PatternFly Accessibility Documentation Generator
============================================================

Component: Select

Found 40 existing accessibility docs
Found component docs at: .../content/components/select/select.md

Generating accessibility documentation for Select using Claude AI...

✓ Documentation saved to: .../accessibility/select/select.md

✓ Documentation generated successfully!

Next steps:
1. Review the generated documentation
2. Enhance with component-specific accessibility requirements
3. Test the documentation with actual component implementation
4. Submit for review
```

### Example 2: List missing documentation
```bash
python scripts/generate_a11y_docs.py --list-missing
```

Output:
```
============================================================
PatternFly Accessibility Documentation Generator
============================================================

Found 40 existing accessibility docs
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
```

## Quality Assurance

After generating documentation, you should:

1. **Review Content**: Ensure the generated content is accurate and relevant
2. **Test Implementation**: Verify the guidelines work with actual components
3. **Check ARIA Patterns**: Confirm the W3C ARIA APG pattern link is correct
4. **Verify Props**: Ensure all React props and HTML attributes are valid
5. **Manual Testing**: Follow the testing criteria with real assistive technologies
6. **Peer Review**: Have accessibility experts review the documentation

## Customization

### Adjusting the AI Prompt
Edit the prompt in `generate_a11y_docs.py` to:
- Change the number of examples provided
- Adjust the level of detail
- Add specific requirements for certain component types
- Include additional context

### Modifying the Template
Update the `generate_documentation()` method to:
- Change the section order
- Add new sections
- Modify the markdown formatting
- Include additional metadata

## Troubleshooting

### API Key Not Found
```
Error: ANTHROPIC_API_KEY environment variable not set
```
Solution: Set the environment variable or use `--api-key` flag

### Component Not Found
```
No existing component docs found, will use component name only
```
Solution: This is a warning, not an error. The generator will still work but may need more manual review.

### JSON Parsing Error
```
Error parsing JSON response
```
Solution: The AI response format may have changed. Check the response text and adjust the JSON parsing logic.

### anthropic Package Not Installed
```
Warning: anthropic package not installed
```
Solution: Install the package: `pip install anthropic`

## Architecture

### Files
- `generate_a11y_docs.py` - Main Python script with Claude AI integration
- `generate-a11y-docs.js` - JavaScript version with template structure
- `README-A11Y-GENERATOR.md` - This documentation

### Classes

#### `AccessibilityDocsGenerator`
Main class that orchestrates the documentation generation process.

**Methods:**
- `analyze_existing_docs()` - Analyzes existing accessibility documentation
- `find_component_docs()` - Locates component documentation files
- `read_example_docs()` - Reads example docs for AI training
- `generate_with_claude()` - Calls Claude AI to generate content
- `generate_documentation()` - Assembles the final markdown file
- `save_documentation()` - Writes the file to disk
- `list_missing_docs()` - Identifies components without a11y docs

## Best Practices

1. **Always Review**: Never publish AI-generated content without human review
2. **Test with AT**: Verify guidelines work with actual assistive technologies
3. **Follow WCAG**: Ensure all recommendations meet WCAG 2.1 Level AA
4. **Component-Specific**: Customize generated docs for each component's unique needs
5. **Keep Updated**: Regenerate docs when components change significantly

## Contributing

To improve the generator:

1. Add more sophisticated component analysis
2. Enhance the AI prompt with better examples
3. Add support for pattern detection across components
4. Implement automatic testing of generated guidelines
5. Add support for other documentation formats

## Resources

- [PatternFly Accessibility Documentation](https://www.patternfly.org/accessibility/about-accessibility)
- [W3C ARIA Authoring Practices Guide](https://www.w3.org/WAI/ARIA/apg/)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Anthropic Claude API Documentation](https://docs.anthropic.com/)

## License

This tool is part of the PatternFly project and follows the same license.

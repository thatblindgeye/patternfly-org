# Quick Start Guide: Accessibility Documentation Generator

## What is this?

An AI-powered tool that automatically generates comprehensive accessibility documentation for PatternFly components using Claude AI. It analyzes existing docs and creates new ones following the established PatternFly accessibility documentation pattern.

## Quick Setup (2 minutes)

### 1. Install Python dependencies
```bash
pip install anthropic
```

### 2. Set your API key
```bash
export ANTHROPIC_API_KEY='your-api-key-here'
```

Get your API key from: https://console.anthropic.com/

### 3. You're ready to go!

## Common Commands

### Generate accessibility docs for a component
```bash
python3 scripts/generate_a11y_docs.py Dropdown
```

### See which components are missing docs
```bash
python3 scripts/generate_a11y_docs.py --list-missing
```

### Run a demo (no API key needed)
```bash
python3 scripts/demo_a11y_generator.py
```

### Check if a component has docs
```bash
python3 scripts/generate_a11y_docs.py --analyze Dropdown
```

## Example Workflow

Let's say you want to create accessibility docs for a "Dropdown" component:

```bash
# Step 1: Check if docs already exist
python3 scripts/generate_a11y_docs.py --analyze Dropdown

# Step 2: Generate the documentation
python3 scripts/generate_a11y_docs.py Dropdown

# Step 3: Review the generated file
# Location: packages/documentation-site/patternfly-docs/content/accessibility/dropdown/dropdown.md

# Step 4: Edit and refine as needed
# Open the file and make any necessary adjustments

# Step 5: Test with the actual component
# Follow the testing criteria in the generated doc
```

## What Gets Generated?

The agent creates a complete accessibility documentation file with:

✓ **Accessibility Guidelines** - High-level implementation guidance
✓ **Testing Criteria** - Interactive checkboxes for manual testing
✓ **React Props** - Accessibility-related component props table
✓ **HTML/CSS Attributes** - ARIA attributes and PatternFly classes table
✓ **Additional Considerations** - Special cases and edge cases
✓ **Further Reading** - Links to W3C ARIA APG patterns

## Output Example

The generated file follows this structure:

```markdown
---
id: ComponentName
section: components
---

import { Checkbox, List, ListItem } from '@patternfly/react-core';

## Accessibility
[Guidelines for implementing accessible components]

## Testing
[Checkbox list of accessibility tests to perform]

## React customization
[Table of accessibility-related React props]

## HTML/CSS customization
[Table of ARIA attributes and PatternFly classes]

## Additional considerations
[Special cases and important notes]

## Further reading
[Links to W3C ARIA APG patterns]
```

## How It Works

1. **Analyzes** existing accessibility docs to learn the pattern
2. **Finds** component documentation (if available)
3. **Generates** content using Claude AI based on:
   - Existing documentation patterns
   - Component functionality
   - WCAG 2.1 Level AA guidelines
   - W3C ARIA Authoring Practices
4. **Assembles** a complete markdown file
5. **Saves** to the accessibility docs directory

## Important Notes

⚠️ **Always review generated content** - AI can make mistakes, especially with component-specific details

✓ **Test with real components** - Verify guidelines work with actual implementations

✓ **Test with assistive tech** - Use screen readers (NVDA, JAWS, VoiceOver) to validate

✓ **Follow WCAG** - Ensure all recommendations meet WCAG 2.1 Level AA standards

## Troubleshooting

**Problem:** `anthropic package not installed`
**Solution:** Run `pip install anthropic`

**Problem:** `ANTHROPIC_API_KEY environment variable not set`
**Solution:** Set the environment variable or use `--api-key` flag

**Problem:** Want to test without using API credits
**Solution:** Run `python3 scripts/demo_a11y_generator.py`

## Files Created

| File | Purpose |
|------|---------|
| `scripts/generate_a11y_docs.py` | Main Python script with AI integration |
| `scripts/generate-a11y-docs.js` | JavaScript version (template only) |
| `scripts/demo_a11y_generator.py` | Demo script (no API calls) |
| `scripts/requirements-a11y-generator.txt` | Python dependencies |
| `scripts/README-A11Y-GENERATOR.md` | Comprehensive documentation |
| `scripts/QUICKSTART-A11Y-GENERATOR.md` | This quick start guide |

## Next Steps

1. **Try the demo** to see what output looks like:
   ```bash
   python3 scripts/demo_a11y_generator.py
   ```

2. **List missing docs** to find components that need documentation:
   ```bash
   python3 scripts/generate_a11y_docs.py --list-missing
   ```

3. **Generate your first doc** for a component:
   ```bash
   python3 scripts/generate_a11y_docs.py YourComponentName
   ```

4. **Review and refine** the generated documentation

5. **Read the full docs** at `scripts/README-A11Y-GENERATOR.md`

## Support

For more details, see:
- `scripts/README-A11Y-GENERATOR.md` - Full documentation
- [PatternFly Accessibility](https://www.patternfly.org/accessibility/about-accessibility)
- [W3C ARIA APG](https://www.w3.org/WAI/ARIA/apg/)

Happy documenting! 🎉

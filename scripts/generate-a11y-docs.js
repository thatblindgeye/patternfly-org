#!/usr/bin/env node

/**
 * Accessibility Documentation Generator for PatternFly Components
 *
 * This agent generates accessibility documentation for PatternFly components
 * by analyzing existing component implementations and following the established
 * documentation pattern.
 *
 * Usage:
 *   node scripts/generate-a11y-docs.js <component-name>
 *
 * Example:
 *   node scripts/generate-a11y-docs.js Dropdown
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ACCESSIBILITY_DOCS_DIR = path.join(__dirname, '../packages/documentation-site/patternfly-docs/content/accessibility');
const COMPONENT_DOCS_DIR = path.join(__dirname, '../packages/documentation-site/patternfly-docs/content');

// Template structure based on existing docs
const TEMPLATE_SECTIONS = {
  frontmatter: (componentName) => `---
id: ${componentName}
section: components
---

`,
  imports: () => `import { Checkbox, List, ListItem } from '@patternfly/react-core';

`,
  accessibility: (componentName, guidelines) => `## Accessibility

To implement an accessible PatternFly **${componentName.toLowerCase()}** component:

${guidelines.map(g => `- ${g}`).join('\n')}

`,
  testing: (componentName, criteria) => `## Testing

At a minimum, a ${componentName.toLowerCase()} should meet the following criteria:

<List isPlain>
${criteria.map((c, idx) => `  <ListItem>
    <Checkbox id="${componentName.toLowerCase()}-a11y-checkbox-${idx + 1}" label={${c.label}} description={${c.description}} />
  </ListItem>`).join('\n')}
</List>

`,
  reactCustomization: (componentName, props) => `## React customization

The following React props have been provided for more fine-tuned control over accessibility.

| Prop | Applied to | Reason |
|---|---|---|
${props.map(p => `| ${p.prop} | \`${componentName}\` | ${p.reason} |`).join('\n')}

`,
  htmlCssCustomization: (componentName, attributes) => `## HTML/CSS customization

The following HTML attributes and PatternFly classes can be used for more fine-tuned control over accessibility.

| Attribute or class | Applied to | Reason |
|---|---|---|
${attributes.map(a => `| ${a.attribute} | ${a.appliedTo} | ${a.reason} |`).join('\n')}

`,
  additionalConsiderations: (considerations) => {
    if (!considerations || considerations.length === 0) return '';
    return `## Additional considerations

Consumers must ensure they take any additional considerations when customizing a ${considerations.componentName}, using it in a way not described or recommended by PatternFly, or in various other specific use-cases not outlined elsewhere on this page.

${considerations.items.map(item => `### ${item.title}\n\n${item.content}`).join('\n\n')}

`;
  },
  furtherReading: (componentName, ariaPattern) => `## Further reading

To read more about accessibility with ${componentName.toLowerCase()}, refer to the following resources:

- [ARIA Authoring Practices Guide - ${ariaPattern}](https://www.w3.org/WAI/ARIA/apg/patterns/${ariaPattern.toLowerCase().replace(/\s+/g, '-')}/)
`
};

/**
 * Analyzes existing accessibility docs to extract patterns
 */
function analyzeExistingDocs() {
  const existingDocs = fs.readdirSync(ACCESSIBILITY_DOCS_DIR)
    .filter(item => {
      const itemPath = path.join(ACCESSIBILITY_DOCS_DIR, item);
      return fs.statSync(itemPath).isDirectory();
    });

  console.log(`Found ${existingDocs.length} existing accessibility docs`);
  return existingDocs;
}

/**
 * Finds component documentation to understand the component's functionality
 */
function findComponentDocs(componentName) {
  const possiblePaths = [
    path.join(COMPONENT_DOCS_DIR, 'design-guidelines', componentName.toLowerCase()),
    path.join(COMPONENT_DOCS_DIR, 'components', componentName.toLowerCase()),
  ];

  for (const basePath of possiblePaths) {
    if (fs.existsSync(basePath)) {
      const files = fs.readdirSync(basePath);
      const mdFiles = files.filter(f => f.endsWith('.md'));
      if (mdFiles.length > 0) {
        return path.join(basePath, mdFiles[0]);
      }
    }
  }

  return null;
}

/**
 * Uses Claude AI to generate accessibility guidelines based on component analysis
 */
async function generateAccessibilityContent(componentName, componentDocs, existingA11yDocs) {
  console.log(`\nGenerating accessibility documentation for ${componentName}...`);
  console.log('This will use Claude AI to analyze the component and generate appropriate guidelines.\n');

  const prompt = `You are generating accessibility documentation for the PatternFly ${componentName} component.

Based on the following information:

1. Existing accessibility documentation examples from similar components
2. Component documentation (if available)
3. WCAG 2.1 Level AA guidelines
4. ARIA Authoring Practices Guide

Generate a comprehensive accessibility documentation following this structure:

ACCESSIBILITY GUIDELINES (3-5 high-level guidelines):
- Each should be a clear, actionable guideline
- Focus on keyboard navigation, screen reader support, ARIA attributes, focus management
- Be specific to this component type

TESTING CRITERIA (5-7 specific test cases):
- Each should be a checkbox item with label and description
- Include keyboard navigation tests
- Include ARIA attribute verification
- Include focus management tests
- Include screen reader announcement tests

REACT PROPS (3-6 accessibility-related props):
- List props that affect accessibility
- Include aria-label, aria-describedby, role, etc.
- Explain when each prop is required vs optional

HTML/CSS ATTRIBUTES (4-8 attributes or classes):
- List relevant ARIA attributes
- Include role attributes
- List PatternFly-specific classes that affect accessibility
- Explain when each is required

ARIA PATTERN NAME:
- The W3C ARIA APG pattern name that most closely matches this component

Format your response as JSON with these keys:
{
  "guidelines": ["guideline 1", "guideline 2", ...],
  "testingCriteria": [
    {"label": "<span>Label with optional <code>code</code></span>", "description": "Description text"},
    ...
  ],
  "reactProps": [
    {"prop": "propName=\"value\"", "reason": "Explanation when required/optional"},
    ...
  ],
  "htmlAttributes": [
    {"attribute": "attribute-name=\"value\"", "appliedTo": ".pf-v6-c-class-name", "reason": "Explanation"},
    ...
  ],
  "ariaPattern": "Pattern Name",
  "additionalConsiderations": {
    "componentName": "${componentName.toLowerCase()}",
    "items": [
      {"title": "Consideration Title", "content": "Detailed explanation"},
      ...
    ]
  }
}

Component to analyze: ${componentName}
`;

  console.log('Please provide the generated content manually or integrate with Claude API.');
  console.log('Expected format: JSON as described above\n');

  // For now, return a template structure
  // In a full implementation, this would call Claude API
  return {
    guidelines: [
      'Ensure the component can be navigated to and interacted with via keyboard',
      'Provide appropriate ARIA attributes for screen reader support',
      'Ensure focus is properly managed when the component state changes',
    ],
    testingCriteria: [
      {
        label: '<span>Standard keyboard navigation can be used to navigate to the component.</span>',
        description: '<span><kbd>Tab</kbd> navigates to the component, and <kbd>Shift</kbd> + <kbd>Tab</kbd> navigates away from it.</span>'
      },
    ],
    reactProps: [
      {
        prop: 'aria-label="[text that labels the component]"',
        reason: 'Adds an accessible name to the component. **Required** when there is no visible text label.'
      },
    ],
    htmlAttributes: [
      {
        attribute: 'aria-label="[text that labels the component]"',
        appliedTo: `.pf-v6-c-${componentName.toLowerCase()}`,
        reason: 'Adds an accessible name to the component. **Required** when there is no visible text label.'
      },
    ],
    ariaPattern: componentName,
    additionalConsiderations: null
  };
}

/**
 * Generates the complete accessibility documentation file
 */
function generateDocumentation(componentName, content) {
  const doc = TEMPLATE_SECTIONS.frontmatter(componentName) +
    TEMPLATE_SECTIONS.imports() +
    TEMPLATE_SECTIONS.accessibility(componentName, content.guidelines) +
    TEMPLATE_SECTIONS.testing(componentName, content.testingCriteria) +
    TEMPLATE_SECTIONS.reactCustomization(componentName, content.reactProps) +
    TEMPLATE_SECTIONS.htmlCssCustomization(componentName, content.htmlAttributes) +
    TEMPLATE_SECTIONS.additionalConsiderations(content.additionalConsiderations) +
    TEMPLATE_SECTIONS.furtherReading(componentName, content.ariaPattern);

  return doc;
}

/**
 * Saves the generated documentation to the appropriate directory
 */
function saveDocumentation(componentName, content) {
  const componentDir = path.join(ACCESSIBILITY_DOCS_DIR, componentName.toLowerCase());
  const filePath = path.join(componentDir, `${componentName.toLowerCase()}.md`);

  if (!fs.existsSync(componentDir)) {
    fs.mkdirSync(componentDir, { recursive: true });
  }

  fs.writeFileSync(filePath, content);
  console.log(`✓ Documentation saved to: ${filePath}`);

  return filePath;
}

/**
 * Main execution function
 */
async function main() {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    console.error('Usage: node generate-a11y-docs.js <component-name>');
    console.error('Example: node generate-a11y-docs.js Dropdown');
    process.exit(1);
  }

  const componentName = args[0];

  console.log('='.repeat(60));
  console.log('PatternFly Accessibility Documentation Generator');
  console.log('='.repeat(60));
  console.log(`\nComponent: ${componentName}\n`);

  // Step 1: Analyze existing docs
  const existingDocs = analyzeExistingDocs();

  // Step 2: Find component documentation
  const componentDocs = findComponentDocs(componentName);
  if (componentDocs) {
    console.log(`Found component docs at: ${componentDocs}`);
  } else {
    console.log('No existing component docs found, will use component name only');
  }

  // Step 3: Check if accessibility doc already exists
  const existingA11yDoc = path.join(ACCESSIBILITY_DOCS_DIR, componentName.toLowerCase());
  if (fs.existsSync(existingA11yDoc)) {
    console.warn(`\n⚠ Accessibility documentation already exists for ${componentName}`);
    console.log('Location:', existingA11yDoc);
    console.log('Use --force flag to overwrite (not yet implemented)\n');
    return;
  }

  // Step 4: Generate content
  const content = await generateAccessibilityContent(componentName, componentDocs, existingDocs);

  // Step 5: Generate documentation
  const documentation = generateDocumentation(componentName, content);

  // Step 6: Save documentation
  const savedPath = saveDocumentation(componentName, documentation);

  console.log('\n✓ Documentation generated successfully!');
  console.log('\nNext steps:');
  console.log('1. Review the generated documentation');
  console.log('2. Enhance with component-specific accessibility requirements');
  console.log('3. Test the documentation with actual component implementation');
  console.log('4. Submit for review\n');
}

// Execute if run directly
if (require.main === module) {
  main().catch(console.error);
}

module.exports = {
  generateAccessibilityContent,
  generateDocumentation,
  analyzeExistingDocs
};

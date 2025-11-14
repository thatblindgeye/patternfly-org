#!/usr/bin/env python3

"""
Accessibility Documentation Generator for PatternFly Components

This agent generates accessibility documentation for PatternFly components
by analyzing existing component implementations and using Claude AI to generate
comprehensive accessibility guidelines.

Usage:
    python scripts/generate_a11y_docs.py <component-name>
    python scripts/generate_a11y_docs.py --list-missing
    python scripts/generate_a11y_docs.py --analyze <component-name>

Examples:
    python scripts/generate_a11y_docs.py Dropdown
    python scripts/generate_a11y_docs.py --list-missing
    python scripts/generate_a11y_docs.py --analyze Dropdown --no-generate
"""

import os
import sys
import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# Try to import anthropic for Claude API
try:
    import anthropic
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    print("Warning: anthropic package not installed. Install with: pip install anthropic")


class AccessibilityDocsGenerator:
    """Generates accessibility documentation for PatternFly components"""

    def __init__(self, repo_root: Path):
        self.repo_root = repo_root
        self.a11y_docs_dir = repo_root / "packages/documentation-site/patternfly-docs/content/accessibility"
        self.content_dir = repo_root / "packages/documentation-site/patternfly-docs/content"

    def analyze_existing_docs(self) -> List[str]:
        """Analyzes existing accessibility docs to extract patterns"""
        if not self.a11y_docs_dir.exists():
            print(f"Error: Accessibility docs directory not found: {self.a11y_docs_dir}")
            return []

        existing_docs = [
            item.name for item in self.a11y_docs_dir.iterdir()
            if item.is_dir()
        ]

        print(f"Found {len(existing_docs)} existing accessibility docs")
        return sorted(existing_docs)

    def find_component_docs(self, component_name: str) -> Optional[Path]:
        """Finds component documentation to understand the component's functionality"""
        possible_paths = [
            self.content_dir / "design-guidelines" / component_name.lower(),
            self.content_dir / "components" / component_name.lower(),
        ]

        for base_path in possible_paths:
            if base_path.exists():
                md_files = list(base_path.glob("*.md"))
                if md_files:
                    return md_files[0]

        return None

    def read_example_docs(self, num_examples: int = 3) -> List[Dict[str, str]]:
        """Reads several existing accessibility docs as examples"""
        existing_docs = self.analyze_existing_docs()
        examples = []

        for doc_name in existing_docs[:num_examples]:
            doc_path = self.a11y_docs_dir / doc_name / f"{doc_name}.md"
            if doc_path.exists():
                with open(doc_path, 'r') as f:
                    examples.append({
                        'name': doc_name,
                        'content': f.read()
                    })

        return examples

    def generate_with_claude(self, component_name: str, api_key: Optional[str] = None) -> Dict:
        """Uses Claude AI to generate accessibility guidelines"""
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic package is required. Install with: pip install anthropic")

        if not api_key:
            api_key = os.getenv('ANTHROPIC_API_KEY')
            if not api_key:
                raise ValueError("ANTHROPIC_API_KEY environment variable not set")

        # Read example documentation
        examples = self.read_example_docs(num_examples=3)
        example_docs = "\n\n---\n\n".join([
            f"Example {i+1}: {ex['name']}\n{ex['content']}"
            for i, ex in enumerate(examples)
        ])

        # Read component docs if available
        component_docs_path = self.find_component_docs(component_name)
        component_docs_content = ""
        if component_docs_path:
            with open(component_docs_path, 'r') as f:
                component_docs_content = f.read()

        prompt = f"""You are an accessibility expert creating documentation for the PatternFly {component_name} component.

I will provide you with:
1. Examples of existing accessibility documentation from similar components
2. Component documentation (if available)

Your task is to generate comprehensive accessibility documentation following the exact same structure and style as the examples.

EXISTING ACCESSIBILITY DOCUMENTATION EXAMPLES:
{example_docs}

{'COMPONENT DOCUMENTATION:\n' + component_docs_content if component_docs_content else 'No existing component documentation available.'}

Now generate accessibility documentation for the {component_name} component following the EXACT structure shown in the examples.

Return your response as a JSON object with the following structure:
{{
  "guidelines": [
    "guideline 1 (should be specific to {component_name})",
    "guideline 2",
    ...
  ],
  "testingCriteria": [
    {{
      "label": "<span>Label text with optional <code className=\\"ws-code\\">code</code></span>",
      "description": "Description text or JSX element as string"
    }},
    ...
  ],
  "reactProps": [
    {{
      "prop": "aria-label=\\"[text that labels the component]\\"",
      "reason": "Explanation with **Required** or optional status"
    }},
    ...
  ],
  "htmlAttributes": [
    {{
      "attribute": "aria-label=\\"[text that labels the component]\\"",
      "appliedTo": ".pf-v6-c-{component_name.lower()}",
      "reason": "Explanation with **Required** or optional status"
    }},
    ...
  ],
  "ariaPattern": "Pattern Name (from W3C ARIA APG)",
  "additionalConsiderations": {{
    "componentName": "{component_name.lower()}",
    "items": [
      {{
        "title": "Consideration Title",
        "content": "Detailed explanation in markdown format"
      }}
    ]
  }}
}}

Important guidelines:
- Be specific to the {component_name} component
- Follow WCAG 2.1 Level AA standards
- Reference W3C ARIA Authoring Practices Guide patterns
- Include 3-5 high-level accessibility guidelines
- Include 5-7 specific testing criteria
- Include 3-6 React props related to accessibility
- Include 4-8 HTML/CSS attributes or classes
- Use the exact same formatting and structure as the examples
- Mark required props/attributes with **Required**
- Use proper PatternFly v6 class names (pf-v6-c-*)
- Include keyboard shortcuts in testing criteria using <kbd> tags
"""

        client = anthropic.Anthropic(api_key=api_key)

        print(f"\nGenerating accessibility documentation for {component_name} using Claude AI...")

        response = client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=4096,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # Extract JSON from response
        response_text = response.content[0].text

        # Try to parse JSON from the response
        try:
            # Look for JSON in code blocks or raw text
            json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
            if json_match:
                json_text = json_match.group(1)
            else:
                # Try to find JSON without code blocks
                json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
                if json_match:
                    json_text = json_match.group(0)
                else:
                    json_text = response_text

            content = json.loads(json_text)
            return content

        except json.JSONDecodeError as e:
            print(f"Error parsing JSON response: {e}")
            print(f"Response text:\n{response_text}")
            raise

    def generate_documentation(self, component_name: str, content: Dict) -> str:
        """Generates the complete accessibility documentation file"""

        # Frontmatter
        doc = f"""---
id: {component_name}
section: components
---

"""

        # Imports
        doc += """import { Checkbox, List, ListItem } from '@patternfly/react-core';

"""

        # Accessibility section
        doc += f"""## Accessibility

To implement an accessible PatternFly **{component_name.lower()}** component:

"""
        for guideline in content['guidelines']:
            doc += f"- {guideline}\n"
        doc += "\n"

        # Testing section
        doc += f"""## Testing

At a minimum, a {component_name.lower()} should meet the following criteria:

<List isPlain>
"""
        for idx, criteria in enumerate(content['testingCriteria'], 1):
            label = criteria['label']
            description = criteria.get('description', '')
            if description:
                doc += f"""  <ListItem>
    <Checkbox id="{component_name.lower()}-a11y-checkbox-{idx}" label={{{label}}} description={{{description}}} />
  </ListItem>
"""
            else:
                doc += f"""  <ListItem>
    <Checkbox id="{component_name.lower()}-a11y-checkbox-{idx}" label={{{label}}} />
  </ListItem>
"""
        doc += """</List>

"""

        # React customization section
        doc += """## React customization

The following React props have been provided for more fine-tuned control over accessibility.

| Prop | Applied to | Reason |
|---|---|---|
"""
        for prop in content['reactProps']:
            doc += f"| `{prop['prop']}` | `{component_name}` | {prop['reason']} |\n"
        doc += "\n"

        # HTML/CSS customization section
        doc += """## HTML/CSS customization

The following HTML attributes and PatternFly classes can be used for more fine-tuned control over accessibility.

| Attribute or class | Applied to | Reason |
|---|---|---|
"""
        for attr in content['htmlAttributes']:
            doc += f"| `{attr['attribute']}` | `{attr['appliedTo']}` | {attr['reason']} |\n"
        doc += "\n"

        # Additional considerations (optional)
        if content.get('additionalConsiderations') and content['additionalConsiderations'].get('items'):
            doc += """## Additional considerations

Consumers must ensure they take any additional considerations when customizing a """
            doc += f"{content['additionalConsiderations']['componentName']}, "
            doc += """using it in a way not described or recommended by PatternFly, or in various other specific use-cases not outlined elsewhere on this page.

"""
            for item in content['additionalConsiderations']['items']:
                doc += f"### {item['title']}\n\n{item['content']}\n\n"

        # Further reading section
        aria_pattern = content['ariaPattern']
        aria_pattern_slug = aria_pattern.lower().replace(' ', '-').replace('(', '').replace(')', '')
        doc += f"""## Further reading

To read more about accessibility with {component_name.lower()}, refer to the following resources:

- [ARIA Authoring Practices Guide - {aria_pattern}](https://www.w3.org/WAI/ARIA/apg/patterns/{aria_pattern_slug}/)
"""

        return doc

    def save_documentation(self, component_name: str, content: str) -> Path:
        """Saves the generated documentation to the appropriate directory"""
        component_dir = self.a11y_docs_dir / component_name.lower()
        component_dir.mkdir(parents=True, exist_ok=True)

        file_path = component_dir / f"{component_name.lower()}.md"
        with open(file_path, 'w') as f:
            f.write(content)

        print(f"✓ Documentation saved to: {file_path}")
        return file_path

    def list_missing_docs(self) -> List[str]:
        """Lists components that don't have accessibility documentation"""
        # This is a simplified version - in reality you'd scan all components
        # from the component docs or PatternFly React package

        existing_a11y = set(self.analyze_existing_docs())

        # Get all component directories from the content folder
        components_dir = self.content_dir / "components"
        all_components = set()

        if components_dir.exists():
            for item in components_dir.iterdir():
                if item.is_dir():
                    # Convert to title case for component name
                    component_name = item.name.replace('-', ' ').title().replace(' ', '')
                    all_components.add(component_name)

        missing = all_components - existing_a11y
        return sorted(list(missing))


def main():
    parser = argparse.ArgumentParser(
        description='Generate accessibility documentation for PatternFly components'
    )
    parser.add_argument(
        'component',
        nargs='?',
        help='Component name to generate docs for (e.g., Dropdown)'
    )
    parser.add_argument(
        '--list-missing',
        action='store_true',
        help='List components missing accessibility documentation'
    )
    parser.add_argument(
        '--analyze',
        metavar='COMPONENT',
        help='Analyze a component without generating docs'
    )
    parser.add_argument(
        '--api-key',
        help='Anthropic API key (defaults to ANTHROPIC_API_KEY env var)'
    )
    parser.add_argument(
        '--force',
        action='store_true',
        help='Overwrite existing accessibility documentation'
    )

    args = parser.parse_args()

    # Find repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent

    generator = AccessibilityDocsGenerator(repo_root)

    print('=' * 60)
    print('PatternFly Accessibility Documentation Generator')
    print('=' * 60)
    print()

    # List missing docs
    if args.list_missing:
        missing = generator.list_missing_docs()
        if missing:
            print(f"Components missing accessibility documentation ({len(missing)}):\n")
            for comp in missing:
                print(f"  - {comp}")
            print()
        else:
            print("All components have accessibility documentation!")
        return

    # Analyze component
    if args.analyze:
        component_name = args.analyze
        print(f"Analyzing component: {component_name}\n")

        existing_docs = generator.analyze_existing_docs()
        component_docs = generator.find_component_docs(component_name)

        if component_docs:
            print(f"✓ Found component docs: {component_docs}")
        else:
            print("✗ No component docs found")

        # Check if a11y doc exists
        a11y_doc_path = generator.a11y_docs_dir / component_name.lower()
        if a11y_doc_path.exists():
            print(f"✓ Accessibility doc exists: {a11y_doc_path}")
        else:
            print(f"✗ Accessibility doc missing")

        return

    # Generate documentation
    if not args.component:
        parser.print_help()
        return

    component_name = args.component

    print(f"Component: {component_name}\n")

    # Check if doc already exists
    existing_a11y_doc = generator.a11y_docs_dir / component_name.lower()
    if existing_a11y_doc.exists() and not args.force:
        print(f"⚠ Accessibility documentation already exists for {component_name}")
        print(f"Location: {existing_a11y_doc}")
        print("Use --force flag to overwrite\n")
        return

    try:
        # Generate content using Claude
        content = generator.generate_with_claude(component_name, args.api_key)

        # Generate documentation
        documentation = generator.generate_documentation(component_name, content)

        # Save documentation
        saved_path = generator.save_documentation(component_name, documentation)

        print('\n✓ Documentation generated successfully!')
        print('\nNext steps:')
        print('1. Review the generated documentation')
        print('2. Enhance with component-specific accessibility requirements')
        print('3. Test the documentation with actual component implementation')
        print('4. Submit for review\n')

    except Exception as e:
        print(f"\n✗ Error generating documentation: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()

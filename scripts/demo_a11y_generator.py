#!/usr/bin/env python3

"""
Demo script for the Accessibility Documentation Generator

This demonstrates what the generator would produce without making actual API calls.
Useful for testing the template structure and understanding the output format.
"""

from pathlib import Path
import sys

# Add the scripts directory to the path
sys.path.insert(0, str(Path(__file__).parent))

from generate_a11y_docs import AccessibilityDocsGenerator


def create_demo_content():
    """Creates demo content as if returned from Claude AI"""
    return {
        "guidelines": [
            "Ensure the component can be navigated to and interacted with via keyboard and other assistive technologies such as screen readers",
            "Provide unique, descriptive labels or accessible names to help users identify the component",
            "Ensure proper focus management when the component's state changes",
            "Use appropriate ARIA attributes to convey the component's purpose and state",
            "Do not place interactive content inside of other interactive elements"
        ],
        "testingCriteria": [
            {
                "label": "<span>Standard keyboard navigation can be used to navigate to and interact with the component.</span>",
                "description": "<span><kbd>Tab</kbd> navigates to the component, and <kbd>Shift</kbd> + <kbd>Tab</kbd> navigates away from it. Interaction keys like <kbd>Enter</kbd> and <kbd>Space</kbd> can activate the component.</span>"
            },
            {
                "label": "<span>The component has a clear and descriptive label or accessible name.</span>",
                "description": "This can be verified by inspecting the component with a screen reader or checking for appropriate aria-label or aria-labelledby attributes."
            },
            {
                "label": "<span>Users are notified of the component's current state.</span>",
                "description": "<span>This can be checked by ensuring ARIA state attributes like <code className=\"ws-code\">aria-expanded</code>, <code className=\"ws-code\">aria-selected</code>, or <code className=\"ws-code\">aria-checked</code> are present and accurate.</span>"
            },
            {
                "label": "Focus is properly managed when interacting with the component.",
                "description": "When the component is activated, focus should move to the appropriate element and return to the trigger element when dismissed."
            },
            {
                "label": "The component can be used with a screen reader.",
                "description": "Test with popular screen readers (NVDA, JAWS, VoiceOver) to ensure all information and interactions are accessible."
            }
        ],
        "reactProps": [
            {
                "prop": "aria-label=\"[text that labels the component]\"",
                "reason": "Adds an accessible name to the component. **Required** when the component does not have a visible text label."
            },
            {
                "prop": "aria-labelledby=\"[id of the element that labels the component]\"",
                "reason": "Adds an accessible name to the component by referencing another element. Use this when there is a visible label element."
            },
            {
                "prop": "aria-describedby=\"[id of the element that describes the component]\"",
                "reason": "Provides additional context or instructions for the component. Useful for helper text or error messages."
            },
            {
                "prop": "isDisabled",
                "reason": "Disables the component and adds appropriate ARIA attributes to convey the disabled state to assistive technologies."
            }
        ],
        "htmlAttributes": [
            {
                "attribute": "aria-label=\"[text that labels the component]\"",
                "appliedTo": ".pf-v6-c-example",
                "reason": "Adds an accessible name to the component. **Required** when the component does not have a visible text label."
            },
            {
                "attribute": "aria-labelledby=\"[id of the element that labels the component]\"",
                "appliedTo": ".pf-v6-c-example",
                "reason": "Adds an accessible name to the component by referencing another element. **Required** when there is a visible label."
            },
            {
                "attribute": "role=\"[appropriate ARIA role]\"",
                "appliedTo": ".pf-v6-c-example",
                "reason": "Defines the component's role for assistive technologies. The specific role depends on the component type."
            },
            {
                "attribute": "aria-expanded=\"[true or false]\"",
                "appliedTo": ".pf-v6-c-example__toggle",
                "reason": "Indicates whether expandable content is currently expanded (true) or collapsed (false). **Required** for components with expandable sections."
            },
            {
                "attribute": "aria-hidden=\"true\"",
                "appliedTo": ".pf-v6-c-example__icon",
                "reason": "Removes decorative icons from the accessibility tree, preventing assistive technologies from announcing unnecessary information. **Required** for decorative icons."
            }
        ],
        "ariaPattern": "Button",
        "additionalConsiderations": {
            "componentName": "example",
            "items": [
                {
                    "title": "Focus management",
                    "content": "When implementing custom focus management, ensure that:\n\n- Focus is always visible when navigating with a keyboard\n- Focus order follows a logical sequence\n- Focus is not trapped unintentionally\n- The focused element is announced correctly by screen readers\n\nWithout proper focus management, keyboard users may have difficulty navigating to or understanding what element currently has focus."
                },
                {
                    "title": "Keyboard shortcuts",
                    "content": "If you implement custom keyboard shortcuts:\n\n- Ensure they don't conflict with browser or screen reader shortcuts\n- Provide documentation for custom shortcuts\n- Allow users to disable or customize shortcuts when possible\n- Test shortcuts with various assistive technologies"
                }
            ]
        }
    }


def main():
    print('=' * 60)
    print('PatternFly Accessibility Documentation Generator - DEMO')
    print('=' * 60)
    print()
    print('This demo shows what the generator produces without making API calls.')
    print()

    # Create generator instance
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    generator = AccessibilityDocsGenerator(repo_root)

    # Use a demo component name
    component_name = "ExampleComponent"

    print(f"Generating demo documentation for: {component_name}")
    print()

    # Create demo content
    content = create_demo_content()

    # Generate documentation
    documentation = generator.generate_documentation(component_name, content)

    # Display the generated documentation
    print("Generated Documentation:")
    print("-" * 60)
    print(documentation)
    print("-" * 60)
    print()

    # Optionally save to a demo location
    demo_output_dir = script_dir / "demo-output"
    demo_output_dir.mkdir(exist_ok=True)

    demo_file = demo_output_dir / f"{component_name.lower()}.md"
    with open(demo_file, 'w') as f:
        f.write(documentation)

    print(f"Demo documentation saved to: {demo_file}")
    print()
    print("Review this file to understand the structure and format")
    print("of generated accessibility documentation.")


if __name__ == '__main__':
    main()

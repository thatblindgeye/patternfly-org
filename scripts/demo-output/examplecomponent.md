---
id: ExampleComponent
section: components
---

import { Checkbox, List, ListItem } from '@patternfly/react-core';

## Accessibility

To implement an accessible PatternFly **examplecomponent** component:

- Ensure the component can be navigated to and interacted with via keyboard and other assistive technologies such as screen readers
- Provide unique, descriptive labels or accessible names to help users identify the component
- Ensure proper focus management when the component's state changes
- Use appropriate ARIA attributes to convey the component's purpose and state
- Do not place interactive content inside of other interactive elements

## Testing

At a minimum, a examplecomponent should meet the following criteria:

<List isPlain>
  <ListItem>
    <Checkbox id="examplecomponent-a11y-checkbox-1" label={<span>Standard keyboard navigation can be used to navigate to and interact with the component.</span>} description={<span><kbd>Tab</kbd> navigates to the component, and <kbd>Shift</kbd> + <kbd>Tab</kbd> navigates away from it. Interaction keys like <kbd>Enter</kbd> and <kbd>Space</kbd> can activate the component.</span>} />
  </ListItem>
  <ListItem>
    <Checkbox id="examplecomponent-a11y-checkbox-2" label={<span>The component has a clear and descriptive label or accessible name.</span>} description={This can be verified by inspecting the component with a screen reader or checking for appropriate aria-label or aria-labelledby attributes.} />
  </ListItem>
  <ListItem>
    <Checkbox id="examplecomponent-a11y-checkbox-3" label={<span>Users are notified of the component's current state.</span>} description={<span>This can be checked by ensuring ARIA state attributes like <code className="ws-code">aria-expanded</code>, <code className="ws-code">aria-selected</code>, or <code className="ws-code">aria-checked</code> are present and accurate.</span>} />
  </ListItem>
  <ListItem>
    <Checkbox id="examplecomponent-a11y-checkbox-4" label={Focus is properly managed when interacting with the component.} description={When the component is activated, focus should move to the appropriate element and return to the trigger element when dismissed.} />
  </ListItem>
  <ListItem>
    <Checkbox id="examplecomponent-a11y-checkbox-5" label={The component can be used with a screen reader.} description={Test with popular screen readers (NVDA, JAWS, VoiceOver) to ensure all information and interactions are accessible.} />
  </ListItem>
</List>

## React customization

The following React props have been provided for more fine-tuned control over accessibility.

| Prop | Applied to | Reason |
|---|---|---|
| `aria-label="[text that labels the component]"` | `ExampleComponent` | Adds an accessible name to the component. **Required** when the component does not have a visible text label. |
| `aria-labelledby="[id of the element that labels the component]"` | `ExampleComponent` | Adds an accessible name to the component by referencing another element. Use this when there is a visible label element. |
| `aria-describedby="[id of the element that describes the component]"` | `ExampleComponent` | Provides additional context or instructions for the component. Useful for helper text or error messages. |
| `isDisabled` | `ExampleComponent` | Disables the component and adds appropriate ARIA attributes to convey the disabled state to assistive technologies. |

## HTML/CSS customization

The following HTML attributes and PatternFly classes can be used for more fine-tuned control over accessibility.

| Attribute or class | Applied to | Reason |
|---|---|---|
| `aria-label="[text that labels the component]"` | `.pf-v6-c-example` | Adds an accessible name to the component. **Required** when the component does not have a visible text label. |
| `aria-labelledby="[id of the element that labels the component]"` | `.pf-v6-c-example` | Adds an accessible name to the component by referencing another element. **Required** when there is a visible label. |
| `role="[appropriate ARIA role]"` | `.pf-v6-c-example` | Defines the component's role for assistive technologies. The specific role depends on the component type. |
| `aria-expanded="[true or false]"` | `.pf-v6-c-example__toggle` | Indicates whether expandable content is currently expanded (true) or collapsed (false). **Required** for components with expandable sections. |
| `aria-hidden="true"` | `.pf-v6-c-example__icon` | Removes decorative icons from the accessibility tree, preventing assistive technologies from announcing unnecessary information. **Required** for decorative icons. |

## Additional considerations

Consumers must ensure they take any additional considerations when customizing a example, using it in a way not described or recommended by PatternFly, or in various other specific use-cases not outlined elsewhere on this page.

### Focus management

When implementing custom focus management, ensure that:

- Focus is always visible when navigating with a keyboard
- Focus order follows a logical sequence
- Focus is not trapped unintentionally
- The focused element is announced correctly by screen readers

Without proper focus management, keyboard users may have difficulty navigating to or understanding what element currently has focus.

### Keyboard shortcuts

If you implement custom keyboard shortcuts:

- Ensure they don't conflict with browser or screen reader shortcuts
- Provide documentation for custom shortcuts
- Allow users to disable or customize shortcuts when possible
- Test shortcuts with various assistive technologies

## Further reading

To read more about accessibility with examplecomponent, refer to the following resources:

- [ARIA Authoring Practices Guide - Button](https://www.w3.org/WAI/ARIA/apg/patterns/button/)

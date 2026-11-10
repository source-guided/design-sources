# Judge how users find and act

Start with what a person arrives knowing and the outcome they want. Identify the actual role, starting scope and authority boundaries. A personalized initial view does not establish that other required exploration is forbidden; technical access to a broader view does not establish that it should be exposed.

Choose how context, available choices, current selection, details and actions relate to each other. The model decides the information hierarchy and controls using task familiarity, repetition, number and variability of choices, device context and existing design conventions. Native controls, visible choices and custom widgets are alternatives with different costs, not ranked defaults.

Consider supporting work in relation to the main task. Decide whether it belongs alongside the current context, in a secondary surface or in another view based on what the user needs to retain and complete. Preserve necessary context and drafts according to the product contract. Determine focus and scroll behavior from that task rather than imposing a fixed panel pattern.

Verify a concrete find-and-act task from the real entry point without developer coaching. Does the interface identify whose context is active, what scope is shown, which object is selected and which object an action changes? After filtering or switching context, observe both the result and action target. Include an outcome outside the initial scope when the product requires one; test an honest empty result where relevant.

Exercise the chosen control's real open, move, commit, cancel and exit behavior. Observe focus and committed value separately. Programmatic value assignment does not demonstrate keyboard selection, native popup appearance or assistive-technology compatibility. Derive exact key expectations from the adopted control's contract. For secondary surfaces, observe whether input and context survive relevant close/reopen or recovery paths, and whether offscreen content is reachable.

For spatial continuity when context changes, follow `interactions` through the UX reference index. When observations expose ambiguity or disorientation, reconsider the interaction rather than adding explanatory copy by default.

Use the [UX reference index](../../../references/index.json) for relevant original guidance: `carbon-dropdown`, `wai-combobox`, `wai-selectonly`, `gov-accordion`, `fluent-drawer` and `google-transit`. These cover different control and task contexts. Product-specific fields, defaults and numerical limits remain with the consuming project.

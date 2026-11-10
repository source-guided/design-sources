# Judge visual expression in context

Use the decision process in `workflow` through the [UX reference index](../../../references/index.json). This source owns the visual relationships that inform that process. It supplies questions for judgment, not a universal style, a catalogue of defects or numerical appearance limits.

## Read the composition as a user

Start with the intended reading order, the relative importance of information and actions, and the adopted product character. Consider the person's familiarity, task frequency, content density and viewing context. Decide which differences need to be noticed and which should remain quiet. More emphasis is not automatically clearer, and a quieter treatment is not automatically better; judge whether the visual signal matches its meaning and consequence.

## Evaluate relationships rather than isolated values

Look at the whole composition and then the material local relationships. Consider how typography, alignment, spacing, shape, scale, contrast and grouping work together to express hierarchy. Does an element appear to belong to its content and peers? Are proportions and visual weight appropriate relative to its label, role and surrounding rhythm? Is space helping reading and action, or separating related things and obscuring priorities? Choose the relationships that matter for this task rather than treating each property as a separate pass/fail item.

## Judge the combined signals

Identify what the person needs to distinguish and what each part of the proposed appearance contributes to that understanding. Consider the current state, input method and surrounding context. Examine the cues together: do they convey different necessary information, make one another easier to understand, or repeat the same distinction with extra visual weight? Compare the combined treatment with a sufficient alternative before accepting all of its parts by default. Stronger and quieter treatments both need a reason grounded in the task.

Separate the required perceptibility and operability from the mechanism chosen to provide them. Semantics, interaction behavior and visible appearance can support the same outcome without being a single inseparable prescription. A browser or component default is a starting implementation, not evidence that its complete appearance is necessary. When a specific mechanism is required by an adopted contract, retain it; otherwise judge its contribution and its interaction with the other cues. Do not remove necessary access merely to achieve a quieter composition.

A component can satisfy an individual criterion and still fit poorly into the whole. Reconsider the combined expression when information is already apparent or several treatments compete for the same attention. Apply this reasoning to the design's meaningful distinctions rather than converting individual appearance properties into a universal checklist.

## Reason about identity across states

Identify what is semantically changing and what remains the same for the person. Start with the existing presentation of that continuing content or action as a comparison point. Decide which visible differences help communicate the real change, and whether their strength is proportionate. A different implementation element does not by itself justify a different visual identity.

Compare the content itself across the relevant states, not only its enclosing rectangle. Consider where reading begins, how text sits and flows, its apparent weight, and its relationship to nearby content and controls. Internal spacing or typography can make unchanged content appear displaced or replaced even when the surrounding layout is stable. Choose the relevant relationships from the task; this is not a demand for identical pixel values in every state.

Evaluate the proposed difference against a treatment that preserves the existing relationships. Explain what would become unclear without it and what reorientation it introduces. A stronger distinction can be warranted when meaning changes; retaining familiarity can be more useful when the person continues working on the same content. Neither adding decoration to signal every state nor suppressing all state distinctions is the default. Resolve the tradeoff in the rendered experience rather than accepting the inherited appearance of a control.

## Form a visual judgment from the effective result

Observe the effective composition before defending the planned treatment. Include contributions from the local component, shared styling and the active interaction state, not just the properties the implementation deliberately changed. Identify the visible relationships that support or conflict with the task's hierarchy and continuity. What is actually visible can extend beyond the layout boxes being measured; stable boxes do not establish that their visible contents and surrounding controls relate appropriately.

Interpret what was observed using the criteria above. Distinguish an intentional relationship from unintended interference, an acceptable tradeoff from an unsupported preference, and an uncertain effect from a confirmed problem. Compare plausible treatments in the same direction and explain the decisive benefit and cost. Revisit the choice when the actual composition contradicts its rationale; do not reduce the review to the subset of properties that already passes a test.

Use the `verification` route for the disposition of material contrary observations. This source owns visual judgment, while the selected verification source owns evidence sufficiency and completion. An image-read receipt shows that an image was accessed, not which relationships were judged or whether a noticed concern was resolved.

Use `selection` for adopted references and user preferences, `interactions` for the effect of transitions on the continuing task, and `feedback-actions` for the meaning and lifetime of results. Keep those owners' criteria there; this source does not prescribe their mechanisms.

# Judge the interaction surface and transition

Apply the shared decision process in `workflow` through the [UX reference index](../../../references/index.json). This source owns the relationship between a changing surface and the user's continuing task. Visual hierarchy, proportion and identity across states are owned by `visual-expression`; consult that owner when evaluating the appearance of a proposed interaction.

## Understand the work the surface supports

Consider task complexity, frequency, familiarity, dependencies, available space and the need to retain or compare surrounding information. For substantial input work, understand what the person knows at entry, what they must prepare, which decisions depend on earlier answers, when validation is useful, and which action commits the result. Use the adopted product contract for what survives navigation, cancellation and failure.

The model chooses the surface and behavior from that context. No surface is prescribed by a field count or by the desire to conceal a layout problem. Consider how plausible alternatives would change the user's effort and the context they retain.

## Follow the action through the transition

Identify what the person is reading or acting on and the next meaningful action. Follow relevant states and consider what appears, disappears, moves, changes meaning or becomes unavailable, including effects outside the changing region. Reason from the person's reading position, attention and action target, not just the component's internal state.

For a consequential change, consider the effort to locate the next action, relocate content, recover context, correct input or repeat work. A small repeated task can make an interruption expensive; a more involved task can justify a larger change of surface. Decide whether the benefit warrants the cost. Neither zero movement nor a familiar interaction pattern decides that balance.

Evaluate coupled changes along the actual task, including the transition into recovery and back to the next action where relevant. Introducing or removing information can alter the surrounding reading order, available space and action locations even when the control itself is unchanged. A useful piece of information does not automatically justify the disruption created by its placement. Consider the person's position and what they must operate next while choosing the treatment, rather than accepting that cost after implementation because the result is visible.

When observation is needed to settle that judgment, choose comparable states and meaningful surroundings. Separate changes caused by content, document layout, scrolling and focus so the observation answers the question. Use representative content or a counterexample that could challenge the rationale; do not impose a universal geometry or state matrix. Return to the shared workflow to conclude whether to retain or revise the treatment rather than treating measurement as the conclusion.

## Follow the owning references

Use `feedback-actions` through the same index for the meaning, scope and lifetime of action results, and `task-navigation` for finding an item, selection and control behavior. The consuming project's selected verification source owns evidence sufficiency and completion reporting.

Relevant external references include `atlassian-inline`, `carbon-modal`, `fluent-drawer`, `nng-modal`, `visa-wizard` and `web-cls`. Select them for a material question and read their scope before relying on them. A pattern name or metric does not decide whether an interaction is appropriate.

# Judge the screen from the user's task

This workflow owns the shared design decision process. It applies to visual expression as well as interaction behavior. The result is a reasoned choice for the user's task, not a component recipe or a checklist score. Follow the connected reference client's entry procedure for source reading and coverage.

## Find the relevant owners

Through the [UX reference index](../../../references/index.json), use `selection` for user direction and relevant references, `visual-expression` for visual hierarchy, proportion and coherence, `task-navigation` for finding and acting, `interactions` for surfaces and state transitions, `feedback-actions` for action results and recovery, and `verification` for bringing the applicable observations together. Identify the material questions this change introduces; do not read every branch mechanically. A visible screen or state change has a visual design question even when its behavior uses a familiar component.

## Make and revisit the design choice

1. **Establish the intended experience.** Identify the user's purpose, current context and next meaningful action. Include what they should notice first, what remains supporting information, and the adopted visual direction. Supplied designs, accepted preferences and existing components are inputs. Distinguish a required user outcome from a mandated mechanism: identify the adopted contract before treating one particular visual or interaction treatment as compulsory. Preserve the required outcome while keeping unspecified implementation choices open.

2. **Establish the need for a change.** Start with what the existing experience already lets the user understand and do. Identify the remaining uncertainty or task obstacle. Compare the proposal with leaving that experience alone: what would the person lose without the addition or transformation? An implementation event is not itself a user need. Decide whether any additional treatment is warranted before choosing its form. Deliberately retaining the existing presentation or omitting an additional signal can be a complete design decision.

3. **Separate continuity from change.** Identify what actually changes in the user's task or understanding and what should still be recognized as the same content, action or context. Use that distinction to choose what to preserve and what to make visibly different. Follow the relevant owner sources for both the information being conveyed and its rendered expression; do not infer continuity merely because the outer component remains in place.

4. **Compare the effects and tradeoffs.** Consider the smallest sufficient treatment and plausible alternatives under the same constraints. Judge what each helps the person understand or do, what it duplicates, and what attention, reorientation or loss of coherence it costs. This may be a brief comparison rather than multiple mockups. Assess the combined treatment and its effects on the surrounding task, not just each element in isolation. Individually defensible additions can together become redundant or disruptive. Functional success, geometric stability and familiar component defaults do not settle the choice. Challenge the proposal against the unchanged experience before rationalizing an implementation that already exists.

5. **Challenge the rendered result, then conclude.** First observe what the user actually encounters in the relevant states, including effects not named in the original design rationale. Use the owning sources to judge those observations against the intended experience. Then decide whether the choice should be retained or revised. Keep the observation distinct from an explanation of why the implementation was chosen; a plausible rationale must not conceal a conflicting result. Follow `verification` for handling contrary observations before making a completion claim. Opening an image, retaining a layout coordinate or passing a functional check does not itself close a design question.

Scale the reasoning to the decision. A short explanation in the existing owner record can be enough. No separate document, universal state matrix, fixed number of alternatives or approval gate is required. Observation and measurement serve unresolved design questions; they are not the purpose of this process.

## Follow through

Use `verification` through the same index for the relevant owner observations. The consuming project's selected verification source owns evidence sufficiency and completion reporting. Keep code correctness, observed design quality and user acceptance distinct. Source access establishes what was read, not that the resulting design judgment was adequate.

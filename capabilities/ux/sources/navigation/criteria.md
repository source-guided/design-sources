# Information architecture and action discovery

Organize information and routes around the purposes and evidence identified through the [context area](../../../../references/context/index.json), including the user's familiarity and authority. The same object can serve different purposes; viewing it must be a useful stopping point, while acting on it must have a discoverable continuation. Page boundaries and data structures do not define the user's task.

## Purpose and information priority

- Can the user recognize what this view is for, what it applies to and what they can accomplish here using familiar task language?
- Given that context, which result, information or action is useful immediately, and what belongs in an optional overview or deeper detail? Can the user obtain the likely needed result without first locating and interpreting an entire collection? Choose emphasis from task relevance and the consequences of missing information, while keeping other plausible purposes easy to reach.
- Which information is necessary for the current purpose and decision, and which detail is useful only on request? Keep essential conditions and consequences available where they are needed; reducing visible content must not hide what makes a decision valid.
- Can someone seeking an overview finish without entering a management flow, and can someone needing detail or an action find the appropriate route without inspecting unrelated information? Choose distinctions from actual user intent and permissions rather than inventing a page for every role.
- Are optional details clearly named and discoverable, with enough summary to decide whether to open them? A smaller initial view is useful only when it preserves understanding and access.

## Roles within the composition

- What user purpose does each information or action region serve, what scope does it act on, and what understanding or result does it provide? Explain the contribution in task terms; a component name, familiar layout or different label does not establish a role.
- When regions offer related information or choices, do their scopes, destinations or effects differ meaningfully to the user? Judge them together in the states where they coexist. Can users understand the relationship without testing each control or guessing whether they are alternatives, levels or repeated access to the same thing?
- If their roles overlap, what user benefit requires both placements in that context, and does it outweigh the extra scanning, choice or apparent hierarchy? Repeated access can be useful; repetition alone is not a defect. Compare keeping, combining or removing a region by what task capability or access would be lost and what burden would be removed. Keep the chosen rationale with the product's decisions rather than relying on an assumed convention.

## Continuation across views and actions

- When moving to another view, does the destination continue the user's purpose with the relevant object, scope and prior choices, or merely present another page? Can the user recognize whether the task is complete, what remains and which next action is useful?
- Can the program prepare a useful route, next step or ready-to-use result from explicit intent and evidence-supported context, leaving only necessary decisions to the user? Routine use should not require reconstructing a workflow or confirming choices whose answer is already established. Defaults and suggested paths need a basis in the task and remain inspectable and changeable where relevant; preparation does not grant authority for an unrequested consequential action.
- Are the information, comparisons and eligible choices needed for that action available in context, without requiring the user to remember values or reconstruct domain rules elsewhere? When selection requires domain judgment, expose applicable guidance or alternatives and their reasons using the product's authoritative rules and data. Do not infer an algorithm or require a recommendation feature for every interface.
- If a proposed action affects related objects or a wider plan, can the user understand that scope and inspect the resulting tradeoffs before proceeding? Keep follow-up choices connected to the original goal; distinguish a proposal from an applied change and make unmet constraints understandable. The domain owner determines dependencies, validity and recomputation; this area owns how users find and understand that support.
- Can the user return, revise a choice or inspect supporting detail without losing their task context? State preservation and transition behavior belong to the [interaction area](../../../../references/interaction/index.json); outcome and recovery explanations belong to the [feedback area](../../../../references/feedback/index.json).

## Judge the whole task

Use representative user purposes to inspect what people must read, infer, remember, enter and revisit from entry to a meaningful stopping point. Where an existing way of working is known, compare that burden with the proposed flow. Reduce unnecessary navigation and learning without crowding unrelated tasks onto one page or imposing a universal click count, page count or component. A reachable destination and a successful click do not establish that the user knows how to proceed. Challenge the chosen starting view with a different plausible purpose and with absent or stale context: can the user recognize what applies, correct the assumption and reach the intended outcome? Check whether the program could have prepared information or choices that the user still has to reconstruct.

[Supporting references](../../../../references/navigation/index.json) belong to this subject. Product-specific choices, algorithms and evaluation cases remain with their product or task.

# Information architecture and action discovery

Organize information and routes around the user's intended outcome, familiarity and authority. The same object can serve different purposes; viewing it must be a useful stopping point, while acting on it must have a discoverable continuation. Page boundaries and data structures do not define the user's task.

## Purpose and information priority

- Can the user recognize what this view is for, what it applies to and what they can accomplish here using familiar task language?
- Which information is necessary for the current purpose and decision, and which detail is useful only on request? Keep essential conditions and consequences available where they are needed; reducing visible content must not hide what makes a decision valid.
- Can someone seeking an overview finish without entering a management flow, and can someone needing detail or an action find the appropriate route without inspecting unrelated information? Choose distinctions from actual user intent and permissions rather than inventing a page for every role.
- Are optional details clearly named and discoverable, with enough summary to decide whether to open them? A smaller initial view is useful only when it preserves understanding and access.

## Continuation across views and actions

- When moving to another view, does the destination continue the user's purpose with the relevant object, scope and prior choices, or merely present another page? Can the user recognize whether the task is complete, what remains and which next action is useful?
- Can the program prepare a useful route, next step or ready-to-use result from the user's expressed intent and known state, leaving only necessary decisions to the user? Routine use should not require reconstructing a workflow or confirming choices whose answer is already established. Defaults and suggested paths need a basis in the task and remain inspectable and changeable where relevant; preparation does not grant authority for an unrequested consequential action.
- Are the information, comparisons and eligible choices needed for that action available in context, without requiring the user to remember values or reconstruct domain rules elsewhere? When selection requires domain judgment, expose applicable guidance or alternatives and their reasons using the product's authoritative rules and data. Do not infer an algorithm or require a recommendation feature for every interface.
- If a proposed action affects related objects or a wider plan, can the user understand that scope and inspect the resulting tradeoffs before proceeding? Keep follow-up choices connected to the original goal; distinguish a proposal from an applied change and make unmet constraints understandable. The domain owner determines dependencies, validity and recomputation; this area owns how users find and understand that support.
- Can the user return, revise a choice or inspect supporting detail without losing their task context? State preservation and transition behavior belong to the [interaction area](../../../../references/interaction/index.json); outcome and recovery explanations belong to the [feedback area](../../../../references/feedback/index.json).

## Judge the whole task

Use representative user purposes to inspect what people must read, infer, remember, enter and revisit from entry to a meaningful stopping point. Where an existing way of working is known, compare that burden with the proposed flow. Reduce unnecessary navigation and learning without crowding unrelated tasks onto one page or imposing a universal click count, page count or component. A reachable destination and a successful click do not establish that the user knows how to proceed.

[Supporting references](../../../../references/navigation/index.json) belong to this subject. Product-specific choices, algorithms and evaluation cases remain with their product or task.

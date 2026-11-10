# Ordinary state changes preserve layout continuity

Editing and ordinary local state changes must preserve surrounding content and the positions needed to continue the task. Changing a control's implementation, showing validation or reporting a local result must not make the user relocate ongoing reading or action targets.

A user-requested change of view or displayed structure is different from a local state transition. Treating an implementation change as intentional does not exempt it from this constraint. The implementation mechanism remains a design choice; this source does not prescribe a component, spacing value or fixed template.

Relevant evidence is the actual transition with comparable content and surroundings, including document position, viewport position, scrolling and focus. An isolated final screenshot or successful operation does not establish continuity. Other interaction questions and original references are in this area's [reference entry](../../../../references/interaction/index.json).

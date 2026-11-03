# Verify product interaction flows

Apply only the checks relevant to the actual task and adopted design.

- Role/permission behavior and rendered UX for affected paths.
- Each primary role's entry-to-outcome path and a concrete find-and-act task from visible UI. Check current scope, selected item, and detail/action identity after filtering; do not substitute the administrator view for other roles. Use UX reference `task-navigation` where relevant.
- First use without prepared successful state, repeat use, and a required outcome outside the default scope where relevant. For an input journey, check preparation, start, recovery/backtracking, and the final commit boundary from visible UI, not just whether the submitted payload is valid.
- Open controls and secondary surfaces: selection/commit/cancel keyboard paths, viewport-edge clipping, close/reopen draft preservation, main-page anchors, scrollbar width, and return focus.
- Interaction transitions: expected stable controls, scroll, and focus across editing, cancellation, errors, and loading. Distinguish intended expansion from incidental layout jumps; load-only metrics are insufficient.
- Data-dependent transitions with and without conditional context, including appearance and disappearance. Select contrasting inputs while holding the task constant; inspect the changing region and meaningful downstream anchors. A static screenshot or no horizontal overflow does not cover this behavior.
- Feedback lifecycle and scope: completion/cancel events do not remain as unrelated page state; contextual messages belong to the current item; temporary messages clear as designed while actionable errors remain recoverable. Check actual action-region correspondence, not only stable siblings. Use UX reference `feedback-actions` for the decision method.

Keep evidence tied to the observed revision; do not claim user acceptance or unobserved behavior.

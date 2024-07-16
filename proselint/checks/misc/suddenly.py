"""
Suddenly.

---
layout:     post
source:     Reference for Writers
source_url: http://bit.ly/1E94vyD
title:      suddenly
date:       2014-06-10
categories: writing
---

“Sudden” means quickly and without warning, but using the word “suddenly” both
slows down the action and warns your reader. Do you know what's more effective
for creating the sense of the sudden? Just saying what happens.

When using “suddenly,” you communicate through the narrator that the action
seemed sudden. By jumping directly into the action, you allow the reader to
experience that suddenness first hand. “Suddenly” also suffers from being
nondescript, failing to communicate the nature of the action itself; providing
no sensory experience or concrete fact to hold on to. Just … suddenly.

Feel free to employ “suddenly” in situations where the suddenness is not
apparent in the action itself. For example, in “Suddenly, I don't hate you
anymore,” the “suddenly” substantially changes the way we think about the
shift in emotional calibration.
"""

from __future__ import annotations

from proselint.checks import (
    CheckFlags,
    CheckRegistry,
    CheckSpec,
    Existence,
    Pd,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "Suddenly, it all made sense.",
]

check = CheckSpec(
    Existence(
        ["Suddenly,"],
        padding=Pd.disabled,
    ),
    "misc.suddenly",
    "Suddenly is nondescript, slows the action, and warns your reader.",
    flags=CheckFlags(limit_results=3),
    ignore_case=False,
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)

"""
Bureaucratese.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      bureaucratese
date:       2014-06-10
categories: writing
---

Bureaucratese.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "I hope the report meets with your approval.",
]

check = CheckSpec(
    Existence([
        # TODO: met with your approval?
        "meet with your approval",
        "meets with your approval",
    ]),
    "misc.bureaucratese",
    "'{}' is bureaucratese.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)

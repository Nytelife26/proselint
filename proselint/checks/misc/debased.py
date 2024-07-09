"""
Debased language.

---
layout:     post
source:     ???
source_url: ???
title:      yelling
date:       2014-06-10
categories: writing
---

Too much yelling.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "This leaves much to be desired.",
]


def check(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "misc.debased"
    msg = "Debased language is a continuous temptation."

    items = [
        "a not unjustifiable assumption",
        "leaves much to be desired",
        "would serve no purpose",
        "a consideration which we should do well to bear in mind",
    ]

    return existence_check(text, items, err, msg)


registry.register("misc.debased", check)

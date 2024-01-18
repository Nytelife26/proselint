"""Pretension.

---
layout:     post
source:     ???
source_url: ???
title:      pretension
date:       2014-06-10
categories: writing
---

Never use the phrase 'all hell broke loose'.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import limit_results

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "We need to reconceptualize the project.",
]


@limit_results(1)
def check(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "misc.pretension.ogilvy"
    msg = "Jargon words like this one are the hallmarks of a pretentious ass."

    items = [
        "reconceptualize",
        "demassification",
        "attitudinally",
        "judgmentally",
    ]

    return existence_check(text, items, err, msg)

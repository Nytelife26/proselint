"""
Too much yelling.

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

from proselint.checks import (
    CheckResult,
    Pd,
    existence_check,
    limit_results,
    ppm_threshold,
    registry,
)

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "The QUICK BROWN fox juMPED over the lazy cat.",
    "Sally sells seashells and they were too expensive!",
]

examples_fail = [
    "Sally sells seashells and they were too expensive!!!!",
    "Sally sells seashells and they were too expensive! They were not!",
    "I'm really excited!!",
    "I'm really excited! Really!",
]


@limit_results(1)
def check_repeated_exclamations(text: str) -> list[CheckResult]:
    """Check the text."""
    err = "typography.exclamation.leonard.repeated"
    msg = "Stop yelling. Keep your exclamation points under control."

    items = [r"[\!]\s*?[\!]{1,}"]

    return existence_check(
        text,
        items,
        err,
        msg,
        padding=Pd.disabled,
        ignore_case=False,
        dotall=True,
    )


@ppm_threshold(30)  # TODO: isn't that way too low?
def check_exclamations_ppm(text: str) -> list[CheckResult]:
    """Make sure that the exclamation ppm is under 30."""
    err = "typography.exclamation.leonard.30ppm"
    msg = "More than 30 ppm of exclamations. Keep them under control."

    items = [r"\w!"]

    return existence_check(text, items, err, msg, padding=Pd.disabled)


registry.register_many({
    "typography.exclamation.leonard.repeated": check_repeated_exclamations,
    "typography.exclamation.leonard.30ppm": check_exclamations_ppm,
})

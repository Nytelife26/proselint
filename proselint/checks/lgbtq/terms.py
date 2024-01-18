"""GLAAD.

---
layout:     post
source:     GLAAD Media Reference Guide - 9th Edition
source_url: http://www.glaad.org/reference
title:      GLAAD Guidelines
date:       2016-07-06
categories: writing
---

This check looks for possibly offensive terms related to LGBTQ issues and
makes more acceptable recommendations. TheNew York Times and
Associated Press have also adopted this style guide.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "They were a gay couple.",
    "Homosexual.",
]

examples_fail = [
    "He was a homosexual man.",
    "My sexual preference is for women.",
]


def check(text: str) -> list[ResultCheck]:
    """Suggest preferred forms given the reference document."""
    err = "lgbtq.terms.glaad"
    msg = "Possibly offensive term. Consider using '{}' instead of '{}'."

    items = [
        ["gay man", ["homosexual man"]],
        ["gay men", ["homosexual men"]],
        ["lesbian", ["homosexual woman"]],
        ["lesbians", ["homosexual women"]],
        ["gay people", ["homosexual people"]],
        ["gay couple", ["homosexual couple"]],
        ["sexual orientation", ["sexual preference"]],
        ["openly gay", ["admitted homosexual", "avowed homosexual"]],
        ["equal rights", ["special rights"]],
    ]

    return preferred_forms_check(text, items, err, msg, ignore_case=False)

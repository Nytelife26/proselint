"""Don't start a paragraph with 'But'.

---
layout:     post
source:     Justin Jungé
source_url:
title:      paragraph-start-with-but
date:       2016-03-10
categories: writing
---

Paragraphs should not start with certain bad words.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    'But I never start with the word "but".',
    """I never start with the word "but",
but might use it after a linebreak.""",
]


def check(text: str) -> list[ResultCheck]:
    """Do not start a paragraph with a 'But'."""
    err = "misc.but"
    msg = "No paragraph or sentence should start with a 'But'."
    regex = r"(^|([\n\r\.]+))(\s*)But"

    return existence_check(
        text, [regex], err, msg, ignore_case=False, padding=Pd.disabled
    )

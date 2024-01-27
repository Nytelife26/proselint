"""Punctuation.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      Punctuation
date:       2014-06-10
categories: writing
---

Dates.

"""
from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import ResultCheck
from proselint.checks import existence_check
from proselint.checks import existence_check_simple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "A cat can sleep 20.5 hours a day.",
    "I asked the Prof. what to do",
]

examples_fail = [
    "See Smith et. al.",
    "i drive 5,5 kmh.",
    "I usually wait an hour. and then another.",
]


def check_garner(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "punctuation.misc.garner"
    msg = "Misplaced punctuation. It's 'et al.'"

    items = [
        r"et\. al",
        r"et\. al\.",
    ]
    return existence_check(text, items, err, msg, padding=Pd.sep_in_txt)


def check_lower_case_after_punctuation(text: str) -> list[ResultCheck]:
    """can have false positives after abbreviations"""
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    err = "punctuation.misc.lower_case"
    msg = "Is the lower case letter correct after the punctuation? here '{}'."
    regex = r"\b[a-z]+[\.!\?]\s+[a-z]+\b"
    exceptions = [
        r"al\.",
        r"lat\.",
        r"vs\.",
        r"etc\.",
        r"Prof\.",
        r"Dr\.",
        r"[vV]ol\.",
        r"[fF]ig\.",
    ]
    # en, TODO: add more, sync with numbers/sentence
    # exceptions_de = ["bzw.", "ca.", "cf.", "etc.", "vgl.",
    #                   "no.", "m.E", "m.a.W.", "u.U.", "s.u.", "z.B."]
    return existence_check_simple(
        text, regex, err, msg, ignore_case=False, exceptions=exceptions
    )


def check_comma_digits(text: str) -> list[ResultCheck]:
    # src = https://github.com/entorb/typonuketool/blob/main/subs.pl#L325
    # note: tnt has also check for german numbers, not implemented here
    err = "punctuation.misc.comma_digits"
    msg = "In English ',' is used as decimal separator."
    regex = Pd.words_in_txt.value.format(r"\d+,\d+")
    # NOTE: intentional words_in_txt

    return existence_check_simple(text, regex, err, msg)

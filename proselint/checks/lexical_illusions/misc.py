"""
Lexical illusions.

---
layout:     post
source:     write-good
source_url: https://github.com/btford/write-good
title:      Lexical illusion present
date:       2014-06-10
categories: writing
---

A lexical illusion is when a word word is unintentionally repeated twice, and
and this happens most often between line breaks.

"""
from __future__ import annotations

from proselint.checks import CheckResult, existence_check_simple, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "And he's gone, gone with the breeze",
    "You should know that that sentence wasn't wrong.",
    "She had had dessert on the balcony.",
    "The practitioner's side",
    "An antimatter particle",
    "The theory",
    "She had coffee at the Foo-bar bar.",
    "Don't just play the game - play the game.",
    "green greenery",
]

examples_fail = [
    "Paris in the the springtime.",
    "You should know that that that was wrong.",
    "She had coffee at the Foo bar bar.",
    "She she coffee at the Foo-bar.",
    "After I write i write i write.",
    "that is an echo is an echo",
    "don't miss the biggest illusion miss the biggest illusion.",
]


def check_repetitions(text: str) -> list[CheckResult]:
    """Check the text."""
    # src = "https://github.com/entorb/typonuketool/blob/main/subs.pl"
    err = "lexical_illusions.misc"
    msg = "There's a lexical illusion in '{}' - one or more words are repeated."
    # check for repetition of 1 to 4 words
    regex = r"\b(?<!\\|\-)(\w+(?:\s+\w+){0,3})(?:\s+\1)+\b"
    # NOTE: this can't be padded without mod -> \1
    exceptions = [r"^had had$", r"^that that$"]
    return existence_check_simple(
        text,
        regex,
        err,
        msg,
        exceptions=exceptions,
    )


registry.register("lexical_illusions.misc", check_repetitions)

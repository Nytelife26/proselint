"""
Archaism.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      archaism
date:       2014-06-10
categories: writing
---

Archaism.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "I want to sleep, and maybe dream.",
]

examples_fail = ["I want to sleep, perchance to dream."]

check = CheckSpec(
    Existence([
        "alack",
        "anent",
        # "anon",
        "begat",
        "belike",
        "betimes",
        "boughten",
        "brocage",
        "brokage",
        "camarade",
        "chiefer",
        "chiefest",
        "Christiana",
        "completely obsolescent",
        "cozen",
        "divers",
        "deflexion",
        "durst",
        "fain",
        "forsooth",
        "foreclose from",
        "haply",
        "howbeit",
        "illumine",
        "in sooth",
        "maugre",
        "meseems",
        "methinks",
        "nigh",
        "peradventure",
        "perchance",
        "saith",
        "shew",
        "sistren",
        "spake",
        "to wit",
        "verily",
        "whilom",
        "withal",
        "wot",
        "enclosed please find",
        "please find enclosed",
        "enclosed herewith",
        "enclosed herein",
        "inforce",
        "ex postfacto",
        "forewent",
        "for ever",
        # "designer", when used to mean a plotter against Christ
        # "demean", when used to mean "to behave" in legal contexts
        # "by the bye", # variant, modern is "by the by"
        # "comptroller" # in British English
        # "abortive" Abortive is archaic in reference to abortions,
        # except in the sense “causing an abortion.”
    ]),
    "archaism.misc",
    "'{}' is archaic.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)

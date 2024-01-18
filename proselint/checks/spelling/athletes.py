"""Misspellings.

---
layout:     post
source:     The Wall Street Journal
source_url: http://on.wsj.com/1rksm8k
title:      misspellings of athletes
date:       2014-06-10
categories: writing
---

Points out misspellings.

"""
from __future__ import annotations

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
"One of the greats: Cal Ripkin.",
]

def check(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms."""
    err = "spelling.athletes"
    msg = "Misspelling of athlete's name. '{}' is the preferred form."

    misspellings = [
        ["Dwyane Wade", ["Dwayne Wade"]],
        ["Miikka Kiprusoff", ["Mikka Kiprusoff"]],
        ["Mark Buehrle", ["Mark Buerhle"]],
        ["Skylar Diggins", ["Skyler Diggins"]],
        ["Agnieszka Radwanska", ["Agnieska Radwanska"]],
        ["J.J. Redick", ["J.J. Reddick"]],
        ["Manny Pacquiao", ["Manny Packquaio"]],
        ["Antawn Jamison", ["Antwan Jamison"]],
        ["Cal Ripken", ["Cal Ripkin"]],
        ["Jhonny Peralta", ["Johnny Peralta"]],
        ["Monta Ellis", ["Monte Ellis"]],
        ["Alex Rodriguez", ["Alex Rodriquez"]],
        ["Mark Teixeira", ["Mark Texeira"]],
        ["Brett Favre", ["Brett Farve"]],
        ["Torii Hunter", ["Tori Hunter"]],
        ["Stephen Curry", ["Stephon Curry"]],
        ["Mike Krzyzewski", ["Mike Kryzewski"]],
    ]

    return preferred_forms_check(text, misspellings, err, msg)

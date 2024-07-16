"""
Metadiscourse.

---
layout:     post
source:     Pinker's book on writing
source_url: ???
title:      metadiscourse
date:       2014-06-10
categories: writing
---

Points out metadiscourse.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, Existence

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It's based on the rest of this article.",
]

check = CheckSpec(
    Existence([
        "The preceeding discussion",
        "The rest of this article",
        "This chapter discusses",
        "The preceding paragraph demonstrated",
        "The previous section analyzed",
    ]),
    "misc.metadiscourse",
    "Excessive metadiscourse.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)

"""-ve vs. -of."""

from __future__ import annotations

from proselint.checks import CheckResult, preferred_forms_check_opti, registry

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "This could of been the third test.",
]


def check(text: str) -> list[CheckResult]:
    """-ve vs. -of."""
    err = "spelling.ve_of"
    msg = "-ve vs. -of. '{}' is the preferred spelling."

    items: dict[str, str] = {
        "could of": "could've",
        "should of": "should've",
        "would of": "would've",
    }
    return preferred_forms_check_opti(text, items, err, msg)


registry.register("spelling.ve_of", check)

"""
Animal adjectives.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      animal words
date:       2014-06-10
categories: writing
---

Animal words.

"""

from __future__ import annotations

from proselint.checks import CheckRegistry, CheckSpec, PreferredFormsSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It was some bird-like creature.",
]

check = CheckSpec(
    PreferredFormsSimple({
        "hawk-like": "accipitrine",
        "goose-like": "anserine",
        "eagle-like": "aquiline",
        "bird-like": "avine",
        "crab-like": "cancrine",
        "goat-like": "hircine",
        "deer-like": "damine",
        "crow-like": "corvine",
        "raven-like": "corvine",
        "crocodile-like": "crocodiline",
        "rattlesnake-like": "crotaline",
        "falcon-like": "falconine",
        "wild animal-like": "ferine",
        "hippopotamus-like": "hippopotamine",
        "swallow-like": "hirundine",
        "porcupine-like": "hystricine",
        "lizard-like": "lacertine",
        "gull-like": "laridine",
        "hare-like": "leporine",
        "earthworm-like": "lumbricine",
        "wolf-like": "lupine",
        "mouse-like": "murine",
        "sheep-like": "ovine",
        "leopard-like": "pardine",
        "panther-like": "pardine",
        "sparrow-like": "passerine",
        "peacock-like": "pavonine",
        "woodpecker-like": "picine",
        "fish-like": "piscine",
        "frog-like": "ranine",
        "centipede-like": "scolopendrine",
        "shrew-like": "soricine",
        "ostrich-like": "struthionine",
        "swine-like": "suilline",
        "bull-like": "taurine",
        "ox-like": "taurine",
        "tiger-like": "tigrine",
        "wasp-like": "vespine",
        "viper-like": "viperine",
        "calf-like": "vituline",
        "veal-like": "vituline",
        "mongoose-like": "viverrine",
        "fox-like": "vulpine",
        "vulture-like": "vulturine",
        "zebra-like": "zebrine",
        "sable-like": "zibeline",
    }),
    "terms.animal_adjectives.garner",
    "There's a word for this: '{}'.",
)


def register_with(registry: CheckRegistry) -> None:
    """Register the check."""
    registry.register(check)

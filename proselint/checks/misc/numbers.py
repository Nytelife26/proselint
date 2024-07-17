"""
Numbers at the beginning of a sentence and up to 10 should be spelled out.

---
layout:     post
source:
source_url: https://www.sciencewrites.org/dos-and-donts
title:      number_spell
date:       2024-01-14
categories: writing
---


"""

from __future__ import annotations

from proselint.checks import CheckSpec, ExistenceSimple

examples_pass = [
    "Smoke phrase with nothing flagged.",
    "It can vary by 9\xa0dB between locations.",
    "With a 1\xa0s duration.",
    "In a lake at a 5\xa0m distance.",
    "A Google Pixel\xa04, a OnePlus\xa08\xa0Pro, "
    "and a Samsung Galaxy Watch\xa04.",  # uses non-break space
    "Subjects distanced by 2\xa0m.",
    "There is a high noise amplitude below 1\xa0kHz,",
    "as observed variation of 9\xa0dB can be attributed",
    "because (1) smaller spacing and (2) something else",
    "In Fig. 3 we see the frequency response of the chirp.",
    "In Fig.\xa03 we see the frequency response of the chirp.",
    "1 INTRODUCTION",
    "2 Foreground: CHARACTERISTICS OF MOBILE DEVICES IN WATER",
    "3 BACKGROUND: CHARACTERISTICS OF MOBILE DEVICES IN WATER",
    "The preamble is composed of eight OFDM symbols from 1 to 4 kHz.",
]

examples_fail = [
    "remainder of only 7 symbol",
    "A Google Pixel 4, a OnePlus 8 Pro, and a Samsung Galaxy Watch 4.",
]

# src = https://www.sciencewrites.org/dos-and-donts
check_section = CheckSpec(
    # - starts with newline
    # - look for number, can have punctuation
    # - must be also a sentence (7 chars & end with punctuation) in same line
    # - \v\r\n is a fix, as python does not seem to honor vertical whitespace \v
    ExistenceSimple(r"^\d+(?:\.\d+)?\s[^\v\r\n\.!\?]{7,}[\.!\?]"),
    "misc.numbers.newline",
    "It is untidy to open sentences with a digit here '{}'. Spell it out, "
    "add a unit, or use decimal places.",
)

# src = https://www.sciencewrites.org/dos-and-donts
check_sentence = CheckSpec(
    # regex = r"[\.!\?]\s[0-9]+[\.\s]"  # too many false positive
    # - start at end of last sentence
    # - look for number, can have punctuation
    # - must be also a sentence (7 chars & end with punctuation) in same line
    ExistenceSimple(
        r"\b\w+[\.!\?] \d+(?:\.\d+)?\s[^\v\.!\?]{7,}[\.!\?]",
        # TODO: sync the exceptions with misc.punctuation
        exceptions=(
            r"al\.",
            r"lat\.",
            r"vs\.",
            r"etc\.",
            r"Prof\.",
            r"Dr\.",
            r"[vV]ol\.",
            r"[fF]ig\.",
        ),
    ),
    "misc.numbers.sentence",
    "It is untidy to open sentences with a digit here '{}'. Spell it out, "
    "add a unit, or use decimal places.",
)

# src = https://www.sciencewrites.org/dos-and-donts
check_single_digit = CheckSpec(
    # looks for single digit in separate in text (not at beginning of sentence)
    # but not part of "x to y"
    # TODO: reduce false positives from numbers with unit but no decimal point
    ExistenceSimple(r"(?<![\.!\?]) [0-9][ \.!\?](?!to \d+)"),
    "misc.numbers.single_digit",
    "It is bad style to use single-digit numbers as numerals "
    "here '{}'. Spell it out or use a non-breaking space (U+00A0) if it is "
    "part of a name.",
)

__register__ = (
    check_section,
    check_section,
    check_single_digit,
)

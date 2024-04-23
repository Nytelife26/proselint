"""Redundancy."""

from __future__ import annotations

from proselint.checks import Pd
from proselint.checks import CheckResult
from proselint.checks import preferred_forms_check_opti
from proselint.checks import preferred_forms_check_regex

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The table was rectangular in shape.",
    "It was blatantly obvious what to do next.",
    "Taking the package was absolutely essential.",
    "He often repeated the old adage.",
    "So much stuff and etc.",
    "Associate together in groups.",
]


def check(text: str) -> list[CheckResult]:
    """Suggest the preferred forms."""
    err = "redundancy.wallace"
    msg = "Redundancy. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "rectangular in shape": "rectangular",
        "audible to the ear": "audible",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_garner(text: str) -> list[CheckResult]:
    """Suggest the preferred forms.

    source:     Garner's Modern American Usage
    source_url: http://bit.ly/1T4alrY
    """
    err = "redundancy.garner"
    msg = "Redundancy. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "adequate enough": "adequate",
        "self-admitted": "admitted",
        "sworn affidavit": "affidavit",
        "mutual agreement": "agreement",
        "former alumnus": "alumnus",
        "directly antithetical": "antithetical",
        "approximately about": "approximately",
        "temporary bivouac": "bivouac",
        "bivouac camp": "bivouac",
        "blend together": "blend",
        "but nevertheless": "but",
        "accused of a charge": "charged with...",
        "circumstances surrounding": "circumstances of",
        "surrounding circumstances": "circumstances",
        "close proximity": "close",
        "collaborate together": "collaborate",
        "fellow collaborator": "collaborator",
        "fellow collaborators": "collaborators",
        "collocated together": "collocated",
        "fellow colleagues": "colleagues",
        "combine together": "combine",
        "self-complacent": "complacent",
        "self-confessed": "confessed",
        "connect together": "connect",
        "consolidate together": "consolidate",
        "still continues to": "continues to",
        "mutually contradictory": "contradictory",
        "mutual cooperation": "cooperation",
        "couple together": "couple",
        "serious crisis": "crisis",
        "entirely eliminate": "eliminate",
        "most especially": "especially",
        "actual fact": "fact",
        "true facts": "facts",
        "future forecast": "forecast",
        "founding forefathers": "founding fathers",
        "free and gratis": "free",
        "free gratis": "free",
        "completely full": "full",
        "basic fundamentals": "fundamentals",
        "free gift": "gift",
        "new innovation": "innovation",
        "interact with each other": "interact",
        "large-size": "large",
        "meld together": "meld",
        "merge together": "merge",
        "mingle together": "mingle",
        "mix together": "mix",
        "mutual feelings for eachother": "mutual feelings",
        "mutual respect for each other": "mutual respect",
        "native-born citizen": "native citizen",
        "absolute necessity": "necessity",
        "blatantly obvious": "obvious",
        "pause for a moment": "pause",
        "advance planning": "planning",
        "future plans": "plans",
        "pooled together": "pooled",
        "potable drinking water": "potable water",
        "new recruit": "recruit",
        "reelected for another term": "reelected",
        "refer back": "refer",
        "regress back": "regress",
        "repay them back": "repay them",
        "repay back": "repay",
        "repeat again": "repeat",
        "repeat back": "repeat",
        "repeat the same": "repeat",
        "repeated the same": "repeated",
        "temporary reprieve": "reprieve",
        "brief respite": "respite",
        "retiral": "retirement",
        "retiracy": "retirement",
        "retreat back": "retreat",
        "return back": "return",
        "closely scrutinize": "scrutinize",
        "software program": "software",
        "surrounded on all sides": "surrounded",
        "the whole entire nation": "the nation",
        "throughout the entire": "throughout the",
        "timpani drum": "timpani",
        "pair of twins": "twins",
        "unfilled vacancy": "vacancy",
        "various different": "various",
        "former veteran": "veteran",
        "visible to the eye": "visible",
        "professional vocation": "vocation",
        "while at the same time": "while",
    }
    ret1 = preferred_forms_check_opti(text, items, err, msg)

    items_regex = {
        r"(?:general )?consensus of opinion": "consensus",
        r"associate together(?: in groups)?": "associate",
    }
    ret2 = preferred_forms_check_regex(text, items_regex, err, msg)

    return ret1 + ret2


def check_nordquist(text: str) -> list[CheckResult]:
    """Suggest the preferred forms.

    source:     Richard Nordquist
    source_url: http://grammar.about.com/bio/Richard-Nordquist-22176.htm
    """
    err = "redundancy.nordquist"
    msg = "Redundancy. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "absolutely essential": "essential",
        "absolutely necessary": "necessary",
    }
    ret1 = preferred_forms_check_opti(text, items, err, msg)

    items_regex: dict[str, str] = {
        r"a\.m\. in the morning": "a.m.",
        r"p\.m\. at night": "p.m.",
    }
    ret2 = preferred_forms_check_regex(text, items_regex, err, msg)

    return ret1 + ret2


def check_atd_1(text: str) -> list[CheckResult]:
    """Check for redundancies from After the Deadline.

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "redundancy.after_the_deadline"
    msg = "Redundancy. Use '{}' instead of '{}'."

    items: dict[str, str] = {
        "Bo Staff": "Bō",
        "Challah bread": "Challah",
        "Hallah bread": "Hallah",
        "I myself": "I",
        "I personally": "I",
        "Mount Fujiyama": "Mount Fuji",
        "Milky Way galaxy": "Milky Way",
        "Rio Grande river": "Rio Grande",
        "old adage": "adage",
        "add a further": "add",
        "add an additional": "add",
        "advance forward": "advance",
        "alternative choice": "alternative",
        "amaretto almond": "amaretto",
        "completely annihilate": "annihilate",
        "annual anniversary": "anniversary",
        "unnamed anonymous": "anonymous",
        "equally as": "as",
        "ascend up": "ascend",
        "ask the question": "ask",
        "assemble together": "assemble",
        "at the present time the": "at present the",
        "at this point in time": "at this point",
        "attach together": "attach",
        "autumn season": "autumn",
        "bald-headed": "bald",
        "balsa wood": "balsa",
        "personal belongings": "belongings",
        "desirable benefits": "benefits",
        "bento box": "bento",
        "best ever": "best",
        "tiny bit": "bit",
        "blend together": "blend",
        "common bond": "bond",
        "added bonus": "bonus",
        "extra bonus": "bonus",
        "bouquet of flowers": "bouquet",
        "major breakthrough": "breakthrough",
        "new bride": "bride",
        "brief in duration": "brief",
        "bruin bear": "bruin",
        "burning hot": "hot",
        "cacophony of sound": "cacophony",
        "brief cameo": "cameo",
        "cameo appearance": "cameo",
        "cancel out": "cancel",
        "cash money": "cash",
        "chai tea": "chai",
        "random chance": "chance",
        "personal charm": "charm",
        "circle around": "circle",
        "round circle": "circle",
        "circulate around": "circulate",
        "classify into groups": "classify",
        "fellow classmates": "classmates",
        "old cliche": "cliche",
        "overused cliche": "cliche",
        "climb up": "climb",
        "time clock": "clock",
        "collaborate together": "collaborate",
        "joint collaboration": "collaboration",
        "fellow colleague": "colleague",
        "combine together": "combine",
        "commute back and forth": "commute",
        "compete with each other": "compete",
        "comprise of": "comprise",
        "comprises of": "comprises",
        "first conceived": "conceived",
        "final conclusion": "conclusion",
        "confer together": "confer",
        "direct confrontation": "confrontation",
        # "confused state": "confused",
        "connect together": "connect",
        "connect up": "connect",
        "consensus of opinion": "consensus",
        "general consensus": "consensus",
        "consult with": "consult",
        "oral conversation": "conversation",
        "cool down": "cool",
        "cooperate together": "cooperate",
        "mutual cooperation": "cooperation",
        "duplicate copy": "copy",
        "inner core": "core",
        "cost the sum of": "cost",
        "could possibly": "could",
        "money-saving coupon": "coupon",
        "originally created": "created",
        "crisis situation": "crisis",
        "crouch down": "crouch",
        "now currently": "currently",
        "old custom": "custom",
        "usual custom": "custom",
        "serious danger": "danger",
        "dates back": "dates",
        "definite decision": "decision",
        "depreciate in value": "depreciate",
        "descend down": "descend",
        "totally destroy": "destroy",
        "completely destroyed": "destroyed",
        "total destruction": "destruction",
        "specific details": "details",
        "difficult dilemma": "dilemma",
        "disappear from sight": "disappear",
        "originally discovered": "discovered",
        "dive down": "dive",
        "over and done with": "done",
        "illustrated drawing": "drawing",
        "drop down": "drop",
        "sand dune": "dune",
        "during the course of": "during",
        "dwindle down": "dwindle",
        "dwindled down": "dwindled",
        "each and every": "every",
        "earlier in time": "earlier",
        "completely eliminate": "eliminate",
        "eliminate altogether": "eliminate",
        "entirely eliminate": "eliminate",
        "glowing ember": "ember",
        "burning embers": "embers",
        "emergency situation": "emergency",
        "unexpected emergency": "emergency",
        "empty out": "empty",
        "enclosed herein": "enclosed",
        "final end": "end",
        "completely engulfed": "engulfed",
        "enter in": "enter",
        "enter into": "enter",
        "equal to one another": "equal",
        "eradicate completely": "eradicate",
        "absolutely essential": "essential",
        "estimated at about": "estimated at",
        "estimated at approximately": "estimated at",
        "estimated at around": "estimated at",
        "evolve over time": "evolve",
        "over exaggerate": "exaggerate",
        "exited from": "exited",
        "actual experience": "experience",
        "past experience": "experience",
        "knowledgeable experts": "experts",
        "extradite back": "extradite",
        "face up to the consequences": "face the consequences",
        "face up to the fact": "face the fact",
        "face up to the challenge": "face the challenge",
        "face up to the problem": "face the problem",
        "facilitate easier": "facilitate",
        "established fact": "fact",
        "actual facts": "facts",
        "hard facts": "facts",
        "true facts": "facts",
        "passing fad": "fad",
        "fall down": "fall",
        "fall season": "fall",
        "major feat": "feat",
        "feel inside": "feel",
        "inner feelings": "feelings",
        "few in number": "few",
        "completely filled": "filled",
        "filled to capacity": "filled",
        "first of all": "first",
        "first time ever": "first time",
        "closed fist": "fist",
        "fly through the air": "fly",
        "focus in": "focus",
        "main focus": "focus",
        "follow after": "follow",
        "as for example": "for example",
        # "first and foremost": "foremost",
        "forever and ever": "forever",
        "for free": "free",
        "personal friend": "friend",
        "personal friendship": "friendship",
        "full to capacity": "full",
        "basic fundamentals": "fundamentals",
        "fuse together": "fuse",
        "gather together": "gather",
        "gather up": "gather",
        "get up on his feet": "get up",
        "get up on your feet": "get up",
        "free gift": "gift",
        "free gifts": "gifts",
        "ultimate goal": "goal",
        # "former graduate": "graduate",
        "grow in size": "grow",
        "absolute guarantee": "guarantee",
        "armed gunman": "gunman",
        "armed gunmen": "gunmen",
        "native habitat": "habitat",
        "had done previously": "had done",
        "two equal halves": "halves",
        # "has got": "has",
        # "have got": "have",
        "safe haven": "haven",
        # "he himself": "he",
        "heat up": "heat",
        "past history": "history",
        "hoist up": "hoist",
        "empty hole": "hole",
        "head honcho": "honcho",
    }

    return preferred_forms_check_opti(text, items, err, msg)


def check_atd_2(text: str) -> list[CheckResult]:
    """Check for redundancies from After the Deadline.

    NOTE: this was one of the slowest Checks,
      so it was segmented to even the load for parallelization
    """
    err = "redundancy.after_the_deadline"
    msg = "Redundancy. Use '{}' instead of '{}'."

    items = {
        "12 noon": "noon",
        "12 o'clock noon": "noon",
        "absolutely necessary": "necessary",
        "absolutely sure": "sure",
        "advance planning": "planning",
        "advance preview": "preview",
        "advance reservations": "reservations",
        "advance warning": "warning",
        "affirmative yes": "yes",
        "all inclusive": "inclusive",
        "anonymous stranger": "stranger",
        "artificial prosthesis": "prosthesis",
        # "bare naked": "naked",
        "boat marina": "marina",
        "brief moment": "moment",
        "careful scrutiny": "scrutiny",
        # "close proximity": "proximity",
        "close scrutiny": "scrutiny",
        "complete monopoly": "monopoly",
        "completely surround": "surround",
        "constantly maintained": "maintained",
        "continue to remain": "remain",
        "exact opposite": "opposite",
        "exact opposites": "opposites",
        "exact replica": "replica",
        "exact same": "same",
        "exposed opening": "opening",
        "final outcome": "outcome",
        "final ultimatum": "ultimatum",
        "foreign imports": "imports",
        "former veteran": "veteran",
        "forward planning": "planning",
        "frozen ice": "ice",
        "frozen tundra": "tundra",
        "full satisfaction": "satisfaction",
        "future plan": "plan",
        "future plans": "plans",
        "future recurrence": "recurrence",
        "harmful injuries": "injuries",
        "high noon": "noon",
        # "highly relevant": "relevant",
        "honest truth": "truth",
        "hot water heater": "water heater",
        "in actual fact": "in fact",
        "in which we live in": "in which we live",
        "incredible to believe": "incredible",
        # "indicted on a charge": "indicted",
        "innovative new": "innovative",
        # "input into": "input",
        "integrate together": "integrate",
        "integrate with each other": "integrate",
        "interdependent on each other": "interdependent",
        "introduced for the first time": "introduced",
        "kneel down": "kneel",
        "knots per hour": "knots",
        # "last of all": "last",
        # "later time": "later",
        "lift up": "lift",
        "live studio audience": "studio audience",
        "live witness": "witness",
        "look ahead to the future": "look to the future",
        "manually by hand": "manually",
        "may possibly": "may",
        "meet together": "meet",
        "meet with each other": "meet",
        "mental telepathy": "telepathy",
        "merge together": "merge",
        "merged together": "merged",
        "meshed together": "meshed",
        "migraine headache": "migraine",
        "minestrone soup": "minestrone",
        "mix together": "mix",
        "moment in time": "moment",
        "mutual respect for each other": "mutual respect",
        "mutually dependent on each other": "mutually dependent",
        "mutually interdependent": "interdependent",
        "my personal opinion": "my opinion",
        "nape of her neck": "nape",
        "natural instinct": "instinct",
        "naturally instinct": "instinct",
        # "necessary requirements": "requirements",
        "never at any time": "never",
        "new innovation": "innovation",
        "new innovative": "innovative",
        "new invention": "invention",
        "nostalgia for the past": "nostalgia",
        "now pending": "pending",
        "number of different": "number of",
        "old pioneer": "pioneer",
        "old proverb": "proverb",
        "open trench": "trench",
        "orbits around": "orbits",
        "outside in the yard": "in the yard",
        "past memories": "memories",
        "penetrate through": "penetrate",
        "perfect ideal": "ideal",
        "plan ahead": "plan",
        "plan in advance": "plan",
        "point in time": "point",
        "polar opposite": "opposite",
        "polar opposites": "opposites",
        "positive identification": "identification",
        "postpone until later": "postpone",
        "pouring down rain": "pouring rain",
        "precise same": "same",
        "present incumbent": "incumbent",
        "previously listed above": "previously listed",
        "private industry": "industry",
        "probed into": "probed",
        "proceed ahead": "proceed",
        "proposed plan": "plan",
        # "protrude out": "protrude",
        "put off until later": "put off",
        # "raise up": "raise",
        "rate of speed": "speed",
        "re-elect for another term": "re-elect",
        "reason is because": "reason is",
        "recur again": "recur",
        "refer back": "refer",
        "reflect back": "reflect",
        "reply back": "reply",
        "retreat back": "retreat",
        "revert back": "revert",
        "rough rule of thumb": "rule of thumb",
        "round in shape": "round",
        "rustic country": "rustic",
        "safe sanctuary": "sanctuary",
        "same exact": "same",
        "same identical": "identical",
        "scrutinize in detail": "scrutinize",
        "secret that cannot be told": "secret",
        "seek to find": "seek",
        "separated apart from each other": "separated",
        "share together": "share",
        "sharp point": "point",
        "shiny in appearance": "shiny",
        "sink down": "sink",
        "skipped over": "skipped",
        # "slow speed": "slow",
        # "small size": "small",
        "small speck": "speck",
        "soft in texture": "soft",
        "soft to the touch": "soft",
        "sole of the foot": "sole",
        "some time to come": "some time",
        "spell out in detail": "spell out",
        "spiked upward": "spiked",
        "spiked upwards": "spiked",
        "spring season": "spring",
        "still lingers": "lingers",
        "still persists": "persists",
        "still remains": "remains",
        "sudden impulse": "impulse",
        "sufficient enough": "sufficient",
        "summer season": "summer",
        "surrounded on all sides": "surrounded",
        "tall in height": "tall",
        "tall in stature": "tall",
        "ten in number": "ten",
        "these ones": "these",
        # "they themselves": "they",
        "those ones": "those",
        "three-way love triangle": "love triangle",
        "truly sincere": "sincere",
        "twelve midnight": "midnight",
        "twelve noon": "noon",
        "unconfirmed rumor": "rumor",
        # "undeniable truth": "undeniable",
        "undergraduate student": "undergraduate",
        "underground subway": "subway",
        "unexpected surprise": "surprise",
        # "unintentional mistake": "unintentional",
        "universal panacea": "panacea",
        "unsolved mystery": "mystery",
        "vacillate back and forth": "vacillate",
        "visible to the eye": "visible",
        "wall mural": "mural",
        "warn in advance": "warn",
        "winter season": "winter",
        "yakitori chicken": "yakitori",
        "yerba mate tea": "yerba mate",
    }
    ret1 = preferred_forms_check_opti(text, items, err, msg)

    items_regex: dict[str, str] = {r"\band etc\.": "etc."}
    ret2 = preferred_forms_check_regex(text, items_regex, err, msg, padding=Pd.disabled)

    return ret1 + ret2

"""Words the NFL won't print on a jersey.

---
layout:     post
source:     The National Football League
source_url: http://bit.ly/1ISK0rb
title:      words the NFL won't print on a jersey
date:       2014-06-10
categories: writing
---

Words the NFL won't print on a jersey.

"""
from __future__ import annotations

from proselint.checks import ResultCheck, Pd
from proselint.checks import existence_check

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "The QB is named ball licker.",
    "The difference between femme and famme.",
    "Interracial is the word.",
    "you jackass, be funny.",
    "To rent a fuck or not to rent a fuck.",
]


def check_a_to_e(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "cursing.nfl"
    msg = "The NFL won't print this word on a jersey."

    items = [
        "420",
        "666",
        "2 on 1",
        "3rd eye",
        "3rd leg",
        "3rdeye",
        "3rdleg",
        "3some",
        "4 twenty",
        "4twenty",
        "60 nine",
        "60nine",
        "a.s.s.",
        "anal",
        "anal annie",
        "anal sex",
        "analannie",
        "analsex",
        "anus",
        "arse",
        "ass",
        "ass bagger",
        "ass blaster",
        "ass clown",
        "ass cowboy",
        "ass fuck",
        "ass fucker",
        "ass hole",
        "ass holes",
        "ass hore",
        "ass jockey",
        "ass kiss",
        "ass kisser",
        "ass klown",
        "ass lick",
        "ass licker",
        "ass lover",
        "ass man",
        "ass monkey",
        "ass munch",
        "ass muncher",
        "ass packer",
        "ass pirate",
        "ass puppies",
        "ass ranger",
        "ass whore",
        "ass wipe",
        "assbagger",
        "assblaster",
        "assclown",
        "asscowboy",
        "assfuck",
        "assfucker",
        "asshole",
        "assholes",
        "asshore",
        "assjockey",
        "asskiss",
        "asskisser",
        "assklown",
        "asslick",
        "asslicker",
        "asslover",
        "assman",
        "assmonkey",
        "assmunch",
        "assmuncher",
        "asspacker",
        "asspirate",
        "asspuppies",
        "assranger",
        "asswhore",
        "asswipe",
        "athletes foot",
        "athletesfoot",
        "axing the weasel",
        "b hard",
        "back door",
        "back door man",
        "backdoor",
        "backdoorman",
        "backseat",
        "bad ass",
        "bad fuck",
        "badfuck",
        "ball licker",
        "ball sack",
        "balllicker",
        "balls",
        "ballsack",
        "banging",
        "barely legal",
        "barelylegal",
        "barf",
        "barf face",
        "barface",
        "barfface",
        "bastard",
        "bazongas",
        "bazooms",
        "beastality",
        "beastiality",
        "beat off",
        "beat your meat",
        "beatoff",
        "beat-off",
        "beatyourmeat",
        "bi",
        "bi sexual",
        "biatch",
        "big ass",
        "big bitch",
        "big bitch",
        "big butt",
        "bigass",
        "bigbastard",
        "bigbutt",
        "bisexual",
        "bi-sexual",
        "bitch",
        "bitches",
        "bitchin",
        "bitchy",
        "bite me",
        "biteme",
        "black out",
        "blackout",
        "blow job",
        "blowjob",
        "bm",
        "boner",
        "bong",
        "boobies",
        "boobs",
        "boody",
        "breast",
        "breast job",
        "breast lover",
        "breast man",
        "breastjob",
        "breastlover",
        "breastman",
        "budweiser",
        "bull crap",
        "bull dike",
        "bull dyke",
        "bull shit",
        "bullcrap",
        "bulldike",
        "bulldyke",
        "bullshit",
        "bumble fuck",
        "bumblefuck",
        "bumfuck",
        "bunghole",
        "butch babes",
        "butch dike",
        "butch dyke",
        "butchbabes",
        "butchdike",
        "butchdyke",
        "butt bang",
        "butt fuck",
        "butt fucker",
        "butt fuckers",
        "butt head",
        "butt man",
        "butt plug",
        "butt stain",
        "buttbang",
        "butt-bang",
        "buttface",
        "buttfuck",
        "butt-fuck",
        "buttfucker",
        "butt-fucker",
        "buttfuckers",
        "butt-fuckers",
        "butthead",
        "buttman",
        "buttpirate",
        "buttplug",
        "buttstain",
        "camel toe",
        "cameltoe",
        "carpet muncher",
        "carpetmuncher",
        "carruth",
        "cherry popper",
        "cherrypopper",
        "chick slick",
        "chickslick",
        "clam digger",
        "clam diver",
        "clamdigger",
        "clamdiver",
        "clit",
        "clitoris",
        "cock",
        "cock block",
        "cock blocker",
        "cock cowboy",
        "cock fight",
        "cock knob",
        "cock licker",
        "cock lover",
        "cock nob",
        "cock queen",
        "cock rider",
        "cock smith",
        "cock sucker",
        "cock tail",
        "cock tease",
        "cockblock",
        "cockblocker",
        "cockcowboy",
        "cockfight",
        "cockhead",
        "cockknob",
        "cocklicker",
        "cocklover",
        "cocknob",
        "cockqueen",
        "cockrider",
        "cocks man",
        "cocksman",
        "cocksmith",
        "cocksucer",
        "cocksucker",
        "cocktail",
        "cocktease",
        "cocky",
        "condom",
        "copulate",
        "corn hole",
        "cornhole",
        "crabs",
        "crack",
        "crack pipe",
        "crack whore",
        "crackpipe",
        "crackwhore",
        "crack-whore",
        "crap",
        "crappy",
        "creamy",
        "crotch",
        "crotch jockey",
        "crotch monkey",
        "crotch rot",
        "crotchjockey",
        "crotchmonkey",
        "crotchrot",
        "cum",
        "cum bubble",
        "cum fest",
        "cum jockey",
        "cum quat",
        "cum queen",
        "cum shot",
        "cumbubble",
        "cumfest",
        "cumjockey",
        "cumm",
        "cumming",
        "cumquat",
        "cumqueen",
        "cumshot",
        "cunnilingus",
        "cunt",
        "cunt fuck",
        "cunt fucker",
        "cunt licker",
        "cuntfuck",
        "cuntfucker",
        "cuntlicker",
        "cyber sex",
        "cyber slimer",
        "cybersex",
        "cyberslimer",
        "dahmer",
        "damn",
        "damn it",
        "damnit",
        "datnigga",
        "dd",
        "deap throat",
        "deaper",
        "deapthroat",
        "deep throat",
        "deeper",
        "deepthroat",
        "defecate",
        "deposit",
        "devil",
        "dick brain",
        "dick fart",
        "dick for brains",
        "dick head",
        "dick lick",
        "dick licker",
        "dick likcer",
        "dick wad",
        "dick weed",
        "dickbrain",
        "dickforbrains",
        "dickhead",
        "dickless",
        "dicklick",
        "dicklicker",
        "dickman",
        "dickwad",
        "dickweed",
        "dike",
        "dildo",
        "dip stick",
        "dipstick",
        "dirty ho",
        "dix",
        "dixie dike",
        "dixie dyke",
        "dixiedike",
        "dixiedyke",
        "do me",
        "doggie style",
        "doggiestyle",
        "doggy stlye",
        "doggystyle",
        "dome",
        "dong",
        "dope",
        "double d",
        "doubled",
        "drag queen",
        "dragqueen",
        "dragqween",
        "dre",
        "drip dick",
        "dripdick",
        "drunk",
        "drunken",
        "dumb ass",
        "dumb bitch",
        "dumb fuck",
        "dumbass",
        "dumbbitch",
        "dumbfuck",
        "easy slut",
        "easyslut",
        "eat me",
        "eat pussy",
        "eatballs",
        "eatme",
        "eatpussy",
        "ejaculate",
        "erection",
        "evl",
        "excrement",
    ]
    return existence_check(text, items, err, msg)


def check_f_to_h(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "cursing.nfl"
    msg = "The NFL won't print this word on a jersey."

    items = [
        "f toyota",
        "f.i.n.e.",
        "f.u.c.k.",
        "face fucker",
        "facefucker",
        "faggot",
        "fagot",
        "fairy",
        "fanny fucker",
        "fannyfucker",
        "fart",
        "fast fuck",
        "fastfuck",
        "fat ass",
        "fat fuck",
        "fat fucker",
        "fatass",
        "fatfuck",
        "fatfucker",
        "fatso",
        "fellatio",
        "femme",
        "finger food",
        "finger fuck",
        "finger fucker",
        "fingerfood",
        "fingerfuck",
        "fingerfucker",
        "fist fuck",
        "fist fucker",
        "fistfuck",
        "fistfucker",
        "fisting",
        "flasher",
        "flatulence",
        "floggin the dolphin",
        "fondle",
        "foot fuck",
        "foot fucker",
        "foot licker",
        "footaction",
        "footfuck",
        "footfucker",
        "footlicker",
        "footstar",
        "fore skin",
        "foreskin",
        "fornicate",
        "four 20",
        "four twenty",
        "four20",
        "fourtwenty",
        "freak fuck",
        "freakfuck",
        "freaky fucker",
        "freakyfucker",
        "free 4 all",
        "free for all",
        "free fuck",
        "free4all",
        "freeforall",
        "freefuck",
        "fuck",
        "fuck bag",
        "fuck buddy",
        "fuck face",
        "fuck fest",
        "fuck freak",
        "fuck friend",
        "fuck head",
        "fuck her",
        "fuck it",
        "fuck knob",
        "fuck me",
        "fuck me hard",
        "fuck monkey",
        "fuck off",
        "fuck pig",
        "fuck them",
        "fuck whore",
        "fuck you",
        "fucka",
        "fuckable",
        "fuckbag",
        "fuckbuddy",
        "fucked",
        "fucked up",
        "fuckedup",
        "fucker",
        "fuckers",
        "fuckface",
        "fuckfest",
        "fuckfreak",
        "fuckfriend",
        "fuckhead",
        "fuckher",
        "fuckin",
        "fuckin a",
        "fuckin nuts",
        "fuckin right",
        "fuckina",
        "fucking",
        "fucking a",
        "fucking bitch",
        "fucking nuts",
        "fuckingbitch",
        "fuckinnuts",
        "fuckinright",
        "fuckit",
        "fuckknob",
        "fuckme",
        "fuckmehard",
        "fuckmonkey",
        "fuckoff",
        "fuckpig",
        "fuckwhore",
        "fuckyou",
        "fudge pakcers",
        "fun fuck",
        "funfuck",
        "fuuck",
        "g unit",
        "gang bang",
        "gang banger",
        "gangbang",
        "gangbanger",
        "gay",
        "gay ass",
        "gay mutha fuckin queer",
        "gay pride",
        "gaymuthafuckinwhore",
        "genital",
        "get it on",
        "getiton",
        "giehn",
        "give head",
        "givehead",
        "glazed donut",
        "glazeddonut",
        "go me",
        "go to hell",
        "god",
        "god damed mutha fucka",
        "god damit",
        "god damn",
        "god damned",
        "god manit",
        "goddamit",
        "goddamn",
        "goddamned",
        "goddamnes",
        "goddamnit",
        "goddamnmuthafucker",
        "gonorrehea",
        "gonzagas",
        "gook",
        "got jesus",
        "got2haveit",
        "gotohell",
        "g-unit",
        "hand job",
        "handjob",
        "hard on",
        "harder",
        "hardon",
        "harem",
        "he hate me",
        "head fuck",
        "head lights",
        "headfuck",
        "headlights",
        "hehateme",
        "hell",
        "hell no",
        "hell yes",
        "hellno",
        "hellyes",
        "hen house",
        "henhouse",
        "herpes",
        "hershey hi way",
        "hersheyhighway",
        "hersheyhiway",
        "hershy high way",
        "ho",
        "ho mo",
        "hobo",
        "hole",
        "hole stuffer",
        "holestuffer",
        "homo",
        "homo bangers",
        "homo sexual",
        "homobangers",
        "homosexual",
        "honkers",
        "honkey",
        "hooker",
        "hookers",
        "hooters",
        "hore",
        "horney",
        "horny",
        "horseshit",
        "hose job",
        "hosejob",
        "hoser",
        "hostage",
        "hot damn",
        "hot pussy",
        "hot to trot",
        "hot2trot",
        "hotdamn",
        "hotpussy",
        "hottotrot",
        "hussy",
        "hustler",
    ]
    return existence_check(text, items, err, msg, padding=Pd.sep_in_txt)
    # TODO: can't be padding=Pd.words_in_txt because of f.u.c.k.
    # TODO: monkeypatch _check() and test for that!


def check_i_to_p(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "cursing.nfl"
    msg = "The NFL won't print this word on a jersey."

    items = [
        "i love beer",
        "i luv beer",
        "id ten t",
        "id10t",
        "idiot",
        "idoit",
        "in the ass",
        "in the buff",
        "ingin",
        "insest",
        "inter course",
        "inter racial",
        "intercourse",
        "interracial",
        "intheass",
        "inthebuff",
        "jack the ripper",
        "jackass",
        "jackoff",
        "jacktheripper",
        "jap",
        "jap crap",
        "japcrap",
        "jerk off",
        "jerkoff",
        "jesus chirst",
        "jesuschrist",
        "jism",
        "jiz",
        "jiz juice",
        "jizim",
        "jizjuice",
        "jizz",
        "jizzim",
        "joint",
        "juggalo",
        "jugs",
        "k mart",
        "kill",
        "killer",
        "killing",
        "kiss ass",
        "kissass",
        "kkk",
        "kmart",
        "knockers",
        "koon",
        "kotex",
        "krap",
        "krappy",
        "kum",
        "kum bubble",
        "kum quat",
        "kumbubble",
        "kumbullbe",
        "kumquat",
        "kunt",
        "ky",
        "ky jelly",
        "lactate",
        "lady boog",
        "laid",
        "lap dance",
        "lapdance",
        "lesbain",
        "lesbayn",
        "lesbian",
        "lesbin",
        "lesbo",
        "lez",
        "lez be",
        "lez be friends",
        "lezbe",
        "lezbefriends",
        "lezbo",
        "lezz",
        "lezzo",
        "lick me",
        "licker",
        "lickme",
        "limp dick",
        "limpdick",
        "limy",
        "live sex",
        "livesex",
        "loaded gun",
        "loadedgun",
        "lolita",
        "looser",
        "lotion",
        "love bone",
        "love goo",
        "love gun",
        "love juice",
        "love muscle",
        "love pistol",
        "love rocket",
        "lovebone",
        "lovegoo",
        "lovegun",
        "lovejuice",
        "lovemuscle",
        "lovepistol",
        "loverocket",
        "low life",
        "lowlife",
        "lube job",
        "lubejob",
        "lucky camel toe",
        "luckycammeltoe",
        "magic wand",
        "magicwand",
        "mams",
        "man hater",
        "man paste",
        "manhater",
        "manpaste",
        "mary jane",
        "maryjane",
        "mastabate",
        "mastabater",
        "master blaster",
        "masterbate",
        "masterblaster",
        "mastrabator",
        "mattress princess",
        "mattressprincess",
        "meat beatter",
        "meatbeatter",
        "molest",
        "molester",
        "molestor",
        "money shot",
        "moneyshot",
        "mother fucker",
        "mother love bone",
        "motherfuck",
        "motherfucker",
        "motherlovebone",
        "muff",
        "muff dive",
        "muff diver",
        "muff licker",
        "muffdive",
        "muffdiver",
        "muffin diver",
        "muffindiver",
        "mufflikcer",
        "murder",
        "mutha fucker",
        "naked",
        "nasty bitch",
        "nasty ho",
        "nasty slut",
        "nasty whore",
        "nastybitch",
        "nastyho",
        "nastyslut",
        "nastywhore",
        "neon deon",
        "nig",
        "niger",
        "nigga",
        "nigger",
        "nipple",
        "nipple ring",
        "nipplering",
        "nit tit",
        "nittit",
        "no fucking way",
        "no sex",
        "nofuckingway",
        "nookie",
        "nooner",
        "nude",
        "nut fucker",
        "nutfucker",
        "oicu812",
        "on the rag",
        "ontherag",
        "orgasm",
        "orgy",
        "ou812",
        "oui",
        "p i m p",
        "pearl necklace",
        "pearlnecklace",
        "pecker",
        "pee",
        "peep show",
        "peepshow",
        "peepshpw",
        "penetration",
        "penis",
        "penthouse",
        "period",
        "phque",
        "pimp",
        "pimp simp",
        "pimped",
        "pimper",
        "pimpjuic",
        "pimpjuice",
        "pimpsimp",
        "piss",
        "piss head",
        "pissed",
        "pisser",
        "pisshead",
        "play boy",
        "play girl",
        "playboy",
        "playgirl",
        "pocket pool",
        "pocketpool",
        "polack",
        "poon tang",
        "poontang",
        "poop",
        "pooper",
        "poor white trash",
        "poorwhitetrash",
        "popimp",
        "porch monkey",
        "porchmonkey",
        "porn",
        "porn flick",
        "porn king",
        "porn princess",
        "pornflick",
        "pornking",
        "porno",
        "pornprincess",
        "pot",
        "premature",
        "prick",
        "prick head",
        "prickhead",
        "primetime",
        "prostitute",
        "pubic",
        "pubic lice",
        "pubiclice",
        "pud",
        "pud boy",
        "pudboy",
        "pudd",
        "pudd boy",
        "puddboy",
        "pun tang",
        "puntang",
        "purina princess",
        "purinapricness",
        "pussy",
        "pussy cat",
        "pussy eater",
        "pussy fucker",
        "pussy licker",
        "pussy lips",
        "pussy lover",
        "pussy pounder",
        "pussycat",
        "pussyeater",
        "pussyfucker",
        "pussylicker",
        "pussylips",
        "pussylover",
        "pussypounder",
        "putt pirate",
        "pwt",
    ]
    return existence_check(text, items, err, msg)


def check_q_to_z(text: str) -> list[ResultCheck]:
    """Check the text."""
    err = "cursing.nfl"
    msg = "The NFL won't print this word on a jersey."

    items = [
        "queef",
        "queer",
        "quickie",
        "rae carruth",
        "rape",
        "rapist",
        "rear end",
        "rear entry",
        "rearend",
        "rearentry",
        "rectum",
        "red light",
        "redlight",
        "reefer",
        "rent a fuck",
        "rentafuck",
        "retard",
        "retarded",
        "ribbed",
        "rim job",
        "rimjob",
        "roach",
        "robber",
        "s and m",
        "s&m",
        "samckdaddy",
        "sandm",
        "satan",
        "schlong",
        "screw",
        "screw you",
        "screwyou",
        "scrotum",
        "semen",
        "sex",
        "sex farm",
        "sex hound",
        "sex house",
        "sex kitten",
        "sex pot",
        "sex slave",
        "sex to go",
        "sex toy",
        "sex toys",
        "sex whore",
        "sexfarm",
        "sexhound",
        "sexhouse",
        "sexkitten",
        "sexpot",
        "sexslave",
        "sextogo",
        "sextoy",
        "sextoys",
        "sexual",
        "sexwhore",
        "sexy",
        "sexy biatch",
        "sexy bitch",
        "sexy moma",
        "sexy slim",
        "sexymoma",
        "sexy-slim",
        "shag",
        "shaggin",
        "shagging",
        "shawtypimp",
        "shit",
        "shit dick",
        "shit eater",
        "shit face",
        "shit for brains",
        "shit fuck",
        "shit fucker",
        "shit happens",
        "shit head",
        "shit out of luck",
        "shit stain",
        "shit4brains",
        "shitdick",
        "shiteater",
        "shitface",
        "shitforbrains",
        "shitfuck",
        "shitfucker",
        "shithapens",
        "shithappens",
        "shithead",
        "shitoutofluck",
        "shits",
        "shitstain",
        "shitter",
        "shitting",
        "shitty",
        "short fuck",
        "shortfuck",
        "showtime",
        "six six six",
        "sixsixsix",
        "sixty 9",
        "sixty nine",
        "sixty9",
        "sixtynine",
        "skank",
        "skank bitch",
        "skank fuck",
        "skank whore",
        "skankbitch",
        "skankfuck",
        "skankwhore",
        "skanky bitch",
        "skanky whore",
        "skankybitch",
        "skankywhore",
        "skin flute",
        "skinflute",
        "skum",
        "skum bag",
        "skumbag",
        "slant",
        "slant eye",
        "slanteye",
        "slave",
        "slave driver",
        "slavedriver",
        "sleeze bag",
        "sleeze ball",
        "sleezebag",
        "sleezeball",
        "slide it in",
        "slideitin",
        "slime",
        "slime ball",
        "slime bucket",
        "slimeball",
        "slimebucket",
        "slut",
        "slut wear",
        "slut whore",
        "sluts",
        "slutt",
        "slutting",
        "slutty",
        "slutwear",
        "slutwhore",
        "smack daddy",
        "smack the monkey",
        "smackthemonkey",
        "smagma",
        "smart ass",
        "snatch",
        "snatch patch",
        "snatchpatch",
        "sniper",
        "snot",
        "sob",
        "sodomite",
        "sodomy",
        "son of a bitch",
        "sonofabitch",
        "sonofbitch",
        "spank the monkey",
        "spankthemonkey",
        "sperm",
        "sperm bag",
        "sperm hearder",
        "sperm herder",
        "spermacide",
        "spermbag",
        "spermhearder",
        "spermherder",
        "spic",
        "spick",
        "spit",
        "spitter",
        "split tail",
        "split tial",
        "splittail",
        "stagg",
        "strap on",
        "strapon",
        "stringer",
        "strip club",
        "stripclub",
        "stroke",
        "stroking",
        "stupid",
        "stupid fuck",
        "stupid fucker",
        "stupidfuck",
        "stupidfucker",
        "suck",
        "suck dick",
        "suck me",
        "suck my ass",
        "suck my dick",
        "suck my tit",
        "suck off",
        "suckdick",
        "sucker",
        "suckme",
        "suckmyass",
        "suckmydick",
        "suckmytit",
        "suckoff",
        "suicide",
        "swallow",
        "swallower",
        "swalow",
        "sweetness",
        "swign dixx",
        "swing dixx",
        "swingin dixx",
        "swinging dicks",
        "syphilis",
        "tampon",
        "tang",
        "testicle",
        "testicles",
        "third eye",
        "third leg",
        "thirdeye",
        "thirdleg",
        "three some",
        "threesome",
        "tit",
        "tit bit nipply",
        "tit fuck",
        "tit fucker",
        "tit fuckin",
        "tit job",
        "tit licker",
        "tit lover",
        "titbitnipply",
        "titfuck",
        "titfucker",
        "titfuckin",
        "titjob",
        "titlicker",
        "titlover",
        "tits",
        "titties",
        "titty",
        "toilet",
        "toilet bowl",
        "tongethruster",
        "tongue",
        "tongue thruster",
        "tongue tramp",
        "tonguethrust",
        "tonguetramp",
        "toung thruster",
        "tounge baller",
        "tounge thrust",
        "trailer trash",
        "trailertrash",
        "tramp",
        "tri sexual",
        "triple x",
        "triplex",
        "trisexual",
        "trojan",
        "trots",
        "tunnel of love",
        "tunneloflove",
        "turd",
        "two bit whore",
        "two on one",
        "twobitwhore",
        "unfuckable",
        "up the ass",
        "up the butt",
        "upskirt",
        "uptheass",
        "upthebutt",
        "urinate",
        "urine",
        "uterus",
        "vagina",
        "vaginal",
        "vd",
        "vibrater",
        "vibrator",
        "virgin",
        "virgin breaker",
        "virginbreaker",
        "vulva",
        "waysted",
        "weenie",
        "wet spot",
        "wetspot",
        "whacker",
        "whiskey dick",
        "whiskeydick",
        "whisky dick",
        "whiskydick",
        "white trash",
        "whitetrash",
        "whore",
        "whore fucker",
        "whore house",
        "whorefucker",
        "whorehouse",
        "wigger",
        "willie wanker",
        "williewanker",
        "wuutang",
        "xxx",
        "yellow man",
        "yellowman",
    ]

    return existence_check(text, items, err, msg)

"""Needless variants.

---
layout:     post
source:     Garner's Modern American Usage
source_url: http://bit.ly/1T4alrY
title:      needless variants
date:       2014-06-10
categories: writing
---

Points out use of needless variants.

"""
from __future__ import annotations

from typing import final

from proselint.checks import ResultCheck
from proselint.checks import preferred_forms_check
from proselint.checks import preferred_forms_check2_main
from proselint.checks import preferred_forms_check2_pre

examples_pass = [
    "Smoke phrase with nothing flagged.",
]

examples_fail = [
    "It was an extensible telescope.",
]


def check_1(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms.  # TODO: test for precalculating consts, see below

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "needless_variants.misc"
    msg = "'{1}' is a needless variant. '{0}' is the preferred form."

    preferences = [
        # Needless variants
        ["abolition", ["abolishment"]],
        ["accessory", ["accessary"]],
        ["accredit", ["accreditate"]],
        ["accrual", ["accruement"]],
        ["accumulate", ["cumulate"]],
        ["accused", ["accusee"]],
        ["acquaintance", ["acquaintanceship"]],
        ["acquittal", ["acquitment"]],
        ["administer", ["administrate"]],
        ["administered", ["administrated"]],
        ["administering", ["administrating"]],
        ["adulterous", ["adulterate"]],
        ["advisory", ["advisatory"]],
        ["advocate", ["advocator"]],
        ["alleger", ["allegator"]],
        ["allusive", ["allusory"]],
        ["ameliorate", ["meliorate"]],
        ["amorous", ["amative"]],
        ["amortization", ["amortizement"]],
        ["amphibology", ["amphiboly"]],
        ["anachronism", ["parachronism"]],
        ["anecdotist", ["anecdotalist"]],
        ["anilingus", ["anilinctus"]],
        ["anticipatory", ["anticipative"]],
        ["antithetical", ["antithetic"]],
        ["applicable", ["applicative"]],
        ["applicable", ["applicatory"]],
        ["applicator", ["applier"]],
        ["approbatory", ["approbative"]],
        ["arbitrageur", ["arbitrager"]],
        ["arsenious", ["arsenous"]],
        ["ascendancy", ["ascendance"]],
        ["ascendancy", ["ascendence"]],
        ["ascendancy", ["ascendency"]],
        ["authorial", ["auctorial"]],
        ["averment", ["averral"]],
        ["barbed wire", ["barbwire"]],
        ["beneficent", ["benefic"]],
        ["benign", ["benignant"]],
        ["bestowal", ["bestowment"]],
        ["betrothal", ["betrothment"]],
        ["blameworthiness", ["blamableness"]],
        ["buck naked", ["butt naked"]],
        ["captor", ["capturer"]],
        ["carte blanche", ["carta blanca"]],
        ["casualties", ["casualities"]],
        ["casualty", ["casuality"]],
        ["catch fire", ["catch on fire"]],
        ["catholically", ["catholicly"]],
        ["ceasefire", ["cease fire"]],
        ["cellphone", ["cell phone", "cell-phone"]],
        ["channel", ["channelize"]],
        ["chaplaincy", ["chaplainship"]],
        ["chrysalis", ["chrysalid"]],
        ["chrysalises", ["chrysalids"]],
        ["cigarette", ["cigaret"]],
        ["cliquish", ["cliquey", "cliquy"]],
        ["cognitive", ["cognitional"]],
        ["cohabit", ["cohabitate"]],
        ["cohabitant", ["cohabitor"]],
        ["collodion", ["collodium"]],
        ["collusive", ["collusory"]],
        ["commemorative", ["commemoratory"]],
        ["commonage", ["commonty"]],
        ["communicative", ["communicatory"]],
        ["compensatory", ["compensative"]],
        ["complacency", ["complacence"]],
        ["complicit", ["complicitous"]],
        ["compute", ["computate"]],
        ["comrade", ["camarade"]],
        ["conciliatory", ["conciliative"]],
        ["concomitance", ["concomitancy"]],
        ["condonation", ["condonance"]],
        ["confirmatory", ["confirmative"]],
        ["congruence", ["congruency"]],
        ["connote", ["connotate"]],
        ["consanguine", ["consanguineal"]],
        ["conspicuousness", ["conspicuity"]],
        ["conspirator", ["conspiratorialist"]],
        ["constitutionalist", ["constitutionist"]],
        ["contemporaneous", ["cotemporaneous"]],
        ["contemporary", ["cotemporary"]],
        ["contigency", ["contingence"]],
        ["contributory", ["contributary"]],
        ["contumacy", ["contumacity"]],
        ["convertible", ["conversible"]],
        ["conveyance", ["conveyal"]],
        ["corroborative", ["corroboratory"]],
        ["coworker", ["coemployee"]],
        ["curative", ["curatory"]],
        ["daredevilry", ["daredeviltry"]],
        ["deceptive", ["deceptious"]],
        ["defamatory", ["defamative"]],
        ["degenerative", ["degeneratory"]],
        ["delimit", ["delimitate"]],
        ["delusive", ["delusory"]],
        ["denunciation", ["denouncement"]],
        ["depositary", ["depositee"]],
        ["depreciatory", ["depreciative"]],
        ["deprivation", ["deprival"]],
        ["derogatory", ["derogative"]],
        ["destructible", ["destroyable"]],
        ["dethrone", ["disenthrone"]],
        ["detoxify", ["detoxicate"]],
        ["detractive", ["detractory"]],
        ["deuterogamy", ["digamy"]],
        ["deviance", ["deviancy"]],
        ["deviant", ["deviationist"]],
        ["digitize", ["digitalize"]],
        ["diminution", ["diminishment"]],
        ["diplomat", ["diplomatist"]],
        ["disciplinary", ["disciplinatory"]],
        ["discriminating", ["discriminant"]],
        ["disintegrative", ["disintegratory"]],
        ["dismissal", ["dismission"]],
        ["disorient", ["disorientate"]],
        ["disoriented", ["disorientated"]],
        ["disquiet", ["disquieten"]],
        ["dissociate", ["disassociate"]],
        ["distrait", ["distraite"]],
        ["divergence", ["divergency"]],
        ["divisible", ["dividable"]],
        ["doctrinaire", ["doctrinary"]],
        ["documentary", ["documental"]],
        ["domesticate", ["domesticize"]],
        ["doubt", ["misdoubt"]],
        ["duplicative", ["duplicatory"]],
        ["dutiful", ["duteous"]],
        ["educationist", ["educationalist"]],
        ["educative", ["educatory"]],
        ["empanel", ["impanel"]],
        ["encumbrance", ["cumbrance"]],
        ["endow", ["indow"]],
        ["endue", ["indue"]],
        ["enigmas", ["enigmatas"]],
        ["enlarge", ["enlargen"]],
        ["epic", ["epical"]],
        ["eroticism", ["erotism"]],
        ["ethicist", ["ethician"]],
        ["ex officio", ["ex officiis"]],
        ["exculpatory", ["exculpative"]],
        ["exigency", ["exigence"]],
        ["exigent", ["exigeant"]],
        ["exoticism", ["exotism"]],
        ["expediency", ["expedience"]],
        ["expedient", ["expediential"]],
        ["expedient", ["expediential"]],
        ["extendable", ["extensible"]],
        ["eyeing", ["eying"]],
        ["fief", ["fiefdom"]],
        ["flagrancy", ["flagrance"]],
        ["flatulence", ["flatulency"]],
        ["fraudulent", ["defraudulent"]],
        ["fraudulent", ["fraudful"]],
        ["funereal", ["funebrial"]],
        ["geographic", ["geographical"]],
        ["geometric", ["geometrical"]],
        ["goatherd", ["goatherder"]],
        ["grievance", ["aggrievance"]],
        ["gustatory", ["gustatorial"]],
        ["habit", ["habitude"]],
        ["henceforth", ["henceforward"]],
        ["hesitancy", ["hesitance"]],
        ["heterogeneous", ["heterogenous"]],
        ["hierarchical", ["hierarchic"]],
        ["hindmost", ["hindermost"]],
        ["honoree", ["honorand"]],
        ["hypostatize", ["hypostasize"]],
        ["hysterical", ["hysteric"]],
    ]
    return preferred_forms_check(text, preferences, err, msg)


def calc_data_1() -> list:
    preferences: final = [
        # Needless variants
        ["abolition", ["abolishment"]],
        ["accessory", ["accessary"]],
        ["accredit", ["accreditate"]],
        ["accrual", ["accruement"]],
        ["accumulate", ["cumulate"]],
        ["accused", ["accusee"]],
        ["acquaintance", ["acquaintanceship"]],
        ["acquittal", ["acquitment"]],
        ["administer", ["administrate"]],
        ["administered", ["administrated"]],
        ["administering", ["administrating"]],
        ["adulterous", ["adulterate"]],
        ["advisory", ["advisatory"]],
        ["advocate", ["advocator"]],
        ["alleger", ["allegator"]],
        ["allusive", ["allusory"]],
        ["ameliorate", ["meliorate"]],
        ["amorous", ["amative"]],
        ["amortization", ["amortizement"]],
        ["amphibology", ["amphiboly"]],
        ["anachronism", ["parachronism"]],
        ["anecdotist", ["anecdotalist"]],
        ["anilingus", ["anilinctus"]],
        ["anticipatory", ["anticipative"]],
        ["antithetical", ["antithetic"]],
        ["applicable", ["applicative"]],
        ["applicable", ["applicatory"]],
        ["applicator", ["applier"]],
        ["approbatory", ["approbative"]],
        ["arbitrageur", ["arbitrager"]],
        ["arsenious", ["arsenous"]],
        ["ascendancy", ["ascendance"]],
        ["ascendancy", ["ascendence"]],
        ["ascendancy", ["ascendency"]],
        ["authorial", ["auctorial"]],
        ["averment", ["averral"]],
        ["barbed wire", ["barbwire"]],
        ["beneficent", ["benefic"]],
        ["benign", ["benignant"]],
        ["bestowal", ["bestowment"]],
        ["betrothal", ["betrothment"]],
        ["blameworthiness", ["blamableness"]],
        ["buck naked", ["butt naked"]],
        ["captor", ["capturer"]],
        ["carte blanche", ["carta blanca"]],
        ["casualties", ["casualities"]],
        ["casualty", ["casuality"]],
        ["catch fire", ["catch on fire"]],
        ["catholically", ["catholicly"]],
        ["ceasefire", ["cease fire"]],
        ["cellphone", ["cell phone", "cell-phone"]],
        ["channel", ["channelize"]],
        ["chaplaincy", ["chaplainship"]],
        ["chrysalis", ["chrysalid"]],
        ["chrysalises", ["chrysalids"]],
        ["cigarette", ["cigaret"]],
        ["cliquish", ["cliquey", "cliquy"]],
        ["cognitive", ["cognitional"]],
        ["cohabit", ["cohabitate"]],
        ["cohabitant", ["cohabitor"]],
        ["collodion", ["collodium"]],
        ["collusive", ["collusory"]],
        ["commemorative", ["commemoratory"]],
        ["commonage", ["commonty"]],
        ["communicative", ["communicatory"]],
        ["compensatory", ["compensative"]],
        ["complacency", ["complacence"]],
        ["complicit", ["complicitous"]],
        ["compute", ["computate"]],
        ["comrade", ["camarade"]],
        ["conciliatory", ["conciliative"]],
        ["concomitance", ["concomitancy"]],
        ["condonation", ["condonance"]],
        ["confirmatory", ["confirmative"]],
        ["congruence", ["congruency"]],
        ["connote", ["connotate"]],
        ["consanguine", ["consanguineal"]],
        ["conspicuousness", ["conspicuity"]],
        ["conspirator", ["conspiratorialist"]],
        ["constitutionalist", ["constitutionist"]],
        ["contemporaneous", ["cotemporaneous"]],
        ["contemporary", ["cotemporary"]],
        ["contigency", ["contingence"]],
        ["contributory", ["contributary"]],
        ["contumacy", ["contumacity"]],
        ["convertible", ["conversible"]],
        ["conveyance", ["conveyal"]],
        ["corroborative", ["corroboratory"]],
        ["coworker", ["coemployee"]],
        ["curative", ["curatory"]],
        ["daredevilry", ["daredeviltry"]],
        ["deceptive", ["deceptious"]],
        ["defamatory", ["defamative"]],
        ["degenerative", ["degeneratory"]],
        ["delimit", ["delimitate"]],
        ["delusive", ["delusory"]],
        ["denunciation", ["denouncement"]],
        ["depositary", ["depositee"]],
        ["depreciatory", ["depreciative"]],
        ["deprivation", ["deprival"]],
        ["derogatory", ["derogative"]],
        ["destructible", ["destroyable"]],
        ["dethrone", ["disenthrone"]],
        ["detoxify", ["detoxicate"]],
        ["detractive", ["detractory"]],
        ["deuterogamy", ["digamy"]],
        ["deviance", ["deviancy"]],
        ["deviant", ["deviationist"]],
        ["digitize", ["digitalize"]],
        ["diminution", ["diminishment"]],
        ["diplomat", ["diplomatist"]],
        ["disciplinary", ["disciplinatory"]],
        ["discriminating", ["discriminant"]],
        ["disintegrative", ["disintegratory"]],
        ["dismissal", ["dismission"]],
        ["disorient", ["disorientate"]],
        ["disoriented", ["disorientated"]],
        ["disquiet", ["disquieten"]],
        ["dissociate", ["disassociate"]],
        ["distrait", ["distraite"]],
        ["divergence", ["divergency"]],
        ["divisible", ["dividable"]],
        ["doctrinaire", ["doctrinary"]],
        ["documentary", ["documental"]],
        ["domesticate", ["domesticize"]],
        ["doubt", ["misdoubt"]],
        ["duplicative", ["duplicatory"]],
        ["dutiful", ["duteous"]],
        ["educationist", ["educationalist"]],
        ["educative", ["educatory"]],
        ["empanel", ["impanel"]],
        ["encumbrance", ["cumbrance"]],
        ["endow", ["indow"]],
        ["endue", ["indue"]],
        ["enigmas", ["enigmatas"]],
        ["enlarge", ["enlargen"]],
        ["epic", ["epical"]],
        ["eroticism", ["erotism"]],
        ["ethicist", ["ethician"]],
        ["ex officio", ["ex officiis"]],
        ["exculpatory", ["exculpative"]],
        ["exigency", ["exigence"]],
        ["exigent", ["exigeant"]],
        ["exoticism", ["exotism"]],
        ["expediency", ["expedience"]],
        ["expedient", ["expediential"]],
        ["expedient", ["expediential"]],
        ["extendable", ["extensible"]],
        ["eyeing", ["eying"]],
        ["fief", ["fiefdom"]],
        ["flagrancy", ["flagrance"]],
        ["flatulence", ["flatulency"]],
        ["fraudulent", ["defraudulent"]],
        ["fraudulent", ["fraudful"]],
        ["funereal", ["funebrial"]],
        ["geographic", ["geographical"]],
        ["geometric", ["geometrical"]],
        ["goatherd", ["goatherder"]],
        ["grievance", ["aggrievance"]],
        ["gustatory", ["gustatorial"]],
        ["habit", ["habitude"]],
        ["henceforth", ["henceforward"]],
        ["hesitancy", ["hesitance"]],
        ["heterogeneous", ["heterogenous"]],
        ["hierarchical", ["hierarchic"]],
        ["hindmost", ["hindermost"]],
        ["honoree", ["honorand"]],
        ["hypostatize", ["hypostasize"]],
        ["hysterical", ["hysteric"]],
    ]
    return preferred_forms_check2_pre(preferences)


def calc_data_2() -> list:
    preferences: final = [
        ["idolize", ["idolatrize"]],
        ["impersonation", ["personation"]],
        ["impervious", ["imperviable"]],
        ["importunity", ["importunacy"]],
        ["impotence", ["impotency"]],
        ["imprimatur", ["imprimatura"]],
        ["improper", ["improprietous"]],
        ["incitement", ["incitation"]],
        ["inconsistency", ["inconsistence"]],
        ["incriminate", ["criminate"]],
        ["inculpatory", ["culpatory"]],
        ["incurrence", ["incurment"]],
        ["infrequent", ["unfrequent"]],
        ["inhibitory", ["inhibitive"]],
        ["innovative", ["innovational"]],
        ["inquisitorial", ["inquisitional"]],
        ["insistence", ["insistment"]],
        ["instillation", ["instillment"]],
        ["instinctive", ["instinctual"]],
        ["insubstantial", ["unsubstantial"]],
        ["insurer", ["insuror"]],
        ["insurrectionary", ["insurrectional"]],
        ["interpret", ["interpretate"]],
        ["intervention", ["intervenience"]],
        ["ironic", ["ironical"]],
        ["irrevocable", ["unrevokable"]],
        ["judgmental", ["judgmatic"]],
        ["jury-rigged", ["gerry-rigged"]],
        ["jury-rigged", ["jerry-rigged"]],
        ["kaffeeklatsch", ["Coffee klatsch", "coffee klatch"]],
        ["knickknack", ["nicknack"]],
        ["labyrinthine", ["labyrinthian"]],
        ["laudatory", ["laudative"]],
        ["legitimation", ["legitimatization"]],
        ["legitimation", ["legitimization"]],
        ["legitimize", ["legitimatize"]],
        ["lengthwise", ["lengthways"]],
        ["licorice", ["liquorice"]],
        ["life-size", ["life-sized"]],
        ["lithe", ["lithesome"]],
        ["loath", ["loth"]],
        ["lollypop", ["lollipop"]],
        ["lubricious", ["lubricous"]],
        ["mayhem", ["maihem"]],
        ["medical marijuana", ["medicinal marijuana"]],
        ["minimize", ["minimalize"]],
        ["monetize", ["monetarize"]],
        ["movable", ["moveable"]],
        ["murk", ["mirk"]],
        ["murky", ["mirky"]],
        ["narcissism", ["narcism"]],
        ["neglectful", ["neglective"]],
        ["negligence", ["negligency"]],
        ["neologist", ["neologizer"]],
        ["neurological", ["neurologic"]],
        ["nictitate", ["nictate"]],
        ["normality", ["normalcy"]],
        ["numbness", ["numbedness"]],
        ["omissible", ["omittable"]],
        ["onomatopoeic", ["onomatopoetic"]],
        ["opined", ["opinioned"]],
        ["optimal advantage", ["optimum advantage"]],
        ["orient", ["orientate"]],
        ["outsize", ["outsized"]],
        ["oversize", ["oversized"]],
        ["overthrow", ["overthrowal"]],
        ["pacifist", ["pacificist"]],
        ["parti-colored", ["parti-color"]],
        ["parti-colored", ["party-colored"]],
        ["participatory", ["participative"]],
        ["partner", ["copartner"]],
        ["partnership", ["copartnership"]],
        # ["password",          ["passcode"]],  # common term > 2020
        ["patina", ["patine"]],
        ["pederast", ["paederast"]],
        ["pediatrician", ["pediatrist"]],
        ["pejorative", ["perjorative"]],
        ["penumbral", ["penumbrous"]],
        ["permissive", ["permissory"]],
        ["permute", ["permutate"]],
        ["pharmaceutical", ["pharmaceutic"]],
        ["pleurisy", ["pleuritis"]],
        ["policyholder", ["policy holder"]],
        ["policyholder", ["policyowner"]],
        ["politicize", ["politicalize"]],
        ["pre-Columbian", ["precolumbian"]],
        ["precedence", ["precedency"]],
        ["preceptorial", ["preceptoral"]],
        ["precipitancy", ["precipitance"]],
        ["precipitate", ["precipitant"]],
        ["preclusive", ["preclusory"]],
        ["prefectorial", ["prefectoral"]],
        ["preponderantly", ["preponderately"]],
        ["preservation", ["preserval"]],
        ["preventive", ["preventative"]],
        ["proconsulate", ["proconsulship"]],
        ["procreative", ["procreational"]],
        ["procurement", ["procurance"]],
        ["propulsion", ["propelment"]],
        ["propulsive", ["propulsory"]],
        ["prosecutory", ["prosecutive"]],
        ["protective", ["protectory"]],
        ["provocative", ["provocatory"]],
        ["prurience", ["pruriency"]],
        ["psychical", ["psychal"]],
        ["punitive", ["punitory"]],
        ["pygmy", ["pygmean", "pygmaen"]],
        ["quantify", ["quantitate"]],
        ["questionnaire", ["questionary"]],
        ["quiescence", ["quiescency"]],
        ["rabbi", ["rabbin"]],
        ["reasonableness", ["reasonability"]],
        ["recidivous", ["recidivistic"]],
        ["recriminatory", ["recriminative"]],
        ["recruitment", ["recruital"]],
        ["recurrence", ["recurrency"]],
        ["recusal", ["recusation"]],
        ["recusal", ["recusement"]],
        ["recusancy", ["recusance"]],
        ["redemptive", ["redemptory"]],
        ["referable", ["referrable"]],
        ["referable", ["referrible"]],
        ["refutative", ["refutatory"]],
        ["remission", ["remittal"]],
        ["remittance", ["remitment"]],
        ["renounceable", ["renunciable"]],
        ["renunciation", ["renouncement"]],
        ["reparative", ["reparatory"]],
        ["repudiatory", ["repudiative"]],
        ["requital", ["requitement"]],
        ["rescission", ["rescindment"]],
        ["restoration", ["restoral"]],
        ["reticence", ["reticency"]],
        ["retributive", ["retributional", "retributionary"]],
        ["review", ["reviewal"]],
        ["revision", ["revisal"]],
        ["revisionary", ["revisional"]],
        ["revocable", ["revokable", "revokeable"]],
        ["revolt", ["revolute"]],
        ["salience", ["saliency"]],
        ["salutary", ["salutiferous"]],
        ["sensory", ["sensatory"]],
        ["sessional", ["sessionary"]],
        ["shareholder", ["shareowner"]],
        ["sickly", ["sicklily"]],
        ["signatory", ["signator"]],
        ["slander", ["slanderize"]],
        ["societal", ["societary"]],
        ["sodomite", ["sodomist"]],
        ["solicit", ["solicitate"]],
        ["speculative", ["speculatory"]],
        ["spirituous", ["spiritous"]],
        ["statutory", ["statutorial"]],
        ["submersible", ["submergeable"]],
        ["submission", ["submittal"]],
        ["subtle", ["subtile"]],
        ["succubus", ["succuba"]],
        ["sufficiency", ["sufficience"]],
        ["supplicant", ["suppliant"]],
        ["surmise", ["surmisal"]],
        ["suspendable", ["suspendible"]],
        ["swathe", ["enswathe"]],
        ["synthesize", ["synthetize"]],
        ["systematize", ["systemize"]],
        ["T-shirt", ["tee-shirt"]],
        ["tactile", ["tactual"]],
        ["tangential", ["tangental"]],
        ["tautological", ["tautologous"]],
        ["thenceforth", ["thenceforward"]],
        ["transience", ["transiency"]],
        ["transposition", ["transposal"]],
        ["transposition", ["transposal"]],
        ["unalterable", ["inalterable"]],
        ["uncommunicative", ["incommunicative"]],
        ["uncontrollable", ["incontrollable"]],
        ["unenforceable", ["nonenforceable"]],
        ["unnavigable", ["innavigable"]],
        ["unreasonableness", ["unreasonability"]],
        ["unsolvable", ["insolvable"]],
        ["usurpation", ["usurpature"]],
        ["variational", ["variative"]],
        ["vegetative", ["vegetive"]],
        ["vindictive", ["vindicative"]],
        ["vituperative", ["vituperous"]],
        ["vociferous", ["vociferant"]],
        ["volitional", ["volitive"]],
        ["wolfish", ["wolvish"]],
        ["wolverine", ["wolverene"]],
        ["Zoroastrianism", ["Zoroastrism"]],
    ]
    return preferred_forms_check2_pre(preferences)


data1 = calc_data_1()
data2 = calc_data_2()


def disabled_check_1(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms.

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "needless_variants.misc"
    msg = "'{1}' is a needless variant. '{0}' is the preferred form."
    return preferred_forms_check2_main(text, data1, err, msg)


def check_2(text: str) -> list[ResultCheck]:
    """Suggest the preferred forms.

    NOTE: this was one of the slowest Checks,
          so it was segmented to even the load for parallelization
    """
    err = "needless_variants.misc"
    msg = "'{1}' is a needless variant. '{0}' is the preferred form."
    return preferred_forms_check2_main(text, data2, err, msg)

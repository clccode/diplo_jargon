"""
Word list for the Diplomacy word-guessing game.

Each entry below is (word, hint_template), where the hint_template
contains a "{blank}" placeholder. At import time, DIPLOMACY_WORDS is
built by substituting that placeholder with underscores matching the
exact length of the word, so the blanks always stay in sync even if
you edit a word later.

Usage:
    from diplomacy_words import DIPLOMACY_WORDS
    word, hint = DIPLOMACY_WORDS[0]
    # word -> "entente"
    # hint -> "An _______ is a friendly understanding or an informal
    #          alliance between nations."
"""

_RAW_WORDS = [
    ("entente", "An {blank} is a friendly understanding or an informal alliance between nations."),
    ("treaty", "A {blank} is a formally signed and ratified agreement between countries."),
    ("alliance", "An {blank} is a union formed for mutual benefit, often between nations."),
    ("embassy", "An {blank} is the official offices of an ambassador in a foreign country."),
    ("envoy", "An {blank} is a diplomat sent on a special mission."),
    ("sanction", "A {blank} is a penalty imposed by one country against another, often economic."),
    ("armistice", "An {blank} is a formal agreement to stop fighting."),
    ("ceasefire", "A {blank} is a temporary suspension of hostilities."),
    ("neutrality", "{blank} is the state of not taking sides in a conflict."),
    ("sovereignty", "{blank} is the full right of a state to govern itself."),
    ("diplomat", "A {blank} is an official who represents their country abroad."),
    ("summit", "A {blank} is a high-level meeting between heads of state."),
    ("protocol", "{blank} refers to the official rules of diplomatic conduct."),
    ("accord", "An {blank} is a formal agreement between parties."),
    ("mediator", "A {blank} is a neutral party who helps resolve a dispute."),
    ("delegate", "A {blank} is a person sent to represent others at a conference."),
    ("consulate", "A {blank} is an office representing a foreign country in a city."),
    ("negotiate", "To {blank} is to discuss terms in order to reach an agreement."),
    ("concession", "A {blank} is something given up in order to reach an agreement."),
    ("blockade", "A {blank} is the sealing off of a place to prevent goods or people from entering."),
    ("coalition", "A {blank} is a temporary alliance of groups for a common purpose."),
    ("sanctuary", "A {blank} is a place offering protection or safety."),
    ("pact", "A {blank} is a formal agreement between two or more parties."),
    ("reparations", "{blank} are payments made to compensate for damage caused during a conflict."),
    ("ambassador", "An {blank} is the highest-ranking diplomat representing a country."),
    ("arbitration", "{blank} is the process of settling a dispute through a neutral third party."),
    ("hostage", "A {blank} is a person seized to compel another party to act."),
    ("embargo", "An {blank} is an official ban on trade with a particular country."),
    ("tariff", "A {blank} is a tax imposed on imported goods."),
    ("annexation", "{blank} is the act of forcibly adding territory to another state."),
    ("secession", "{blank} is the act of formally withdrawing from a political union."),
    ("autonomy", "{blank} is the right of self-governance."),
    ("federation", "A {blank} is a union of states with a central governing body."),
    ("propaganda", "{blank} is biased information used to promote a political cause."),
    ("espionage", "{blank} is the practice of spying to gather secret information."),
    ("detente", "{blank} is the easing of strained relations between nations."),
    ("plebiscite", "A {blank} is a direct vote by citizens on a political issue."),
    ("referendum", "A {blank} is a public vote on a single political question."),
    ("hegemony", "{blank} is the dominance of one state or group over others."),
    ("isolationism", "{blank} is a policy of avoiding political alliances with other countries."),
    ("multilateral", "{blank} describes an agreement involving three or more parties."),
    ("bilateral", "{blank} describes an agreement involving two parties."),
    ("ratify", "To {blank} is to formally approve a treaty or agreement."),
    ("compromise", "A {blank} is an agreement reached through mutual concession."),
    ("peacekeeping", "{blank} refers to efforts to maintain peace after a conflict."),
    ("superpower", "A {blank} is a nation with dominant global influence."),
    ("neutral", "{blank} describes a party that does not take sides in a conflict."),
    ("statecraft", "{blank} is the skillful management of state affairs and diplomacy."),
    ("conciliation", "{blank} is the process of overcoming distrust and resolving differences."),
    ("asylum", "{blank} is protection granted by a state to someone fleeing persecution."),
    ("attache", "An {blank} is a diplomatic official assigned to an embassy, often specializing in a particular field."),
    ("extradition", "{blank} is the surrender of a person by one state to another for trial or punishment."),
    ("repatriation", "{blank} is the return of a person, such as a refugee or prisoner, to their home country."),
    ("recognition", "{blank} is a state's formal acknowledgment of another state or government as legitimate."),
    ("rapprochement", "A {blank} is the re-establishment of friendly relations between two countries."),
    ("trusteeship", "A {blank} is a territory placed under the administration of another country, often under international supervision."),
    ("mandate", "A {blank} is an authorization given to a country to administer a territory on behalf of an international body."),
    ("plenipotentiary", "A {blank} is a diplomat given full authority to act on behalf of their government."),
    ("communique", "A {blank} is an official statement or announcement, especially one released after a diplomatic meeting."),
    ("ultimatum", "An {blank} is a final demand, the rejection of which may lead to a breakdown in relations or war."),
    ("reciprocity", "{blank} is the practice of exchanging privileges or treatment on equal terms between countries."),
    ("unilateral", "{blank} describes an action taken by one party without the agreement of others."),
    ("trilateral", "{blank} describes an agreement or action involving three parties."),
    ("appeasement", "{blank} is the policy of making concessions to an aggressive power to avoid conflict."),
    ("containment", "{blank} is a policy of preventing the expansion of a hostile power or ideology."),
    ("deterrence", "{blank} is the use of threats, such as military strength, to discourage an adversary from acting."),
    ("brinkmanship", "{blank} is the practice of pushing a dangerous situation to the verge of conflict to gain advantage."),
    ("realpolitik", "{blank} is a practical approach to politics based on power and interests rather than ideals."),
    ("disarmament", "{blank} is the reduction or elimination of a country's weapons and armed forces."),
    ("demilitarization", "{blank} is the removal of military forces and fortifications from an area."),
    ("protectorate", "A {blank} is a state that is controlled and protected by a stronger one."),
    ("suzerainty", "{blank} is a relationship in which a dominant state controls the foreign affairs of a subordinate one that retains internal autonomy."),
    ("irredentism", "{blank} is a political movement seeking to reclaim territory on ethnic or historical grounds."),
    ("belligerent", "A {blank} is a nation or group formally engaged in a war."),
    ("combatant", "A {blank} is a person or party engaged directly in fighting during a conflict."),
    ("capitulation", "A {blank} is an agreement to surrender under specified conditions."),
    ("indemnity", "An {blank} is compensation paid, often by a defeated nation, for losses or damages."),
    ("protectionism", "{blank} is a trade policy that shields domestic industries using tariffs or restrictions."),
    ("demarche", "A {blank} is a formal diplomatic protest or representation made to a foreign government."),
    ("condominium", "A {blank} is territory governed jointly by two or more states."),
    ("nonalignment", "{blank} is a policy of not formally allying with any major power bloc."),
    ("nonintervention", "{blank} is the principle that states should not interfere in the internal affairs of others."),
    ("normalization", "{blank} is the process of establishing or restoring standard diplomatic relations between countries."),
    ("credentials", "{blank} are documents presented by a diplomat to formally establish their authority to represent their government."),
    ("exequatur", "An {blank} is an official recognition granted by a host country authorizing a consul to perform their duties."),
    ("vassal", "A {blank} is a state or ruler subordinate to a more powerful one."),
    ("suzerain", "A {blank} is a dominant power that controls the foreign affairs of a subordinate state."),
    ("parley", "A {blank} is a discussion between opposing sides to settle a dispute or negotiate terms."),
    ("legate", "A {blank} is an official envoy or representative, especially one sent by a high authority such as the Pope."),
    ("nuncio", "A {blank} is a papal ambassador representing the Vatican in a foreign country."),
    ("consul", "A {blank} is an official appointed to represent a country's commercial and citizen interests in a foreign city."),
    ("extraterritoriality", "{blank} is the exemption of a person or place from the legal jurisdiction of the country in which they are located."),
    ("revanchism", "{blank} is a policy aimed at recovering territory or status lost in a previous conflict."),
    ("concordat", "A {blank} is a formal agreement between the Holy See and a national government."),
    ("veto", "A {blank} is the power to unilaterally block a decision, such as in the UN Security Council."),
    ("covenant", "A {blank} is a formal, binding agreement between nations."),
    ("charter", "A {blank} is a formal document establishing an organization and outlining its principles, such as the United Nations Charter."),
]

DIPLOMACY_WORDS = [
    (word, template.format(blank="_" * len(word)))
    for word, template in _RAW_WORDS
]
"""
The Words of Estimative Probability are to convey the likelihood of a future event occurring. A well-chosen WEP
gives a decision maker a clear and unambiguous estimate upon which to base a decision.
"""

# Weasel words use in estimative statements is almost certain to confuse; they should be avoided at all costs.
weasel_words = [  # TODO: tidy up speech marks
    'might', "It's conceivable", "could", "may", 'suggest', 'perhaps',
    'possibly', 'we believe not', 'we do not believe', 'I do not believe', 'I believe',
    'a chance', 'estimate that', 'cannot rule out', 'cannot dismiss'
]

"word: margin, min_percent, max_percent, descriptor"

medicine_words = {
    1: {
        "word": "Likely",
        "min_percent": 51,
        "max_percent": 100,
        "margin": None,
        "descriptor": "Expected to happen to more than 50% of subjects."
    },
    2: {
        "word": "Frequent",
        "min_percent": 10,
        "max_percent": 50,
        "margin": None,
        "descriptor": "Expected to happen to more than 50% of subjects."
    },
    3: {
        "word": "Occasional",
        "min_percent": 2,
        "max_percent": 9.9,
        "margin": None,
        "descriptor": "Will happen to 1-10% of subjects."
    },
    4: {
        "word": "Rare",
        "min_percent": 0,
        "max_percent": 1,
        "margin": None,
        "descriptor": "Will happen to less than 1% of subjects."
    }
}

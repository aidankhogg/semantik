from semantikIntelligence.intel_agency.nucleus import Discipline


class HumanIntelligence(Discipline):
    """
    Human intelligence (HUMINT) are gathered from a person in the location in question.
    """

    def __init__(self):
        self.acronym = 'HUMINT'
        self.name = 'Human Intelligence'

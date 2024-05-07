from abc import ABC


class AgencyBranch(ABC):
    def __init__(self):
        self.branch_type = 'unknown'


class IntelligenceBranch(AgencyBranch):
    def __init__(self):
        super().__init__()
        self.branch_type = 'intelligence'


class OperationsBranch(AgencyBranch):
    def __init__(self):
        super().__init__()
        self.branch_type = 'operations'


class OperativeBranch(AgencyBranch):
    def __init__(self):
        super().__init__()
        self.branch_type = 'operative'


class DefenseBranch(AgencyBranch):
    def __init__(self):
        super().__init__()
        self.branch_type = 'counter'


if __name__ == '__main__':
    pass

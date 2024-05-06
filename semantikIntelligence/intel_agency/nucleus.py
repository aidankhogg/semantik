from abc import ABC

from engine.worker.base import WorkOrder, Worker


class Discipline(ABC):
    pass


class BaseIntelligenceAsset(ABC):
    pass


class BaseIntelligenceAgent(ABC):
    pass


class IntelligenceOfficer(Worker):
    def __init__(self):
        super().__init__()


class BaseIntelligenceRequest(ABC):
    pass


class BaseIntelligenceOrder(WorkOrder, ABC):
    pass


class BaseIntelligenceFocus(ABC):
    pass

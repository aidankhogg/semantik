from semantikIntelligence.intel_agency.management.desks import IntelligenceDesk, IntelligenceRequest, IntelligenceOrder
from semantikIntelligence.intel_agency.management.ops import OperationsCenter


class IntelligenceAgency:
    def __init__(self):
        self.intelligence_desk = IntelligenceDesk()
        self.operations_center = OperationsCenter()
        self.officer_pool = []
        self.strategy_board = None

    def submit_request(self, request: IntelligenceRequest):
        self.intelligence_desk.add_to_desk(request)

    def deliver_order(self, order: IntelligenceOrder):
        self.operations_center.receive_orders(order)


if __name__ == '__main__':
    sia = IntelligenceAgency()

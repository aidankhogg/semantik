from typing import Union, List
from uuid import UUID

from commons.patterns.creational.singleton import ThreadedSingletonMeta
from semantikIntelligence.old_agency.activities import IntelMission, IntelOperation
from semantikIntelligence.old_agency.beauracracy.boxticking import IntelligenceRequest, IntelligenceOrder

print("Import finished")


class IntelligenceAgency:

    def __init__(self):
        self._cursor = None
        self.ops_center = OperationsCenter()
        self.intel_desk = IntelligenceDesk()
        self.officer_pool = OfficerPool()

    def select(self, reference: Union[str, UUID], desk: str = 'any'):
        """

        :param reference:
        :param desk:
        :return:
        """
        pass


class OperationsCenter(metaclass=ThreadedSingletonMeta):
    def __init__(self):
        self._cursor = None
        self._historic = []
        self._missions = []
        self._operations = []
        self.test = [1, 'dfs', '983244f4-fWW4-FW4F4']


    def receive_orders(self, orders: IntelligenceOrder):
        if isinstance(orders, IntelMission):
            print('Mission')
            self._missions.append(orders)
        elif isinstance(orders, IntelOperation):
            print('Operation')
            self._operations.append(orders)
        else:
            if isinstance(orders, IntelligenceOrder):
                self._operations.append(orders)
            else:
                raise TypeError("Not an intelligence order")

    def execute_mission(self, mission_reference: str):
        pass

    def abort_mission(self, mission_reference: str):
        pass

    def halt_mission(self, mission_reference: str):
        pass

    def situation_report(self, mission_reference: str) -> dict:
        return {}

    def launch_operation(self, op_reference: str):
        pass

    def halt_operation(self, op_reference: str):
        pass

    def wrap_operation(self, op_reference: str):
        pass

    def operation_update(self, op_reference: str):
        pass

    def select_mission(self, mission_reference: str):
        pass

    def select_operation(self, op_reference: str):
        pass


class IntelligenceDesk(metaclass=ThreadedSingletonMeta):
    def __init__(self):
        self._cursor = None
        self.requests = []

    @property
    def open_requests(self):
        return self.requests

    def add_to_desk(self, request: IntelligenceRequest):
        pass

    def update_request(self, request: IntelligenceRequest):
        pass

    def select(self, reference: Union[str, UUID], desk: str = 'any'):
        pass


class OfficerPool(metaclass=ThreadedSingletonMeta):
    def __init__(self):
        self._offices = []

    @property
    def all_officers(self):
        return self._offices


if __name__ == '__main__':
    sia = IntelligenceAgency()

from typing import Union, List
from uuid import UUID

from commons.patterns.creational.singleton import ThreadedSingletonMeta
from semantikIntelligence.intel_agency.management.desks import IntelligenceOrder


class OperationsCenter:  # TODO: Singleton
    def __init__(self):
        self._active_ops = List[IntelligenceOperation]
        self._suspended_ops: List[IntelligenceOperation] = []

    def get_sitrep(self, op_ref: Union[str, UUID]) -> Union[str, dict]:
        print(f"checking status of operation '{op_ref}'")
        if op_ref in self._active_ops:
            print("found")
        return 'unknown'

    def receive_orders(self, orders: Union[IntelligenceOrder, list]) -> None:
        pass


class IntelligenceOperation:
    def __init__(self):
        self._order: IntelligenceOrder or None = None


if __name__ == '__main__':
    test = OperationsCenter()

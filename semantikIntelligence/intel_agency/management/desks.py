from abc import ABC
from typing import Union
from uuid import uuid4, UUID


class IntelligenceRequest:
    def __init__(self):
        self._meta = {
            "uid": uuid4()
        }

    @property
    def request_id(self) -> str:
        return str(self._meta["uid"])

    def check_status(self, request_ref: Union[str, UUID]):
        pass


class IntelligenceOrder:
    def __init__(self):
        self._request: IntelligenceRequest or None = None


class IntelligenceDesk:
    def __init__(self):
        self._open_requests = []

    @property
    def requests(self):
        return self._open_requests

    def add_to_desk(self, request: IntelligenceRequest):
        pass

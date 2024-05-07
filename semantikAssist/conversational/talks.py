from typing import List

from commons.patterns.structural.composition import Component


class Message(Component):
    """
    TODO: Add class docstring
    """

    def __init__(self):
        super().__init__()
        self.raw = "raw message"

    def operation(self) -> str:
        pass


class Conversation(Component):
    def __init__(self):
        self._children: List[Component] = []
        

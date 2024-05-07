from abc import ABC


class BasePersona(ABC):
    def __init__(self):
        pass


class Persona(BasePersona, ABC):
    def __init__(self):
        super().__init__()

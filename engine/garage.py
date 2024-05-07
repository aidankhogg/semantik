from semantik.app import start_app
from commons.patterns.creational.singleton import ThreadedSingletonMeta

"""
The garage module contains 
"""


class Engine(metaclass=ThreadedSingletonMeta):
    """
    TODO: Add docstring here for the Engine class
    """

    def __init__(self):
        self.test = 1

    @staticmethod
    def start() -> None:
        """
        TODO: Add docstring here for engine start method
        :return: nothing
        """
        start_app()

    def stop(self, force_stop: bool = False) -> None:
        """
        TODO: Add docstring here for engine stop method
        :param force_stop: force terminate the app?
        :return: nothing
        """
        pass


if __name__ == "__main__":
    engine = Engine()
    print(engine.test)
    engine2 = Engine()
    engine2.test = 2
    print(engine2.test)
    print(engine.test)

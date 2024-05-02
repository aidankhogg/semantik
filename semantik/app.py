from commons.patterns.creational.singleton import ThreadedSingletonMeta

"""
The semantik app module contains the object representation of
"""


class Semantik(metaclass=ThreadedSingletonMeta):  # TODO: Turn into a Singleton
    """
    TODO: Add docstring here for semantik class
    :return:
    """

    def __init__(self):
        pass


def start_app() -> None:
    """
    TODO: Add docstring here for start_app method
    :return:
    """
    pass


if __name__ == '__main__':
    start_app()

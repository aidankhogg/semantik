from os import environ
from engine.garage import Engine


def boot_checks(passive_only: bool = False) -> None:
    """
    TODO: Add docstring here for boot_checks method.
    :param passive_only:
    :return: nothing
    """
    pass


def start_engine() -> None:
    """
    TODO: Add docstring here for start_engine method
    :return: nothing
    """
    print("Starting engine...")
    Engine().start()


def stop_engine(force_shutdown: bool = False) -> None:
    """
    TODO: Add docstring here for stop_engine method
    :param force_shutdown:
    :return: nothing
    """
    if force_shutdown:
        print("Stopping engine forcefully...")
    else:
        print("Stopping engine...")
    Engine().stop(force_shutdown)

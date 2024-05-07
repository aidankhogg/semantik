from os import environ
from typing import Union

from engine.garage import Engine


def boot_checks(passive_check: bool = False,
                include_mark: bool = True,
                include_results: bool = False) -> Union[bool, dict, tuple]:
    """
    TODO: Add docstring here for boot_checks method.
    :param include_mark: return the True for passed mark, False otherwise.
    :param include_results: add the test results - tuple (bool, dict{results})
    :param passive_check: will not raise exceptions for check failures
    :return: nothing
    """
    print("Performing boot checks...")  # TODO: convert to INFO log output
    results = {
        "check_start": True,
        "test_fail": True
    }
    check_passed = True
    failed_checks = []
    for check, passed in results.items():
        if not passed:
            # print(f"{check} failed") TODO: convert to ERROR log
            check_passed = False
            failed_checks.append(check)
        else:
            pass

    if not passive_check and not check_passed:
        raise AssertionError(f"Boot checks failed: {', '.join(failed_checks)}")

    if include_results and include_mark:
        return check_passed, results
    elif include_results and not include_mark:
        return results
    elif include_mark and not include_results:
        return check_passed
    else:
        pass


def start_engine() -> None:
    """
    TODO: Add docstring here for start_engine method
    :return: nothing
    """
    print("Starting engine...")  # TODO: convert to INFO log output
    if not boot_checks():
        raise Exception("Boot checks failed. Aborting engine start.")
    else:
        Engine().start()


def stop_engine(force_shutdown: bool = False) -> None:
    """
    TODO: Add docstring here for stop_engine method
    :param force_shutdown:
    :return: nothing
    """
    if force_shutdown:
        print("Stopping engine forcefully...")  # TODO: convert to WARNING log output
    else:
        print("Stopping engine...")  # TODO: convert to INFO log output
    Engine().stop(force_shutdown)


if __name__ == "__main__":
    print("Manual boot check started...")
    status, checks = boot_checks(passive_check=True, include_mark=True, include_results=True)
    print(status)
    print(checks)
    start_engine()
    stop_engine()

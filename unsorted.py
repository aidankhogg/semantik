import logging
import os.path
from typing import Union


def detect_project_path(override_flag_file: Union[str, None] = None) -> str:
    """
    Get project path from by detecting a flag file. 'main.py' by default
    :param override_flag_file: specify an alternative file to be used as the flag of the root directory
    :return: string of the path or raises *FileNotFoundError*
    """
    current_dir = os.path.abspath(os.curdir)
    while True:
        parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
        # print([parent_dir])
        if os.path.isfile(os.path.join(current_dir, 'main.py' if override_flag_file is None else override_flag_file)):
            return current_dir
        elif current_dir == parent_dir:
            raise FileNotFoundError(f'Could not find this file '
                                    f'({"main.py" if override_flag_file is None else override_flag_file}).')
        else:
            current_dir = parent_dir


def get_project_path(detect_file: Union[str, None] = 'main.py') -> str:
    """
    Checks ENVIRONMENT_PATH environment variable to see if it exists, otherwise performs detection method.
    :return:
    """
    if os.environ.get('ENVIRONMENT_PATH', None) is None:
        logging.warning("Setting environment variable: ENVIRONMENT_PATH")
        os.environ['ENVIRONMENT_PATH'] = detect_project_path(detect_file if detect_file is not None else None)
        return detect_project_path(detect_file if detect_file is not None else None)
    #
    return os.environ['ENVIRONMENT_PATH']


if os.environ.get('ENVIRONMENT_PATH', False) is False or os.environ.get('ENVIRONMENT_PATH', False) is None:
    logging.error("INVESTIFY NOT CONFIGURED. INITIALIZING FIRST RUN.")
    get_project_path()
elif not os.path.isdir(os.environ.get('ENVIRONMENT_PATH', '/m155in6_p4th')):
    logging.error("Environment missing (ENVIRONMENT_PATH is not set). INITIALIZING FIRST RUN.")
logging.warning("Initializing Investify")

logging.warning("Reattempting boot...")

if os.environ.get('ENVIRONMENT_PATH') is False or os.environ.get('ENVIRONMENT_PATH') is None:
    logging.warning("INVESTIFY NOT CONFIGURED. INITIALIZING FIRST RUN.")
else:
    logging.warning("Initializing Investify")

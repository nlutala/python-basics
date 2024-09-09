"""
A module for the logger decorator to sit in.

Author: nlutala (Nathan Lutala)
"""

import logging
from datetime import datetime

LOGGER = logging.getLogger(__name__)

"""
Letting the logger know to write all logs at the info level (my logs) and above to a
file called create_and_load_data.log
"""
logging.basicConfig(
    filename="create_and_load_data.log",
    filemode="w",  # To write new content everytime the program is run again
    encoding="utf-8",
    level=logging.INFO,
)


def log_activity(func: callable):
    """
    Defining a decorator called log_activity, which will be used to log that each
    function has been executed after its completion.\n

    :param - func (a reference to the function passed as a parameter)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        LOGGER.info(
            f"Received {res} from {func.__name__} when executed at {str(datetime.now())}"
        )
        return res

    return wrapper

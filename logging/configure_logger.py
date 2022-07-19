"""

    configure_logger.py

    Description:

        This script is used to configure the loggers that are used for the 
        web scraper and article recommender. The config.json file contains all 
        the configuration arguments. If the config.json file is somehow missing
        an email is sent to the repo owner with the error message.

    Variables:

        base_error_message

    Functions: 

        configure_logger(config_file_name = 'config.json')

"""

###############################################################################

import sys

sys.path.append("modules")

import json
import logging.config
import os

from env import email_address

###############################################################################

base_error_message = """
    An error occurred in configure_logger() in the configure_logger.py module.
"""

###############################################################################


def configure_logger(config_file_name="config.json") -> bool:
    """
    Configure all loggers according to the arguments set in the config file
    file. Upon success this function returns True and will return False
    upon failure. Any errors raised by this function are handled by default
    so that script execution is not killed.

    Parameters
    ----------
    config_file_name: str, optional
        The name of the config file. The file should be a .json file.

    Returns
    -------
    bool: Returns True if the function succeeded in configuring all loggers
        returns false otherwise.

    Handles
    -------
    FileNotFoundError: If the config file doesn't exist or the path
        provided was incorrect an error message is emailed to the app owner
        and the function returns False.

    json.decoder.JSONDecodeError: If the json module is unable to load the
        config file (likely due to the file containing invalid json) an
        error message is emailed to the app owner and the function returns
        False.

    ValueError: If an error in the config file leads the logging module to
        be unable to configure the loggers an error message is emailed to
        the app owner and the function returns False.
    """

    try:
        # Get the config file path.
        logging_config_file = os.path.join(os.path.dirname(__file__), config_file_name)

        # Read the config file and configure the loggers.
        with open(logging_config_file, "r") as config_file:
            config_dict = json.load(config_file)
            logging.config.dictConfig(config_dict)

        return True

    # If the config file was not found.
    except FileNotFoundError as file_error:
        message = base_error_message + file_error
        os.system(
            f'echo {message} | mail -s "Article Recommender Web Scraper Error" {email_address}'
        )
        return False

    # If the json module was unable to load the config file.
    except json.decoder.JSONDecodeError as json_error:
        message = base_error_message + json_error
        os.system(
            f'echo {message} | mail -s "Article Recommender Web Scraper Error" {email_address}'
        )
        return False

    # If an error in the config file led the logging module to be unable to
    # configure the loggers.
    except ValueError as value_error:
        message = base_error_message + value_error
        os.system(
            f'echo {message} | mail -s "Article Recommender Web Scraper Error" {email_address}'
        )
        return False

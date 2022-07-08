"""

    configure_logger.py

    Description:
        This script is used to configure the loggers that are used for the 
        web scraper and article recommender. The config.json file contains all 
        the configuration arguments. If the config.json file is somehow missing
        an email is sent to the repo owner with the error message.

"""

###############################################################################

import json
import logging.config
import os

###############################################################################


def configure_logger():
    try:
        logging_config_file = os.path.join(os.path.dirname(__file__), "config.json")

        with open(logging_config_file, "r") as config_file:
            config_dict = json.load(config_file)
            logging.config.dictConfig(config_dict)

    except FileNotFoundError as fe:
        # Send email with config file missing message.
        pass

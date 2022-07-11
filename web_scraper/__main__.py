"""

    __main__.py

    Description:

        This is the main entry point for the article recommender web scraper. 
        This script serves four main purposes: read any received emails to 
        update the website dataset, scrape article info for all recent articles
        for each website in the website dataset, prepare the data for the 
        article recommender application, and store the prepared data in the 
        database.

    Example Usage:

        This script can be executed from a terminal with the following command:

        python -m web_scraper

"""

###############################################################################

import sys

sys.path.append("logging")
sys.path.append("modules")

import logging
import pandas as pd
import traceback

from configure_logger import configure_logger
from env import email_address

###############################################################################

if __name__ == "__main__":
    try:

        # Configure the logger using the configure_logger module. If the
        # configuration was successful use the webScraper logger for this script.
        logger_configured_successfully = configure_logger()
        logger = None
        if logger_configured_successfully:
            logger = logging.getLogger("webScraper")

        # read new emails for updates

        # Pull all the latest articles from each website and API in the database.
        sites_and_apis = pd.read_csv("data/site-and-api-data.csv")
        for source in sites_and_apis:
            pass

        # prepare the article data

        # write the data to the database

        # If the logger  was configured successfully log that execution of the
        # web scraper script completed.
        if logger_configured_successfully:
            logger.info(
                """Web scraper completed execution.

            -------------------------------------------

            """
            )

    # If an unhandled and unexpected error occurred.
    except Exception as error:
        message = """
            An unexpected and unhandled error occurred in the Article 
            Recommender Web Scraper. This error caused execution of the script 
            to hault. The error has been logged and is also shown here.

        """
        error_message = "".join(
            traceback.format_exception(None, error, error.__traceback__)
        )

        # Log the traceback of the error message.
        if logger_configured_successfully:
            logger.error(error_message)

        # Send an email to the app owner containing the error message.
        os.system(
            f'echo {message + error_message} | mail -s "Article Recommender Web Scraper Error" {email_address}'
        )

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

import logging
import pandas as pd

from configure_logger import configure_logger

###############################################################################

if __name__ == "__main__":

    configure_logger()
    logger = logging.getLogger("webScraper")

    # read new emails for updates

    # Pull all the latest articles from each website and API in the database.
    sites_and_apis = pd.read_csv("data/site-and-api-data.csv")
    for source in sites_and_apis:
        pass

    # prepare the article data

    # write the data to the database

    logger.info("Web scraper completed execution.")

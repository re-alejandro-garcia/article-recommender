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
sys.path.append("web_scraper/extract")

import os
import logging
import pandas as pd
import traceback

import medium
import news

from configure_logger import configure_logger
from env import email_address, news_api_key

###############################################################################

functions = {"medium": medium.get_latest_article_data}

functions_with_api_key = {
    "news": {"function": news.get_latest_article_data, "api_key": news_api_key}
}

###############################################################################

if __name__ == "__main__":
    try:

        # Configure the logger using the configure_logger module. If the
        # configuration was successful use the webScraper logger for this
        # script.
        logger_configured_successfully = configure_logger()
        logger = None
        if logger_configured_successfully:
            logger = logging.getLogger("webScraper")

        # TODO read new emails for updates

        # Pull all the latest articles from each website and API in the
        # database.
        sites_and_apis = pd.read_csv("data/site-and-api-data.csv")
        article_data = pd.DataFrame()
        for index, row in sites_and_apis.iterrows():
            # if row['class'] in functions_with_api_key:
            #   api_key = functions_with_api_key[row['class']]['api_key']
            #   df = functions_with_api_key[row['class']]['function'](row['url'], row['name'], row['topic'], api_key)
            # else:
            #   df = functions[row['class']](row['url'], row['name'], row['topic'])
            # article_data = pd.concat([article_data, df]).reset_index(drop = True)
            pass

        # TODO prepare the article data

        # TODO write the data to the database

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
            f'echo {message + error_message} | mail -s "Article Recommender \
                Web Scraper Error" {email_address}'
        )

# Keep track of all sites to scrape with corresponding: div classes to search for,
# and last article viewed.
# Update website information when necessary
# Return: dict(Article Name : Link) for each website

# Upon initialization load saved website info
# Main script will update website info if necessary, the local website info dict
# will be updated and then used to update the yaml file so re-loading will not
# be necessary.
# Main script will obtain results from obtain_scraping_results().
# - Parse through each website in website_info.
# - For each website search through the html file for each search class.
# - Remove all results after last article viewed (inclusive).
# - Update last article viewed.
# - Update website_info.
# - Combine results and return.

import yaml
import os
import logging
import traceback
from ArticleSuggestor.Web_Scraper.Save_File_IO import Save_File_IO
from ArticleSuggestor.Web_Scraper.Web_Scraper import Web_Scraper
from ArticleSuggestor.Web_Scraper import Data_Cleaner

website_info_file_location = {
    True: os.path.join(os.path.dirname(__file__), "Save_Files/Test_Website_Info.yaml"),
    False: os.path.join(os.path.dirname(__file__), "Save_Files/Website_Info.yaml"),
}


def get_article_data(logger: logging.Logger = None, *, _testing: bool = False) -> list:
    try:
        website_info = Save_File_IO.load_website_info(
            website_info_file_location[_testing], logger
        )
        article_info = []
        for url in website_info:
            scraping_results = Web_Scraper.scrape_website(
                url, website_info[url]["search_classes"], logger
            )
            Data_Cleaner.remove_previously_viewed_articles(
                scraping_results,
                website_info[url]["last_article_viewed"],
                _logger=logger,
            )
            Data_Cleaner.remove_old_articles(scraping_results, _logger=logger)
            article_info.extend(scraping_results)
            if scraping_results:
                website_info[url]["last_article_viewed"] = scraping_results[0]["title"]

        Save_File_IO.save_website_info(
            website_info_file_location[_testing], website_info, logger
        )
        return article_info
    except Exception as e:
        if logger:
            logger.error(
                f"An unhandled exception occurred in Data_Pipeline.py get_article_data()."
            )
            logger.error(f"website_info: {website_info}")
            logger.error(f"traceback: {traceback.print_exc()}")
            logger.error(f"Update the file Data_Pipeline.py to handle exception: {e}")
        else:
            traceback.print_exc()
            print(
                f"An unhandled exception occurred in Data_Pipeline.py get_article_data()."
            )
            print(f"Update the file Data_Pipeline.py to handle exception: {e}")
        return []

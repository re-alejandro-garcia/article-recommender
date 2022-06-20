# Given a web address and search parameters return a list of all matching
# results from an html file. This is an instantiated class.
# All methods accept an optional logger for logging error messages.

from bs4 import BeautifulSoup
import requests
import yaml
import os
import logging
import traceback
import itertools
import sys


class MissingSearchClassesError(Exception):
    """
    Exception raised for missing div search classes in the web scraper.
    """

    def __init__(self, message):
        self.message = message


class Web_Scraper:
    @staticmethod
    def get_soup(website: str, logger: logging.Logger = None) -> BeautifulSoup:
        try:
            result = requests.get(website)
            content = result.text
            soup = BeautifulSoup(content, "lxml")
            soup.prettify()
            return soup
        except requests.exceptions.MissingSchema as ms:
            if logger:
                logger.error(
                    "MissingSchema error occurred in Web_Scraper.py get_soup()."
                )
                logger.error(f"Web address {website} is not a valid URL.")
                logger.error(
                    "From Web_Scraper.py verify that parameter website is correct."
                )
            else:
                traceback.print_exc()
                print(f"Web address {website} is not a valid URL.")
                print("From Web_Scraper.py verify that parameter website is correct.")
            return None
        except requests.exceptions.Timeout as t:
            if logger:
                logger.error("Timeout error occurred in Web_Scraper.py get_soup().")
                logger.error(
                    f"Connection with web address {website} was not successful."
                )
            else:
                traceback.print_exc()
                print(f"Connection with web address {website} was not successful.")
            return None
        except requests.exceptions.ConnectionError as ce:
            if logger:
                logger.error("ConnectionError occurred in Web_Scraper.py get_soup().")
                logger.error(f"Web address {website} is not a valid URL.")
                logger.error(
                    "From Web_Scraper.py verify that parameter website is correct."
                )
            else:
                traceback.print_exc()
                print(f"Web address {website} is not a valid URL.")
                print("From Web_Scraper.py verify that parameter website is correct.")
            return None
        except requests.exceptions.RequestException as re:
            if logger:
                logger.error("RequestException occurred in Web_Scraper.py get_soup().")
                logger.error(
                    f"An ambiguous exception occurred while trying to connect to {website}."
                )
                logger.error(
                    f"From Web_Scraper.py investigate {type(re)} for request to {website}"
                )
            else:
                traceback.print_exc()
                print(
                    f"An ambiguous exception occurred while trying to connect to {website}."
                )
                print(
                    f"From Web_Scraper.py investigate {type(re)} for request to {website}"
                )
            return None

    @staticmethod
    def get_webpage_blocks(soup: BeautifulSoup, search_classes: dict) -> list:
        sorted_keys = sorted(search_classes.keys())
        return list(
            itertools.chain.from_iterable(
                soup.find_all("div", class_=search_classes[key]) for key in sorted_keys
            )
        )

    @staticmethod
    def get_article_titles(div_blocks: list) -> list:
        return [
            Web_Scraper.clean_string(div_block.find("a").find("h3").get_text())
            for div_block in div_blocks
        ]

    @staticmethod
    def get_article_links(div_blocks: list) -> list:
        return [div_block.find("a")["href"] for div_block in div_blocks]

    @staticmethod
    def yield_article_links(div_blocks: list):
        for link in Web_Scraper.get_article_links(div_blocks):
            yield link

    @staticmethod
    def get_article_submission_dates(div_blocks: list) -> list:
        return [
            div_block.find("time")["datetime"].split("T")[0] for div_block in div_blocks
        ]

    @staticmethod
    def yield_article_submission_dates(div_blocks: list):
        for date in Web_Scraper.get_article_submission_dates(div_blocks):
            yield date

    # Due to the possibility of an article not having a sub-description (which
    # consequently causes the list comprehession to raise an exception) this
    # function might need to be eliminated, but will be saved for now in case
    # it proves to be useful (but that is unlikely, so remove upon completing
    # development).
    @staticmethod
    def get_article_sub_descriptions(div_blocks: list) -> list:
        return [
            Web_Scraper.clean_string(
                div_block.find("a").find("h3").find_next_sibling("div").get_text()
            )
            for div_block in div_blocks
        ]

    @staticmethod
    def get_article_sub_description(div_block: str) -> str:
        try:
            return Web_Scraper.clean_string(
                div_block.find("a").find("h3").find_next_sibling("div").get_text()
            )
        except AttributeError as e:
            if str(e) == "'NoneType' object has not attribute 'get_text'":
                return ""
            else:
                raise AttributeError(e)

    @staticmethod
    def yield_article_sub_descriptions(div_blocks: list):
        for div_block in div_blocks:
            yield Web_Scraper.get_article_sub_description(div_block)

    @staticmethod
    def clean_string(text: str) -> str:
        return text.replace("\xa0", " ").replace("\u200a", " ")

    @staticmethod
    def scrape_website(
        website: str, search_classes: dict, logger: logging.Logger = None
    ) -> list:
        try:
            if not search_classes:
                raise MissingSearchClassesError("Parameter search_classes is empty.")
            soup = Web_Scraper.get_soup(website, logger)
            if soup:
                div_blocks = Web_Scraper.get_webpage_blocks(soup, search_classes)
                titles = Web_Scraper.get_article_titles(div_blocks)
                link_iterator = iter(Web_Scraper.yield_article_links(div_blocks))
                date_iterator = iter(
                    Web_Scraper.yield_article_submission_dates(div_blocks)
                )
                sub_desc_iterator = iter(
                    Web_Scraper.yield_article_sub_descriptions(div_blocks)
                )
                return [
                    {
                        "title": title,
                        "link": next(link_iterator),
                        "date": next(date_iterator),
                        "description": next(sub_desc_iterator),
                    }
                    for title in titles
                ]
            else:
                return []
        except (TypeError, AttributeError) as e:
            if logger:
                logger.error(
                    f"{type(e).__name__} occurred in {traceback.extract_tb(sys.exc_info()[2], -1)}"
                )
                logger.error(
                    f"Ensure that arguments passed to {traceback.extract_tb(sys.exc_info()[2], -1)} from scrape_website() are valid."
                )
            else:
                traceback.print_exc()
                print(
                    f"Ensure that arguments passed to {traceback.extract_tb(sys.exc_info()[2], -1)} from scrape_website() are valid."
                )
            return []
        except MissingSearchClassesError as e:
            if logger:
                logger.error(
                    f"MissingSearchClassesError occurred in scrape_website() for website: {website}"
                )
                logger.error(
                    f"Ensure that Website_Info.yaml is configured properly for {website}"
                )
            else:
                traceback.print_exc()
                print(
                    f"Ensure that Website_Info.yaml is configured properly for {website}"
                )
            return []
        except Exception as e:
            if logger:
                logger.error(
                    f"An unhandled exception occurred in Web_Scraper.py scrape_website() while scraping {website}"
                )
                logger.error(f"Update the file Web_Scraper.py to handle exception: {e}")
            else:
                traceback.print_exc()
                print(
                    f"An unhandled exception occurred in Web_Scraper.py scrape_website() while scraping {website}"
                )
                print(f"Update the file Web_Scraper.py to handle exception: {e}")
            return []

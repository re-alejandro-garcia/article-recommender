"""

    medium.py

    Description:

        This module contains the web scraping code used for scraping article 
        data for the latest posts from medium publications. The following 
        information is collected for each article: author, publication, title, 
        subtitle, article intro, date, read time, and url.

    Functions:

        get_latest_article_data(url)
        get_latest_posts_links(url)
        get_article_data(url)

"""

###############################################################################

import pandas as pd
import requests
from bs4 import BeautifulSoup

###############################################################################


def get_latest_article_data(url: str) -> pd.DataFrame:
    """
    Collect data for the latest articles posted on the medium publication
    referenced by the provided URL.

    Parameters
    ----------
    url: str
        The URL of the medium publication's latest posts page.

    Returns
    -------
    DataFrame:
        A pandas dataframe containing article data for the latest
        articles posted to the provided publication.
    """

    pass


###############################################################################


def get_latest_posts_links(url: str) -> list[str]:
    """
    Returns the URL links to 10 latest articles posted on the medium
    publication referenced by the provided URL.

    Parameters
    ----------
    url: str
        The URL of the medium publication's latest posts page.

    Returns
    -------
    list[str]:
        A list of URL links to the latest articles posted to the provided
        publication.
    """

    pass


###############################################################################


def get_article_data(url: str) -> dict:
    """
    Returns a dictionary containing all the data for the article referenced
    by the provided URL.

    Parameters
    ----------
    url: str
        The URL of the medium article.

    Returns
    -------
    dict:
        A dictionary containing the data for the provided article.
    """

    pass

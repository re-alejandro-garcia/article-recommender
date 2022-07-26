"""

    news.py

    Description:

        This module contains all code used for extracting article information
        with the News API. The following information is collected for each
        article: author, publication, title, subtitle, article intro, date,
        read time, and url.

    Functions:

        get_latest_article_data(*args)
        get_article_data(article)

"""

###############################################################################

import pandas as pd

# from newsapi import NewsApiClient

###############################################################################


def get_latest_article_data(*args) -> pd.DataFrame:
    """
    Collect data for the latest articles posted on a variety of publications
    through the use of the News API.

    Parameters
    ----------
    args: (optional)
        This parameter is provided only to allow for this function to be
        called in the same way web scraping functions are called.

    Returns
    -------
    DataFrame:
        A pandas dataframe containing article data for the latest
        articles posted to the provided publication.
    """

    pass


###############################################################################


def get_article_data(article: dict) -> dict:
    """
    Returns a dictionary containing all the information for the article
    dictionary passed as argument.

    Parameters
    ----------
    article: dict
        An article dictionary as returned by the News API.

    Returns
    -------
    dict:
        A dictionary with the article information properly organized and
        extracted for merging with the main article dataframe.
    """

    pass

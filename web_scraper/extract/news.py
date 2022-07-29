"""

    news.py

    Description:

        This module contains all code used for extracting article information
        with the News API. The following information is collected for each
        article: author, publication, title, subtitle, article intro, date,
        read time, and url.

    Functions:

        get_latest_article_data(url, publication, topic, api_key)
        get_news_page(news, topic, timestamp, url)
        get_article_data(articles)

"""

###############################################################################

import pandas as pd

from newsapi import NewsApiClient

###############################################################################


def get_latest_article_data(
    url: str, publication: str, topic: str, api_key: str = None
) -> pd.DataFrame:
    """
    Collect data for the latest articles posted on a variety of publications
    through the use of the News API.

    Parameters
    ----------
    url: str
        The URL of the publication to grab latest posts from. This is used if
        we want to get all the latest article from a specific publication.

    publication: str
        The name of the publication corresponding to the provided URL.

    topic: str
        The keyword(s) to search for when grabbing latest articles through
        the News API. This is used if we want to get all the latest articles
        that mention a specific topic.

    Returns
    -------
    DataFrame:
        A pandas dataframe containing article data for the latest
        articles posted to the provided publication.
    """

    # Initialize the article data dataframe.
    article_data = pd.DataFrame()

    # Initialize News API Client and get the last timestamp when data was
    # acquired.
    news = NewsApiClient(api_key=api_key)
    timestamp = None

    # For page yielded by the get_news_page function add the returned
    # dataframe to the article_data dataframe.
    for page in get_news_page(news, topic, timestamp, url):
        article_data = pd.concat([article_data, page]).reset_index(drop=True)

    return article_data


###############################################################################


def get_news_page(news, topic: str, timestamp: str, url: str) -> pd.DataFrame:
    """
    This function is a generator. Yield the article data for each page
    until reaching the final page for the given search parameters.

    Parameters
    ----------
    topic: str
        The keyword phrase to search for in the articles. The News API
        uses this as the q argument to search the contents of each article
        for the matching phrase.

    timestamp: str
        The timestamp in ISO 8601 format of the last time article data was
        acquired.

    url: str
        The URL of the publication to grab latest posts from. This is used if
        we want to get all the latest article from a specific publication.

    Returns
    -------
    DataFrame:
        A dataframe containing the article data for the yielded page.
    """

    # Start from page 1.
    page_number = 1

    # We'll keep going until reaching the final page.
    while True:

        # Grab 100 articles from the current page number.
        articles = news.get_everything(
            q=f'"{topic}"', from_param=timestamp, language="en", page=page_number
        )

        # If the page has less than 100 articles, we have reached the final
        # page.
        if len(articles["articles"]) < 100:
            break

        # Increment the page number and yield the results of get_article_data()
        page_number += 1
        yield get_article_data(articles)

    # Yield the results of get_article_data() for the final page.
    yield get_article_data(articles)


###############################################################################


def get_article_data(articles: dict) -> pd.DataFrame:
    """
    Returns a dictionary containing all the information for the article
    dictionary passed as argument.

    Parameters
    ----------
    articles: dict
        A dictionary of articles as returned by the News API.

    Returns
    -------
    DataFrame:
        A dataframe with the article information properly organized and
        extracted for merging with the main article dataframe.
    """

    # Initialize the article dataframe.
    article_df = pd.DataFrame(
        {
            "author": [],
            "publication": [],
            "title": [],
            "subtitle": [],
            "article_intro": [],
            "date": [],
            "read_time": [],
            "url": [],
        }
    )

    # For each article in the article dictionary acquire all the required data.
    # Join everything into the article dataframe
    for article in articles["articles"]:
        article_info = {}

        article_info["author"] = [article["author"]]
        article_info["publication"] = [article["source"]["name"]]
        article_info["title"] = [article["title"]]
        article_info["subtitle"] = [article["description"][:100]]
        article_info["article_intro"] = [article["content"]]
        article_info["date"] = [article["publishedAt"]]
        article_info["read_time"] = [None]
        article_info["url"] = [article["url"]]

        temp = pd.DataFrame(article_info)
        article_df = pd.concat([article_df, temp]).reset_index(drop=True)

    return article_df

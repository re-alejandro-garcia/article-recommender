"""

    medium.py

    Description:

        This module contains the web scraping code used for scraping article
        data for the latest posts from medium publications. The following
        information is collected for each article: author, publication, title,
        subtitle, article intro, date, read time, and url.

    Functions:

        get_latest_article_data(url, publication)
        get_latest_posts_links(url)
        get_article_data(url, publication)

"""

###############################################################################

import pandas as pd

import requests
from bs4 import BeautifulSoup

###############################################################################


def get_latest_article_data(url: str, publication: str) -> pd.DataFrame:
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

    # Initialize the article data dataframe.
    article_data = pd.DataFrame(
        {
            "author": [],
            "publication": [],
            "title": [],
            "subtitle": [],
            "article_intro": [],
            "date": [],
            "read_time": [],
            "url": [],
            "publication_url": [],
        }
    )

    links = get_latest_posts_links(url)

    # For each article link collect the data and combine the existing article
    # data dataframe with the data collected.
    for link in links:
        temp = pd.DataFrame(get_article_data(url, publication))
        article_data = pd.concat([article_data, temp]).reset_index(drop=True)

    return article_data


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

    # Get the HTML for the webpage with an HTTPS request and create the
    # soup object.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Gather all <a> elements with the relevant title value and get the href
    # and remove everything after '?source' since this stuff is not needed.
    links = soup.find_all("a", title="Latest stories published on Towards Data Science")
    return [link["href"].split("?source")[0] for link in links]


###############################################################################


def get_article_data(url: str, publication: str) -> dict:
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

    # Get the HTML for the webpage with an HTTPS request and create the
    # soup object.
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    article_info = {}

    # Collect all the data for the article that we need. The classes referring
    # to each data point are consistent across all Medium publications.
    article_info["author"] = [soup.find("div", class_="pw-author").div.div.div.a.text]
    article_info["publication"] = [publication]
    article_info["title"] = [soup.find("h1", class_="pw-post-title").text]
    article_info["article_intro"] = [
        soup.find("p", class_="pw-post-body-paragraph").text
    ]
    article_info["date"] = [soup.find("p", class_="pw-published-date").span.text]
    article_info["read_time"] = [soup.find("div", class_="pw-reading-time").text]
    article_info["url"] = [url]

    # Sometimes articles don't have a subtitle so we must check if there is a subtitle and
    # set the subtitle to an empty string if one doesn't exist.
    if (subtitle := soup.find("h2", class_="pw-subtitle-paragraph")) is None:
        article_info["subtitle"] = [""]
    else:
        article_info["subtitle"] = [subtitle.text]

    return article_info

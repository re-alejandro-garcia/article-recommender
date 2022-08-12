"""

    test_medium.py

    Description:

        This module contains all unit tests for the medium.py module in the
        web_scraper package.

    Variables:

        expected_output_get_article_data
        input_get_latest_posts_links
        input_get_latest_article_data

    Functions:

        test_get_article_data(url, publication, expected_output)
        test_get_latest_posts_links()
        test_get_latest_article_data()

"""

###############################################################################

import sys

sys.path.append("web_scraper/extract/")

import pytest
import medium
import re
import requests
import pandas as pd

###############################################################################

expected_output_get_article_data = [
    (
        "https://towardsdatascience.com/ai-can-now-play-minecraft-and-is-a-step-closer-to-navigate-the-world-1f19cfe37ef",
        "Towards Data Science",
        {
            "author": ["Alberto Romero"],
            "publication": ["Towards Data Science"],
            "title": [
                "AI Can Now Play Minecraft — A Step Closer to Navigate the World"
            ],
            "subtitle": ["The beginning of open-ended AI"],
            "article_intro": [
                "After building impressive models in language processing (GPT-3) and text-to-image generation (DALL·E 2), OpenAI is now facing an arguably greater challenge: open-ended action. In the great task of solving so-called artificial general intelligence (AGI), they realize language and vision aren’t the only domains in which AI should excel. GPT-3 and DALL·E 2 are extremely good at what they do, but as powerful as they are they remain constrained within the limited boundaries of their virtual worlds."
            ],
            "date": ["Jul 6"],
            "read_time": ["7 min read"],
            "url": [
                "https://towardsdatascience.com/ai-can-now-play-minecraft-and-is-a-step-closer-to-navigate-the-world-1f19cfe37ef"
            ],
        },
    ),
    (
        "https://betterprogramming.pub/how-i-negotiated-100k-from-google-370823b2c79c",
        "Better Programming",
        {
            "author": ["Sunny Beatteay"],
            "publication": ["Better Programming"],
            "title": ["How I Negotiated My Google Offer by $100K"],
            "subtitle": ["My tips for squeezing Big Tech offers for all they’re worth"],
            "article_intro": [
                "I’ll be the first to admit that I’ve never been great at negotiating. During my first job search, I choked during negotiations. I’d rather solve the coin change problem 100 times in a row than ask a recruiter for more money."
            ],
            "date": ["Jul 19"],
            "read_time": ["8 min read"],
            "url": [
                "https://betterprogramming.pub/how-i-negotiated-100k-from-google-370823b2c79c"
            ],
        },
    ),
    (
        "https://levelup.gitconnected.com/7-php-string-functions-you-should-know-and-how-to-use-them-c2727397158f",
        "Level Up Coding",
        {
            "author": ["Joshua Otwell"],
            "publication": ["Level Up Coding"],
            "title": ["7 PHP String Functions You Should Know and How To Use Them"],
            "subtitle": [""],
            "article_intro": [
                "Like I’m always saying, in today’s data landscape, you are going to process string and text data regularly. PHP has many many string functions built right into the language. Here are 7 of them you may not know about but should…"
            ],
            "date": ["Jul 20"],
            "read_time": ["6 min read"],
            "url": [
                "https://levelup.gitconnected.com/7-php-string-functions-you-should-know-and-how-to-use-them-c2727397158f"
            ],
        },
    ),
]

input_get_latest_posts_links = [
    (
        "https://towardsdatascience.com/latest",
        "Towards Data Science",
        "https://towardsdatascience.com/",
    ),
    (
        "https://betterprogramming.pub/latest",
        "Better Programming",
        "https://betterprogramming.pub/",
    ),
    (
        "https://levelup.gitconnected.com/latest",
        "Level Up Coding",
        "https://levelup.gitconnected.com/",
    ),
]

input_get_latest_article_data = [
    ("https://towardsdatascience.com/latest", "Towards Data Science")
]

###############################################################################


@pytest.mark.parametrize(
    "url, publication, expected_output", expected_output_get_article_data
)
def test_get_article_data(url: str, publication: str, expected_output: dict):
    """
    Run unit tests on medium.get_article_data(). Each test will compare the
    output to the expected output and check for an exact match.
    """

    assert medium.get_article_data(url, publication) == expected_output


###############################################################################


@pytest.mark.parametrize("url, publication, base_url", input_get_latest_posts_links)
def test_get_latest_posts_links(url: str, publication: str, base_url: str):
    """
    Run unit tests on medium.get_latest_posts_links(). Each test will check if
    the list of returned URLs is a valid set of URLs based on three conditions:
    (1) the base URL is present, (2) the base URL is followed by 1 or more
    characters, and (3) if we try obtaining a http request for the URL we get a
    200 status code.
    """

    links = medium.get_latest_posts_links(url, publication)
    regex = r".+"

    assert len(links) != 0

    for link in links:

        # Does the link contain the base URL?
        assert link.startswith(base_url)

        # Is the base URL followed by at least one character?
        assert re.match(regex, url.replace(base_url, "")) is not None

        # Does sending a request to this link return a status code of 200?
        resp = requests.get(link)
        assert resp.status_code == 200


###############################################################################


@pytest.mark.parametrize("url, publication", input_get_latest_article_data)
def test_get_latest_article_data(url, publication):
    """
    Run unit tests on medium.get_latest_article_data(). Since this function is
    dependent on the the get_latest_posts_links() and get_article_data()
    functions it will be assumed that if those functions have passed their
    tests then this function will be capable of passing its tests. A successful
    test for this function will consist of two checks: (1) does the function
    return a Pandas DataFrame, (2) the dataframe should contain 10 rows and 8
    columns.
    """

    df = medium.get_latest_article_data(url, publication, "")

    assert type(df) == pd.DataFrame
    assert df.shape == (10, 8)

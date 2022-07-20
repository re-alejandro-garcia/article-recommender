"""

    test_medium.py

    Description:

        This module contains all unit tests for the medium.py module in the
        web_scraper package.

    Variables:

        expected_output_get_article_data

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

###############################################################################


@pytest.mark.parametrize(
    "url, publication, expected_output", expected_output_get_article_data
)
def test_get_article_data(url, publication, expected_output):
    assert medium.get_article_data(url, publication) == expected_output


###############################################################################


def test_get_latest_posts_links():
    pass


###############################################################################


def test_get_latest_article_data():
    pass

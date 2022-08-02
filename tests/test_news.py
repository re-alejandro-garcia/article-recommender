"""

    test_news.py

    Description:

        This module contains all unit tests for the news.py module in the
        web_scraper package. Because certain functions in the news.py
        module are dependent an the use of an api key not all functions
        can be tested. In these cases test files containing test data are
        used in place of the function return value.

        The get_news_page function requires an api key meaning it would not
        be possible to automate testing of this function on Github. For this
        reason there is no unit test for get_news_page.

    Variables:

        Variable

    Functions:

        test_get_latest_article_data()
        test_get_article_data()

"""

###############################################################################

import sys

sys.path.append("web_scraper/extract/")

# import pytest
import news

###############################################################################


def test_get_article_data(news_test_input, news_test_output):
    """
    Run unit tests on news.get_article_data(). Each test will compare the
    output to the expected output and check for an exact match.
    """

    # It's important to drop the article_intro column because this column often
    # has special characters in the string value that don't play nicely with
    # the test data. So we want to ignore this column when determining if the
    # test was successful.
    # NOTE In a future iteration of this project this can possibly be modified
    # so that the special characters are removed as part of the acquisition
    # process.
    test_input = news.get_article_data(news_test_input).drop(columns="article_intro")
    test_output = news_test_output.drop(columns="article_intro")

    assert test_output.equals(test_input)

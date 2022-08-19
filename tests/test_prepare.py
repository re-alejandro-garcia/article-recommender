"""

    test_prepare.py

    Description:

        This module contains all unit tests for the prepare.py module in the
        web_scraper package.

    Functions:

        test_prepare_text_data()
        test_normalize_dates()
        test_prepare_read_time()
        test_prepare_article_data()

"""

###############################################################################

import sys

sys.path.append("web_scraper/prepare/")

# import pytest
import prepare

# import pandas as pd

###############################################################################


def test_prepare_text_data(prepare_text_data_input, prepare_text_data_output):
    """
    Run unit tests on prepare.prepare_text_data(). Each test will compare the
    output to the expected output and check for an exact match.
    """

    prepare_text_data_input = prepare.prepare_text_data(prepare_text_data_input)

    for i in range(len(prepare_text_data_input)):
        assert (
            prepare_text_data_input.iloc[i]["title"]
            == prepare_text_data_output.iloc[i]["title"]
        )
        assert (
            prepare_text_data_input.iloc[i]["subtitle"]
            == prepare_text_data_output.iloc[i]["subtitle"]
        )
        assert (
            prepare_text_data_input.iloc[i]["article_intro"]
            == prepare_text_data_output.iloc[i]["article_intro"]
        )


###############################################################################


def test_normalize_dates(normalize_dates_input, normalize_dates_output):
    """
    Run unit tests on prepare.normalize_dates(). Each test will compare the
    output to the expected output and check for an exact match.
    """

    assert prepare.normalize_dates(normalize_dates_input).equals(normalize_dates_output)


###############################################################################


def test_prepare_read_time(prepare_read_time_input, prepare_read_time_output):
    """
    Run unit tests on prepare.prepare_read_time(). Each test will compare the
    output to the expected output and check for an exact match.
    """

    assert prepare.prepare_read_time(prepare_read_time_input).equals(
        prepare_read_time_output
    )


###############################################################################


def test_prepare_article_data(prepare_article_data_input, prepare_article_data_output):
    """
    Run unit tests on prepare.prepare_article_data(). Each test will compare
    the output to the expected output and check for an exact match.
    """

    assert prepare.prepare_article_data(prepare_article_data_input).equals(
        prepare_article_data_output
    )

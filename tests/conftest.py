"""

    conftest.py

    Description:

        This module contains fixtures that are used in various unit tests with
        pytest.

    Fixtures:

        news_test_input()
        news_test_output()

"""

###############################################################################

import pytest
import json
import pandas as pd

###############################################################################


@pytest.fixture
def news_test_input() -> dict:
    with open("tests/test_files/test_news_get_article_data_input.json", "r") as file:
        data = json.loads(file.read())

    return data


###############################################################################


@pytest.fixture
def news_test_output() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/test_news_get_article_data_output.csv")
    return df


###############################################################################


@pytest.fixture
def prepare_text_data_input() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/prepare_text_data_input.csv")
    return df


###############################################################################


@pytest.fixture
def prepare_text_data_output() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/prepare_text_data_output.csv")
    return df


###############################################################################


@pytest.fixture
def normalize_dates_input() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/normalize_dates_input.csv")
    return df


###############################################################################


@pytest.fixture
def normalize_dates_output() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/normalize_dates_output.csv")
    return df


###############################################################################


@pytest.fixture
def prepare_read_time_input() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/prepare_read_time_input.csv")
    return df


###############################################################################


@pytest.fixture
def prepare_read_time_output() -> pd.DataFrame:
    df = pd.read_csv("tests/test_files/prepare_read_time_output.csv")
    return df

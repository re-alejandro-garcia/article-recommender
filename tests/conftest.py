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
def news_test_input():
    with open("tests/test_files/test_news_get_article_data_input.json", "r") as file:
        data = json.loads(file.read())

    return data


###############################################################################


@pytest.fixture
def news_test_output():
    df = pd.read_csv("tests/test_files/test_news_get_article_data_output.csv")
    return df

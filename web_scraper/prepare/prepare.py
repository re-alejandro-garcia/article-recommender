"""

    prepare.py

    Description:

        This module contains the code used for preparing the collected article
        data from all extract modules.

    Functions:

        prepare_article_data(df)
        prepare_text_data(df)
        normalize_dates(df)
        prepare_read_time(df)

"""

###############################################################################

# import numpy as np
import pandas as pd

# import unicodedata
# import re
# import datetime

###############################################################################


def prepare_article_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Perform all transformations necessary to prepare the article data
    for analysis and modeling.

    Parameters
    ----------
    df: DataFrame
        A pandas dataframe containing all the collected article data.

    Returns
    -------
    DataFrame:
        A pandas dataframe containing the transformed article data.
    """

    pass


###############################################################################


def prepare_text_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Prepares all text data in the article dataset, including the title,
    subtitle, and article intro of each article.

    Parameters
    ----------
    df: DataFrame
        A pandas dataframe containing all the collected article data.

    Returns
    -------
    DataFrame:
        A pandas dataframe with all text columns transformed.
    """

    pass


###############################################################################


def normalize_dates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts all dates in the article dataset into a uniform format.

    Parameters
    ----------
    df: DataFrame
        A pandas dataframe containing all the collected article data.

    Returns
    -------
    DataFrame:
        A pandas dataframe with all dates normalized.
    """

    pass


###############################################################################


def prepare_read_time(df: pd.DataFrame) -> pd.DataFrame:
    """
    For articles with a read time, the read time is converted into an
    value. For articles with no read time, the read time is calculated
    based on the length of the article.

    Parameters
    ----------
    df: DataFrame
        A pandas dataframe containing all the collected article data.

    Returns
    -------
    DataFrame:
        A pandas dataframe with read time prepared/estimated.
    """

    pass

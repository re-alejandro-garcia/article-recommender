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

import unicodedata
import re

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

    # Replace any nulls with an empty string.
    df["title"] = df["title"].fillna("")
    df["subtitle"] = df["subtitle"].fillna("")
    df["article_intro"] = df["article_intro"].fillna("")

    # Convert everything to lowercase.
    df["title"] = df["title"].apply(str.lower)
    df["subtitle"] = df["subtitle"].apply(str.lower)
    df["article_intro"] = df["article_intro"].apply(str.lower)

    # Normalize all characters to utf-8.
    normalize = (
        lambda column: unicodedata.normalize("NFKD", column)
        .encode("ascii", "ignore")
        .decode("utf-8", "ignore")
    )
    df["title"] = df["title"].apply(normalize)
    df["subtitle"] = df["subtitle"].apply(normalize)
    df["article_intro"] = df["article_intro"].apply(normalize)

    # Remove punctuation and special characters.
    replace_dash = lambda column: column.replace("-", " ")
    remove_special_characters = lambda column: re.sub(r"[^a-z0-9\s\+\#]", "", column)
    df["title"] = df["title"].apply(replace_dash).apply(remove_special_characters)
    df["subtitle"] = df["subtitle"].apply(replace_dash).apply(remove_special_characters)
    df["article_intro"] = (
        df["article_intro"].apply(replace_dash).apply(remove_special_characters)
    )

    return df


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

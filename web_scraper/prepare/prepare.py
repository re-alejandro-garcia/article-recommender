"""

    prepare.py

    Description:

        This module contains the code used for preparing the collected article
        data from all extract modules.

    Functions:

        prepare_article_data(df)
        prepare_text_data(df)
        replace_dash(string)
        replace_newline(string)
        remove_special_characters(string)
        normalize_dates(df)
        modify_date_string(date)
        prepare_read_time(df)

"""

###############################################################################

# import numpy as np
import pandas as pd

import unicodedata
import re
import datetime

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
    df["title"] = (
        df["title"]
        .apply(replace_dash)
        .apply(replace_newline)
        .apply(remove_special_characters)
    )
    df["subtitle"] = (
        df["subtitle"]
        .apply(replace_dash)
        .apply(replace_newline)
        .apply(remove_special_characters)
    )
    df["article_intro"] = (
        df["article_intro"]
        .apply(replace_dash)
        .apply(replace_newline)
        .apply(remove_special_characters)
    )

    return df


###############################################################################


def replace_dash(string: str) -> str:
    return string.replace("-", " ")


###############################################################################


def replace_newline(string: str) -> str:
    return string.replace("\n", " ")


###############################################################################


def remove_special_characters(string: str) -> str:
    return re.sub(r"[^a-z0-9\s\+\#]", "", string)


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

    df["date"] = df["date"].apply(modify_date_string)
    df["date"] = pd.to_datetime(df["date"]).dt.date
    return df


###############################################################################


def modify_date_string(date: str) -> str:
    """
    Convert the date string to a format that can be re-formatted by Pandas.

    Parameters
    ----------
    date: str
        A string representing a date.

    Returns
    -------
    str:
        A re-formatted date string.
    """

    if date.endswith("Z"):
        return date.replace("Z", "")
    elif re.match(r"[a-zA-Z]{3}\s[0-9]", date):
        return date + ", " + str(datetime.datetime.now().year)
    else:
        return date


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

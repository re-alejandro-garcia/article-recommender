import yaml
import os
import logging
import traceback


def get_email_credentials():
    login_credentials_file_path = os.path.join(
        os.path.dirname(os.getcwd()), "ExternalResources/AS_Login_Credentials.yaml"
    )
    login_credentials = dict()
    with open(login_credentials_file_path, "rt") as f:
        login_credentials = yaml.safe_load(f.read())
    return login_credentials["username"], login_credentials["password"]


def get_mailing_list() -> dict:
    mailing_list_file_path = os.path.join(
        os.path.dirname(__file__), "Mailing_List.yaml"
    )
    mailing_list = dict()
    with open(mailing_list_file_path, "rt") as f:
        mailing_list = yaml.safe_load(f.read())
    return list(mailing_list.keys())


def format_html_element(article: dict) -> str:
    return f'<a href="{article["link"]}">{article["title"]}</a>'

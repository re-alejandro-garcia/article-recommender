import logging
import traceback
import yagmail
from ArticleSuggestor.Email_Interface import Configure_Email


def send_email(article_info: list, logger: logging.Logger = None):
    username, password = Configure_Email.get_email_credentials()
    email_server = yagmail.SMTP(username, password)
    to = Configure_Email.get_mailing_list()
    subject = "Test"
    contents = [
        Configure_Email.format_html_element(article) for article in article_info
    ]
    email_server.send(to, subject, contents)

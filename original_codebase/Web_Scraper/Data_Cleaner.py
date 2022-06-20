# Clean data retrieved from the web scraper to be ready to use in the ML model

# May be better to store last viewed article as a dict for easier removal

import logging
import datetime


def remove_previously_viewed_articles(
    scraping_results: list, last_article_viewed: str, *, _logger: logging.Logger = None
):
    def index_of_last_viewed_article():
        for index, article in enumerate(scraping_results):
            if article.get("title") == last_article_viewed:
                return index
        else:
            return len(scraping_results)

    del scraping_results[index_of_last_viewed_article() :]


def remove_old_articles(
    scraping_results: list, current_date: str = None, *, _logger: logging.Logger = None
):
    if current_date:
        current_date = datetime.date.fromisoformat(current_date)
    else:
        current_date = datetime.date.today()

    one_day = datetime.timedelta(days=1)
    previous_day = current_date - one_day
    scraping_results[:] = [
        article
        for article in scraping_results
        if datetime.date.fromisoformat(article.get("date")) >= previous_day
    ]

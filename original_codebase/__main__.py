# App will scrape all provided sites up to last article viewed.
# : Check email for any updates and update scraper
# : Obtain dict with all scraping results

# All recently added articles will go through ML model to determine which should be suggested.
# All suggested articles will be emailed.
# Last article viewed is updated.

# Can receive email with update for ML model.
# Can receive email with new sites to scrape as well as articles to use with ML model.

# Save all raw data to a temporary file and re-save to a permanent upon request
# from an email. The temporary file is overwritten with each new download of raw data.

import logging
from .Web_Scraper import Data_Pipeline as dp
from .Configure_Logger import Configure_Logger as cl
from .Email_Interface import Email_Interface as ei

if __name__ == "__main__":
    cl.configure_logger()
    logger = logging.getLogger("ArticleSuggestor")

    # Read email for updating ML model
    # Read email for updating web scraper
    # Update Web Scraper
    article_info = dp.get_article_data(logger)
    # Run results through ML model
    ei.send_email(article_info, logger)

    logger.info("ArticleSuggestor script ran to completion.")

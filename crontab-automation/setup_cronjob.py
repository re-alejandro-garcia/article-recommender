"""
    setup_cronjob.py



    Description: 

        A script that configures crontab according to project specifications.
        The python-crontab package downloaded from pypi is used configure the 
        cronjob and write it. The cronjob created is named so that when 
        re-running this script any existing cronjob with the same name can be 
        removed before created the new cronjob.
"""

###############################################################################

# python-crontab: python -m pip install python-crontab
# Documentation: https://pypi.org/project/python-crontab/
from crontab import CronTab

from getopt import getopt, GetoptError
import sys

###############################################################################

# Get any command line arguments that may have been passed. The possible
# command line options are as follows:
# -a : setup the article recommender cronjob
# -w : setup the web scraper recommender cronjob
# -d : delete the selected cronjob
try:
    opts, args = getopt(sys.argv[1:], "awd", [])

    # Turn the received options into a set of all received options instead of
    # the default tuples returned by getopt.
    options = {opt[0] for opt in opts}

# If an invalid command line argument was received exit the script.
except GetoptError:
    print(f"Received invalid option/argument: {sys.argv[1 : ]}")
    sys.exit()

###############################################################################

# These are the commands that will be executed by crontab for running the
# article recommender app and the web scraper.
article_recommender_command = "execute article recommender (actual command pending)"
web_scraper_command = (
    "~/Repositories/article-recommender/shell-scripts/run-web-scraper.sh"
)

# These are the job names for each cronjob. These are used for finding and
# removing the command when being replaced.
article_recommender_job_name = "Article Recommender"
web_scraper_job_name = "Web Scraper"

# Run the jobs during the hours defined below.
article_recommender_hour_range = [21, 22]
web_scraper_hour_on = [0, 12, 18]
web_scraper_minute_on = [0]

# Run the job at the minutes defined below.
article_recommender_minute_on = [0, 30]

###############################################################################

# Setup the article recommender cronjob if the -a option was received.
if "-a" in options:
    with CronTab(user=True) as cron:

        # Remove any existing cronjob with the same name as job_name.
        job = cron.find_comment(article_recommender_job_name)
        cron.remove(job)

        # Write the new cronjob using the parameters defined above if the -d
        # option was not received.
        if "-d" not in options:
            job = cron.new(
                command=article_recommender_command,
                comment=article_recommender_job_name,
            )
            job.hour.during(*article_recommender_hour_range)
            job.minute.on(*article_recommender_minute_on)

###############################################################################

# Setup the web scraper cronjob if the -w option was received.
if "-w" in options:
    with CronTab(user=True) as cron:

        # Remove any existing cronjob with the same name as job_name.
        job = cron.find_comment(web_scraper_job_name)
        cron.remove(job)

        # Write the new cronjob using the parameters defined above if the -d
        # option was not received.
        if "-d" not in options:
            job = cron.new(command=web_scraper_command, comment=web_scraper_job_name)
            job.hour.on(*web_scraper_hour_on)
            job.minute.on(*web_scraper_minute_on)

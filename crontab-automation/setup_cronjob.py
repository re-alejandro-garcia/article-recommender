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

###############################################################################

# These are the commands that will be executed by crontab for running the
# article recommender app and the web scraper.
article_recommender_command = "execute article recommender (actual command pending)"
web_scraper_command = "execute web scraper (actual command pending)"

# These are the job names for each cronjob. These are used for finding and
# removing the command when being replaced.
article_recommender_job_name = "Article Recommender"
web_scraper_job_name = "Web Scraper"

# Run the jobs during the hours defined below.
article_recommender_hour_range = [21, 22]
web_scraper_hour_on = [0, 12, 18]

# Run the job at the minutes defined below.
article_recommender_minute_on = [0, 30]

###############################################################################

# Modify the crontab file of the current user.
with CronTab(user=True) as cron:

    # Remove any existing cronjob with the same name as job_name.
    job = cron.find_comment(article_recommender_job_name)
    cron.remove(job)

    # Write the new cronjob using the parameters defined above.
    job = cron.new(
        article_recommender_command=article_recommender_command,
        comment=article_recommender_job_name,
    )
    job.hour.during(*article_recommender_hour_range)
    job.minute.on(*article_recommender_minute_on)

###############################################################################

# Modify the crontab file of the current user.
with CronTab(user=True) as cron:

    # Remove any existing cronjob with the same name as job_name.
    job = cron.find_comment(web_scraper_job_name)
    cron.remove(job)

    # Write the new cronjob using the parameters defined above.
    job = cron.new(
        article_recommender_command=web_scraper_command, comment=web_scraper_job_name
    )
    job.hour.on(*web_scraper_hour_on)

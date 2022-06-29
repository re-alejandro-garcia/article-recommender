"""
    setup_cronjob.py



    Description: 

        A script that configures crontab according to project specifications.
        The python-crontab package downloaded from pypi is used configure the 
        cronjob and write it. The cronjob created is named so that when 
        re-running this script any existing cronjob with the same name can be 
        removed before created the new cronjob.
"""

################################################################################

# python-crontab: python -m pip install python-crontab
# Documentation: https://pypi.org/project/python-crontab/
from crontab import CronTab

################################################################################

# The cronjob will be setup to run the command below and it will be given the name
# assigned to job_name.
command = "echo hello"
job_name = "Article Recommender"

# Run the job during the hours defined below.
hour_range = [21, 22]

# Run the job at the minutes defined below.
minute_on = [0, 30]

################################################################################

# Modify the crontab file of the current user.
with CronTab(user=True) as cron:

    # Remove any existing cronjob with the same name as job_name.
    job = cron.find_comment(job_name)
    cron.remove(job)

    # Write the new cronjob using the parameters defined above.
    job = cron.new(command=command, comment=job_name)
    job.hour.during(*hour_range)
    job.minute.on(*minute_on)

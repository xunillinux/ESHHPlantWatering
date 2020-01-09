#!/usr/bin/env python3

from apscheduler.schedulers.blocking import BlockingScheduler

import logging
logging.basicConfig(filename='schedulerlogfile.log',level=logging.DEBUG)

from Handler.Handler import Handler

def startHandlerJob():
    handler.ExecuteAllSensors()

handler = Handler()

scheduler = BlockingScheduler()
scheduler.add_job(startHandlerJob,'cron', hour='*', max_instances=1)
scheduler.start()
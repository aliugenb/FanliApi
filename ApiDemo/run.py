# __author__ = Roger
# -*- coding: utf-8 -*-
import os
from datetime import datetime

from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
from apscheduler.schedulers.blocking import BlockingScheduler

import mail
from Fanli.createFile import CreateFile

#执行器
executors = {
    'default': ThreadPoolExecutor(10),
    'processpool': ProcessPoolExecutor(3),
}


def my_job():
    cur_day = datetime.now().strftime('%Y-%m-%d')
    cur_time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    report_path = '../Fanli/Report/' + cur_day + '/'
    path = '../Fanli/'
    result = os.system('nosetests '+path+' --with-html  --html-report='+report_path+'fanli_report_'+cur_time+'.html ')
    if result != 0:
        files = os.listdir(report_path)
        file = report_path + files[-1]
        mail.send_mail(file, 'getResouces接口Fail')


def create_json():
    CreateFile().create_file('getResource')

s = BlockingScheduler(executors=executors)
s.add_job(my_job, 'interval', seconds=5)
s.add_job(create_json, 'interval', seconds=5)

try:
    s.start()
except (SystemExit, KeyboardInterrupt):
    s.shutdown()


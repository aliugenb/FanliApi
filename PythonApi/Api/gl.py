# __author__ = Roger
# -*- coding: utf-8 -*-
import os

common_java = {'src': '1', 'v': '5.3'}
common_php = {'c_src': '1', 'c_v': '5.3'}
ios_header = {'User-Agent': 'Fanli/5.2.0.31 (iPhone; iPhone OS 9.3.4; zh_CN; ID:1-6798630-68696270745943-17-8)'}

and_header = {'User-Agent': 'Fanli/5.3.0.40 (nubia NX529J; Android 5.1.1; zh_CN; ID:2-6798630-62664606858404-1-0)'}


excel = '../file/demo1.xls'
report = '../file/Report'
if not os.path.exists(report):
    os.mkdir(report)

QuickEntry = '../file/QuickEntry.txt'
Clock = '../file/Clock.txt'


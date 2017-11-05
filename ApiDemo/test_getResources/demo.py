# -*- coding: utf-8 -*-
# __author__ = Roger
import requests
from Fanli.readConfig import ReadConfig
import checkDynamic
from Fanli import getResponse
import os
import json
from Fanli.getFile import GetFile

path = os.path.dirname(os.getcwd())
print path
match_path = path + '/Match/'
url = 'http://fun.fanli.com/api/mobile/getResource?key='
header = ReadConfig(path).get_header('ios')


keys = ['taobao_url_rule', 'webview_exception_monitor', 'taobao_app_key']
for key in keys:
    response = requests.get(url=url + 'key', headers=header, timeout=5)
    match_path = GetFile('getResource').get_file(key)
    match = open(match_path, 'r')
    match_data = match.read()
    json1_data = json.loads(match_data)
    json2_data

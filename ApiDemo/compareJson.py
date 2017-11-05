# -*- coding: utf-8 -*-
# __author__ = Roger
import json
import requests
from Fanli.readConfig import ReadConfig
from Fanli import getResponse
import os
import jsoncompare
import json_delta
import jsonschema
from Fanli.getFile import GetFile
import selenium

path = os.path.dirname(os.getcwd())
match_path = path + '/Fanli/Match/'
url = 'http://fun.fanli.com/api/mobile/getResource?key='
header = ReadConfig(path+'/Fanli/').get_header('ios')


keys = ['taobao_url_rule', 'webview_exception_monitor', 'taobao_app_key']
response = requests.get(url=url + 'webview_exception_monitor', headers=header, timeout=5)
match_path = GetFile('getResource').get_file('webview_exception_monitor')
match = open(match_path)
match_data = match.read()
match.close()
json2_data = json.loads(match_data)
# print json1_data
json1_data = getResponse.get_detail(response.json(),'')
# print json2_data
# print json1_data == json2_data
match.close()
# json2_data = {"$schema":"http://json-schema.org/draft-04/schema#","type":"object","properties":{"statuss":{"type":"integer"},"info":{"type":"string"},"data/webview_exception_monitor/updatetime":{"type":"string"},"data/webview_exception_monitor/content":{"type":"string"},"data/webview_exception_monitor":{"type":"object","properties":{"content":{"type":"string"},"updatetime":{"type":"string"}},"required":["content","updatetime"]},"data":{"type":"object","properties":{"webview_exception_monitor":{"type":"object","properties":{"content":{"type":"string"},"updatetime":{"type":"string"}}}},"required":["webview_exception_monitor"]}},"required":["statuss","info","data/webview_exception_monitor/updatetime","data/webview_exception_monitor/content","data/webview_exception_monitor","data"]}

# jsoncompare(json1_data,json2_data)
print 1111

# json_delta.diff(json1_data, json2_data)
try:
    jsonschema.validate(json1_data, json2_data)
except jsonschema.ValidationError as ex:
    # msg = ("HTTP response body is invalid (%s)") % ex
    # raise ex.message
    print ex
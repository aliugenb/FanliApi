# __author__ = Roger
# -*- coding: utf-8 -*-
import requests
from Fanli.readConfig import ReadConfig
import checkDynamic
from Fanli import getResponse

import json


class test_getResources(ReadConfig):

    def __init__(self):
        self.work_path = ReadConfig.work_path
        self.match_path = self.work_path + '/Match'
        self.url = 'http://fun.fanli.com/api/mobile/getResource?key='
        self.header = ReadConfig(self.work_path).get_header('ios')


    def setUp(self):
        print 'begin'

    def test_dynamic(self):
        response = requests.get(url=self.url + 'dynamic', headers=self.header, timeout=5)
        assert response.status_code == 200
        json_result = response.json()
        assert str(json_result['status']) == '1'
        data = getResponse.get_detail(json_result, '')
        checkDynamic.check_dynamic(data)

    def test_common(self):
        keys = ['taobao_url_rule', 'webview_exception_monitor', 'taobao_app_key']
        # for key in keys:
        #     response = requests.get(url=self.url + 'key', headers=self.header, timeout=5)
        #     match = open(self.match_path, 'a')
        #     match_data = match.read()
        #     print match
    def tearDown(self):
        print 'end'
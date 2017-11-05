# -*- coding: utf-8 -*-
# __author__ = Roger
from readConfig import ReadConfig
import requests
import getResponse
import json
from datetime import datetime
import os


class CreateFile(ReadConfig):

    def __init__(self):
        self.cur_day = datetime.now().strftime('%Y-%m-%d')
        self.work_path = ReadConfig.work_path

    def create_file(self, name):
        path = self.work_path + '/Match/' + name + '/' + self.cur_day + '/'
        if not os.path.exists(path):
            os.makedirs(path)
        keys = ReadConfig(self.work_path).get_keys(name)
        app_headers = ReadConfig(self.work_path).get_header('ios')
        urls = {'getResource': 'http://fun.fanli.com/api/mobile/getResource?key='}
        if name in urls.keys():
            for key in keys['unchange']:
                response = requests.get(urls[name] + key, headers=app_headers, timeout=5)
                match = getResponse.get_detail(response.json(), '')
                getResponse.tem = {}
                f = open(path + key + '.json', 'a')
                f.write(json.dumps(match))
                f.close()
        else:
            print u'这是啥url'


if __name__ == '__main__':
    CreateFile().create_file('getResource')
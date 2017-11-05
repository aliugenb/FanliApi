# -*- coding: utf-8 -*-
# __author__ = Roger
import re
import requests
import os
from Fanli.readConfig import ReadConfig
path = os.path.dirname(os.getcwd())
match_path = path + '/Fanli/Match/'
url = 'http://fun.fanli.com/api/mobile/getResource?key='
header = ReadConfig(path+'/Fanli/').get_header('ios')

tem = {}


def get_detail(data, path):
    global flag

    if isinstance(data, dict):

        for k, v in data.iteritems():
            if isinstance(v, dict):
                path1 = path+'/'+k
                get_detail(v, path1)

            elif isinstance(v, list):
                flag_tmp = path + '/' + k
                flag = re.sub(r'^/', '', flag_tmp)
                get_detail(v, flag)
            detail_k1 = path+'/'+k
            detail_k = re.sub(r'^/', '', detail_k1)
            tem[detail_k] = v

    elif isinstance(data, list):
        list_dict = {}
        for item in data:
            path2 = flag+'-'+str(data.index(item))
            list_dict[path2] = item
        get_detail(list_dict, '')

    return tem

if __name__ == '__main__':
    keys = ['taobao_url_rule', 'webview_exception_monitor', 'taobao_app_key']
    for key in keys:
        response = requests.get(url=url + key, headers=header, timeout=5)
        match = get_detail(response.json(), '')
        tem = {}
        print match
        print '------------------------------'

# -*- coding: utf-8 -*-
# __author__ = Roger
import requests
import logging
from Fanli import getImg
import json

# url = 'http://fun.fanli.com/api/mobile/getResource?key=dynamic&src=2&v=5.6.0.23'
# response = requests.get(url,  timeout=5)
# json_data = response.json()
# data = getResponse.get_detail(json_data, '')


def check_dynamic(response):
    if not response:
        return False
    else:
        if response['status'] != 1:
            return False
        else:
            check_pos(response, 'splash')
            check_pos(response, 'interstitial')


def check_pos(data, pos):
    if data['data/'+pos+'_infos/content'] == '[]':
        pass
    else:
        check_data = json.loads(data['data/'+pos+'_infos/content'])
        for item in check_data:
            # print item.keys()
            if pos == 'splash':
                image = item['fgFileUrl']
                if 'action' in item.keys():
                    action = item['action']
                    assert action['link']
                    assert action['type'] == '2'
            else:
                image = item['imgUrl']
                action = item['linkUrl']
            assert requests.get(image).status_code == 200
            assert getImg.get_image(image) < 1024


if __name__ == '__main__':
    print 111
    # print a
    # for k,v in a.iteritems():
    #     print '%s:%s'%(k,v)
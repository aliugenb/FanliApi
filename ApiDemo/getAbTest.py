# -*- coding: utf-8 -*-
# __author__ = Roger
import requests
from readConfig import ReadConfig


def get_abtest(host):
    k = ''
    ab_test = {}
    url = 'http://passport.fanli.com/mobileapi/i/device/update?lastappver=5.6.0.28&mc=17&jailbreak=0&idfa=FEC3234D-6436-42F0-8817-D5BEEB4C235B&verify_global=vdweznd9hikg2rko900j687yqa&nc=1&c_src=1&c_v=5.6.0.28&c_aver=3.0&devid=68696270745943&t=1481268545&c_sign=Af4l8Ix6dMoqj2y%2FW2Bw2dTJkdEqU2V7evyDv%2BJjSJLxds6zuANmh%2FxLoUcUFcbeKt1bDgWhbPm52bpobutGww%3D%3D'
    app_header = ReadConfig().get_header('ios')
    response = requests.get(url=url, headers=app_header, timeout=5)
    data = response.json()
    response.close()
    try:
        api_info = data['data']['abtest']['apiinfo']
    except TypeError:
        print data['info']
        return
    ab_devid = data['data']['abtest']['d']
    ab_uid = data['data']['abtest']['u']
    ab_info = ab_devid + ab_uid
    # for api in api_info:
    #     if api['url'] == host:
    #         k = str(api['k'])
    # for ab in ab_info:
    #     if k in ab['va'].split(','):
    #         ab_test[ab['s']] = ab['g']
    for api in api_info:
        for ab in ab_info:
            if api['url'] == host:
                k = str(api['k'])
                if k in ab['va'].split(','):
                    ab_test[ab['s']] = ab['g']
    return ab_test

if __name__ == '__main__':
    host = 'fun.fanli.com/api/mobile/getResource'
    print get_abtest(host)
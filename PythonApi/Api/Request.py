# __author__ = Roger
# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import gl
from Excel import HandleExcel
from VerifyJson import VerifyJson


class RequestUrl:

    def __init__(self):
        self.obj = HandleExcel()
        self.header = gl.ios_header
        self.rows = self.obj.get_urls()
        self.row_names = self.obj.get_first_row()

    def request_url(self, n=0):
        start_time = datetime.now()
        params = {}
        for num in self.rows.keys():
            req_url = self.rows[num][self.row_names.index('接口名')].encode('utf-8')
            if self.rows[num][self.row_names.index('请求参数')]:
                params = eval(self.rows[num][self.row_names.index('请求参数')].encode('utf-8'))
            n += 1

            try:
                response = requests.get(req_url, headers=self.header, params=params, timeout=5)
                response.raise_for_status()
            except requests.Timeout, e:
                self.obj.write_msg(num, e.__str__())
                self.obj.write_result(num, 'Fail')
            except requests.RequestException, e:
                self.obj.write_msg(num, e.__str__())
                self.obj.write_result(num, 'Fail')
            else:
                if response.status_code == 200:
                    print response.url
                    if req_url == response.url:
                        self.obj.write_code(num, 200)
                    else:
                        self.obj.write_code(num, 302)
                    json_result = response.json()
                    if str(json_result['status']) == '1':
                        verify_result = VerifyJson().verify_json(req_url, json_result)
                        self.obj.write_result(num, verify_result)
                    elif str(json_result['status']) == '0':
                        info = json_result['info']
                        # 写入报错信息,返回的json及结果
                        self.obj.write_msg(num, info)
                        self.obj.write_json(num, response.text)
                        self.obj.write_result(num, u'接口内部错误')
            print '第'+''+str(n)+''+'轮,测试:'+'\n'+''+req_url+''
        self.obj.save_response()
        end_time = datetime.now()
        print '执行测试共花费了'+''+str((end_time-start_time).seconds)+''+'s'
if __name__ == '__main__':
    obj1 = RequestUrl()
    # for i in range(1, 5):
    obj1.request_url()
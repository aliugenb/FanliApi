# __author__ = Roger
# -*- coding: utf-8 -*-

import xlrd
from xlutils import copy
import os
import gl


class HandleExcel:

    def __init__(self):
        self.excel = xlrd.open_workbook(gl.excel, formatting_info=True)
        self.sheet = self.excel.sheet_by_index(0)
        self.new_excel = copy.copy(self.excel)
        self.new_sheet = self.new_excel.get_sheet(0)

    def get_first_row(self):
        first_row = self.sheet.row_values(0)
        row_values = []
        for row in first_row:
            row_value = row.encode('utf-8')
            row_values.append(row_value)
        return row_values

    def get_urls(self):
        # urls = {}
        rows = {}
        for i in range(1, self.sheet.nrows):
            row = self.sheet.row_values(i)
            rows[i] = row
            # result有值不会再放入请求url
            for k in rows.keys():
                if rows[k][self.get_first_row().index('result')]:
                    del rows[k]
        # for num in rows.keys():
        #     api = rows[num][self.get_first_row().index('接口名')].encode('utf-8')
        #     parameters = rows[num][self.get_first_row().index('请求参数')].encode('utf-8')
        #     # eval处理后类型为dict
        #     p = eval(parameters)
        #     c = ''
        #     for a in p.keys():
        #         b = '%s=%s' % (a, p[a])
        #         c = b + '&' + c
        #     # 去除最后多余&
        #     parameter = re.sub(r'&$','',c)
        #     # parameter = c[:-1]
        #     url = api + parameter
        #     urls[num] = url
        if len(rows.keys()) == 0:
            print '没有要待测试的接口,请检查录入的接口result一栏是否为空'
        else:
            print '共录入待测接口' + '' + str(len(rows.keys())) + '' + '条'
        return rows

    def write_api(self, num, api):
        self.new_sheet.write(num, self.get_first_row().index('接口名'), api)

    def write_parameters(self, num, parameters):
        self.new_sheet.write(num, self.get_first_row().index('请求参数'), parameters)

    def write_code(self, num, code):
        self.new_sheet.write(num, self.get_first_row().index('status code'), code)

    def write_msg(self, num, msg):
        self.new_sheet.write(num, self.get_first_row().index('msg'), msg)

    def write_result(self, num, result):
        self.new_sheet.write(num, self.get_first_row().index('result'), result)

    def write_json(self, num, re_json):
        self.new_sheet.write(num, self.get_first_row().index('返回json'), re_json)

    def save_response(self):
        os.remove(gl.excel)
        self.new_excel.save(gl.excel)


if __name__ == '__main__':
    obj = HandleExcel()
    obj.get_urls()

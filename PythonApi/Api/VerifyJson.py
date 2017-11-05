# __author__ = Roger
# -*- coding: utf-8 -*-
import gl
import json
from Traversal import TraversalJson
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class VerifyJson:
    def __init__(self):
        self.reference = open(gl.QuickEntry, 'r')
        self.cur_day = datetime.now().strftime('%Y-%m-%d')
        self.cur_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.report = open(gl.report+'/Report-'+self.cur_day+'.txt', 'a')

    def verify_json(self, req_url, json_result):
        self.report.write('Request:' + '\n' + req_url)
        self.report.write('\n')
        self.report.write(self.cur_time)
        self.report.write('\n')
        # 待测数据
        ori_dict = TraversalJson().traversal_json(json_result)
        # 验证标准
        references = json.loads(self.reference.read())
        reference_dict = TraversalJson().traversal_json(references)
        verify_result = ''
        if cmp(ori_dict, reference_dict) == 0:
            print 'pass1'
            verify_result = 'pass'
            self.report.write('pass'+'\n'+'\n'+'\n')
        else:
            if cmp(ori_dict.keys(), reference_dict.keys()) == 0:
                for key in ori_dict.keys():
                    if isinstance(ori_dict[key], type(reference_dict[key])):
                        verify_result = 'pass'
                        # self.file.write('测试通过'+'\n'+'\n'+'\n')
                    else:
                        self.report.write('测试数据类型错误'+'\n'+'\n'+'\n')
                        # result = '%s:%s'%(key,a[key])
                        self.report.write('%s:%s'%(key,ori_dict[key])+'\n'+'\n'+'\n')
                        self.report.write('%s:%s' % (key, reference_dict[key])+'\n'+'\n'+'\n')
                        verify_result = 'Fail'
            else:
                # lack_key = list(set(cmp_schema.keys()).difference(set(a.keys())))
                self.report.write(u'与验证标准对比,测试数据缺少以下节点:'+'\n' + '\n'.join(list(set(reference_dict.keys()).difference(set(ori_dict.keys()))))+'\n'+'\n'+'\n'+'\n')
                verify_result = 'Fail'
        self.report.close()
        return verify_result

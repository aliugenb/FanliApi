# __author__ = Roger
# -*- coding: utf-8 -*-
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ReadConfig:

    work_path = os.path.dirname(__file__)

    def __init__(self, path):
        # self.config = open('/Users/Roger/Documents/Python/Fanli/Conf/config.txt', 'r').read()
        self.config = open(path + '/Conf/config.txt', 'r').read()

    def get_header(self, app_os):
        header = re.search(r'(?:'+app_os+'_header)=(.*)', self.config, re.M | re.I)
        app_header = eval(header.group(1))
        return app_header

    def get_keys(self, pos):
        keys = re.search(r'(?:'+pos+'_keys)\s*=\s*(.*)', self.config, re.M | re.I)
        app_keys = eval(keys.group(1))
        return app_keys


if __name__ == '__main__':
    parent_path = os.path.dirname(__file__)
    obj = ReadConfig(parent_path)
    print obj.get_header('and')
    print obj.get_keys('getResource')


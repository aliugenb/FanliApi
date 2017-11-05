# __author__ = Roger
# -*- coding: utf-8 -*-
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class ReadConfig:

    def __init__(self):
        self.config = open('../File/config.txt', 'r').read()
        
    def get_excel(self):
        excel = re.search(r'excel=(\S*)', self.config, re.M | re.I)
        return excel.group(1)

    def get_report(self):
        report = re.search(r'report=(\S*)', self.config, re.M | re.I)
        return report.group(1)

    def get_header(self):
        header = re.search(r'(.*\S.header)=(.*)', self.config, re.S | re.I)
        # return header.group(2)


if __name__ == '__main__':
    obj = ReadConfig()
    # for i in range(1, 5):
    print obj.get_header()

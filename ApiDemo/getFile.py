# -*- coding: utf-8 -*-
# __author__ = Roger
from Fanli.readConfig import ReadConfig
import os


class GetFile(ReadConfig):

    def __init__(self, test_key):
        self.work_path = ReadConfig.work_path
        self.dir_path = self.work_path + '/Match/' + test_key

    def get_file(self, filename):
        file_path = ''
        filename_list = os.listdir(self.dir_path)
        dir_path = self.dir_path + '/' + filename_list[-1]
        file_list = os.listdir(dir_path)
        for file in file_list:
            if file.find(filename)==0:
                file_path = dir_path + '/' + file
                break
        return file_path

if __name__ == '__main__':
    print GetFile('getResource').get_file('taobao_app_key')

#-*- coding: UTF-8 -*- 
'''
Created on 2016年8月1日

@author: ye.liu
'''

import os
import time


curTime = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
os.popen('adb devices')
os.system('adb shell /system/bin/screencap -p /sdcard/screenshot.png')
time.sleep(1)
os.system('adb pull /sdcard/screenshot.png %USERPROFILE%/Desktop/screenshot-'+curTime+'.png')
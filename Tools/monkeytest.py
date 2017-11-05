#-*- coding: UTF-8 -*- 
import os

apk = {'fanli':'com.fanli.android.apps','pro':'com.fanli.android.superfan.apps'}
test_apk = raw_input('which package you want\nfanli or young:')
apk_name = apk[test_apk]
event_num = raw_input('How many pseudo random events(-v) do you want?\nenter int num:')
if event_num.isdigit() and int(event_num)>0:
	print 'OK,your events are '+event_num
else:
	print 'Please enter a number and the number>0'
touch_num = raw_input('How much you need to click on the probability\nenter int num:')
if touch_num.isdigit() and int(touch_num)>0:
	print 'OK,your touch_num are '+touch_num
else:
	print 'Please enter a number and the number>0'
trackball_num = raw_input('How much is the probability you need to slide\nenter int num:')
if trackball_num.isdigit() and int(trackball_num)>0:
	print 'OK,your tralkball_num are '+ trackball_num
else:
	print 'Please enter a number and the number>0'
total_num = int(touch_num) +int(trackball_num)
'''print total_num'''
if int(total_num)<100:
	print 'OK,You will be able to A monkey test.'
else:
	print 'total_num can not More than 100 ,and the program will be closed, then you should start again!'
	os._exit(0)
#check the input value
for_time = raw_input('How many times monkey test do you want?\ntimes(>1:')
if for_time.isdigit() and int(for_time)>1:
	print 'OK,you want to loop' + for_time + 'times monkey test'
else:
	print 'Please enter a number and the number >1' 
#the log path
log_path = 'D:\\'
#the log name
log_name = 'Monkeytestlog.txt'
#monkey_shell script
monkey_shell = 'adb shell monkey -v -v  -v -p ' + apk_name +' '+'--pct-touch'+' '+touch_num+' '+'--pct-trackball'+' '+trackball_num+' '+'--throttle'+' '+'300'+' ' +event_num + '>' + log_path
def monkeytest():
	print 'now let \'s check your phone'
phonedevice = os.popen('adb devices').read()
if phonedevice.strip().endswith('device'):
	print 'OK,you phone get ready,let\'s start monkey test!'
	for i in range (1,int(for_time)+1):
		print 'The',i,'Monkey test starting...' 
		print os.popen(monkey_shell +str(i) + log_name)
		print i,'complete!'
	print 'OK,monkey test all complete!The log is in D:\\'
else:
	print 'please chek your phone has linked your computer well'
#find 'adb' connand at your os
	sysPath = os.environ.get('PATH')
	if not sysPath.find('platform-tools'):
		print '''please install the android-sdk and put the 'platform-tools' dir in your system PATH'''
	else:
#kill the 'tadb.exe'
		tadb = os.popen('tasklist').read()
		if tadb.find('tadb.exe') !=-1:
			print 'Find \ tadb.exe\' ,it must be killed!!!'
			os.system('taskkill /im tadb.exe /F')
			print 'OK,the \'tadb\' has been killed,let\'s go on'
			monkeytest()
		else:
			print 'not find \'tadb.exe\',great!go on!'
			monkeytest()

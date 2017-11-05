#coding:utf-8
import requests
import json
import xlrd
import os
from xlutils.copy import copy

excel = 'apidemo.xls'   #定义存放用例的excel路径，当前路径下
data = xlrd.open_workbook(excel)
host = 'http://xxxxxxx/api'#测试服,这个自己写吧
headers = {'Accept-Version':'v2','content-type': 'application/json'}  #定义headers

result = []  #用来存放验证结果
responseValue = []  #存放返回的数据
table = data.sheet_by_index(0)
nrow = table.nrows  #获取行数
for i in range(1,nrow): #循环获取每行中的数据
    requestMethod = table.cell(i,2).value   #方法，post、get、delete
    url = host + table.cell(i,1).value  #拼接url
    payload = table.cell(i,3).value #定义要传的值
    ex = table.cell(i,4).value  #获取期望的返回值，目前是用status_code来判断
    if requestMethod == 'get':  #不同的方法发不同的请求
        r = requests.get(url,headers = headers)
    elif requestMethod == 'post':
        r = requests.post(url,data = payload,headers = headers)
    elif requestMethod == 'delete':
        r = requests.delete(url,data = payload,headers = headers)
    if r.status_code == ex:  #如果和期望值一样，case通过
        result.append('true')
        if 'message' in r.json().keys():  #这个看情况而定吧，这边例如账号密码错误也是在message里的
            responseValue.append(r.json()['message'])  #将message先存入response
        else:
            responseValue.append('')
    else:
        result.append('false') #如果结果不对的话，如果有message就写，没有就全部写入
        if 'message' in r.json().keys():
            responseValue.append(r.json()['message'])
        else:
            responseValue.append(json.dumps(r.json(),ensure_ascii=False))  
    r.close()
    print('共有%d个url，当第%d个执行完毕'%(nrow-1,i))
book = copy(data)
sheet1 = book.get_sheet(0)  #copy原来的excel
for j in range(1,nrow):#将结果写入到对应的表格中  #将结果和response都写入到复制的工作表中
    sheet1.write(j,5,result[j-1])
    sheet1.write(j,6,responseValue[j-1])
os.remove(excel)
book.save(excel)    #移除原来的excel，保存新的excel
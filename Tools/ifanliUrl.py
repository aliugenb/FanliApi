# __author__ = Roger
# -*- coding: utf-8 -*-
import urlparse
import urllib
import platform


sysos = platform.system()
if sysos == 'Windows':
    input_url = raw_input("输入需要转换的url\n".decode('utf-8').encode('gbk'))
elif sysos == 'Darwin':
    input_url = raw_input("输入需要转换的url\n")
else:
    pass
# 删除空格
# url = input_url.replace(' ', '')


def is_space(s):
    return s and len(s.strip()) > 0

url = filter(is_space, input_url)
print "\n\n"

ifanli = 'ifanli://m.51fanli.com/app/show/web?url='

if url:
    print u"你输入的url是:\n", url, "\n\n"
    parsedTuple = urlparse.urlparse(url)
    url_schema = parsedTuple.scheme
    url_netloc = parsedTuple.netloc
    url_path = parsedTuple.path

    if 'http' in url_schema or 'https' in url_schema:
        ifanli_url = urllib.quote(url, '')
        if 'fanli.com' in url_netloc:
            if '/goshop/go' in url_path:
                ifanli = ifanli + ifanli_url + '&style=2'
                print u"输入的链接是goshop链接\nifanli链接:\n",ifanli
            else:
                ifanli = ifanli + ifanli_url
                print u"输入的链接是内站链接\nifanli链接:\n",ifanli
        else:
            ifanli = ifanli + ifanli_url + '&style=2'
            print u"输入的链接是外站链接\nifanli链接:\n",ifanli

    elif 'ifanli' in url_schema:
        print u"输入的已是ifanli链接,不需要进行转换\nifanli链接:\n",url
    else:
        print u"链接不合法,请输入以http、https或者ifanli开头的链接"
else:
    print u"未输入url"

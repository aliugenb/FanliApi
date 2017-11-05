# __author__ = Roger
# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

# 输入Email地址和口令:
from_addr = 'yeliu89@sina.com'
password = 'z15861802243'
# 输入收件人地址:
to_addr = 'ye.liu@fanli.com'
# 输入SMTP服务器地址:
smtp_server = 'smtp.sina.com'


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_mail(file, subject):
    # msg = MIMEText('hello', 'html', 'utf-8')
    msg = MIMEMultipart()
    msg['From'] = _format_addr('测试<%s>'%from_addr)
    msg['To'] = _format_addr('返利<%s>'%to_addr)
    msg['Subject'] = Header(subject, 'utf-8')

    msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

    with open(file, 'rb') as f:
        mime = MIMEBase('html', 'html', filename='report.html')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='report.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)

    try:
        server = smtplib.SMTP(smtp_server, 25)
        # server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
        print u'邮件发送成功'
    except smtplib.SMTPException, e:
        print e
        print u'邮件发送失败'

if __name__ == '__main__':
    send_mail()
# 파이썬으로 이메일 보내기 실습

import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD :')


# to_email_list = ['email1', 'email2', 'email3'] #여러명에게 이메일 보내기


# for email in to_email_list: (for i in is)
    msg = EmailMessage()
    msg['Subject'] = 'Hello from SSAFY DJ ROOM-2'
    msg['From'] = 'dltmddpdl0@naver.com'
    msg['To'] = 'lee.seunghyun0343@gmail.com' #email
    msg.set_content('lets get some lunch!'

    ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
    ssafy.login('dltmddpdl0', password)
    ssafy.send_message(msg)

print('email sent!')


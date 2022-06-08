#이메일 보내기
import smtplib
from email.mime.text import MIMEText
me = 'abc@server.kr'
you = 'def@server.com'
contents = '12월에 동창회가 있으니 참여 바람'

msg = MIMEText(contents, _charset='euc-kr')
msg['Subject'] = '동창회 모임'
msg['From'] = me
msg['To'] = you

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()

server.login("자신의 아이디", "패스워드")

server.sendmail(me, you, msg.as_string())
server.quit()
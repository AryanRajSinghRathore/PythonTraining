import smtplib
from email.message import EmailMessage
##f = open('password.txt')
##my_pass = f.read()

msg = EmailMessage()
msg['Subject'] = 'Python Training'
msg['From'] = 'rathoretanmay1234@gmail.com'
msg['To'] = 'aryanarya1142003@gmail.com'
msg.set_content('MOTA MANAKTALLA')

server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('rathoretanmay1234@gmail.com',password='yjjucgxiovkzesik')
server.send_message(msg)
server.quit()

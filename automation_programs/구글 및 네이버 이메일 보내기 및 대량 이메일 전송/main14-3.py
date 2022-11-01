import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

send_email = "jkim734@gmail.com"
send_pwd = "xebflneigyjbfoph"

recv_email = "kbt8832@naver.com"

smtp_name = "smtp.gmail.com"
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = '첨부파일 테스트입니다.'
msg['From'] = send_email
msg['To'] = recv_email

text = """
첨부파일 메일 테스트 내용입니다.
"""
contentPart = MIMEText(text)
msg.attach(contentPart)

etc_file_path = r'/workspaces/python_40projects/automation_programs/구글 및 네이버 이메일 보내기 및 대량 이메일 전송/Worlds 2021 - Commercial Break - December Night.mp4'
with open(etc_file_path, 'rb') as f:
    etc_part = MIMEApplication(f.read())
    etc_part.add_header("Content-Disposition", 'attachment', filename='Worlds 2021 - Commercial Break - December Night.mp4')
    msg.attach(etc_part)

s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()
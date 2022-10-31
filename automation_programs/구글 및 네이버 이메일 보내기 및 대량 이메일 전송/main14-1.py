#네이버 메일을 보내는 코드 만들기
import smtplib
from email.mime.text import MIMEText

send_email = "appleallway@naver.com"
send_pwd = "appleman"

recv_email = "stellajsy07@gmail.com"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = """
Hold my hand, everything will be okay
내 손을 잡아, 모든 게 괜찮아질 거야.

I heard from the heavens that clouds have been gray
날이 어두워질 거라고 하늘을 통해 들었어
Pull me close, wrap me in your aching arms
날 가까이 끌어당겨 너의 아픈 팔로 감싸줘

I see that you're hurting, why'd you take so long
네가 이렇게 상처를 받는데 왜 이렇게 오래 걸린 거야

To tell me you need me? I see that you're bleeding
내가 필요하다고 말해줘 지금 피를 흘리고 있잖아

You don't need to show me again
나한테 다시 보여주지 않아도 되지만

But if you decide to, I'll ride in this life with you
하지만 네가 결정한다면, 난 너와 함께 이 삶을 살 거야.

I won't let go 'til the end
난 널 끝까지 놓지 않을 테니

So, cry tonight
그러니 오늘 밤은 울어도 돼

But don't you let go of my hand
대신 내 손은 절대 놓지 마

You can cry every last tear
울고 싶은 만큼 울어도 돼

I won't leave 'til I understand
널 전부 이해하기 전엔 떠나지 않겠다고

Promise me, just hold my hand
약속해줘, 그냥 내 손을 잡아.
"""

msg = MIMEText(text)

msg['Subject'] = "세상의 고단함에 지친 당신에게"
msg["From"] = send_email
msg["To"] = recv_email
print(msg.as_string())

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()

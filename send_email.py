import smtplib
from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# 이메일 로그인 계정 입력
sender = ' '
password = ' ' # 구글이면 앱 비밀번호


# 수신자 이메일 입력
receiver = ' '



mail_type = 'smtp.gmail.com' # 타입 수정
port = 587          # or 467 587// 포트번호 찾아서 수정

# 계정 세션 설정
smtp = smtplib.SMTP(mail_type, port)
smtp.set_debuglevel(True)



# smtp 계정 인증 설정
smtp.ehlo()
smtp.starttls()
smtp.login(sender, password) # 로그인



#이메일 데이터 설정
msg = MIMEText('메일내용입니다')
msg['Subject'] = '안녕하세요'
msg['Form'] = sender  # 발신자
msg['To'] = receiver  # 수신자



#메일 전송
smtp.sendmail(sender, receiver, msg.as_string())

smtp.quit()


# multipart사용해서 html로 메일내용 작성 가능















import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 이메일 로그인 계정 입력
sender = ""
password = ""


# 수신자 이메일 입력
receiver = ""

def smtp_setting(email, password):

    mail_type = 'smtp.gmail.com' # 타입 수정
    port = 587                   # or 465 // 포트번호 찾아서 수정

    
    # 계정 세션 설정
    smtp = smtplib.SMTP(mail_type, port)
    smtp.set_debuglevel(True)

    # smtp 계정 인증 설정
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email, password) # 로그인

    return smtp


def send_plain_mail(sender, receiver, email, password, subject, content):
    try:

        #smtp 세션 생성
        smtp = smtp_setting(email, password)

        #이메일 데이터 설정
        msg = MIMEText(content)
        msg['Subject'] = subject
        msg['Form'] = sender  # 발신자
        msg['To'] = receiver  # 수신자

        #메일 전송
        smtp.sendmail(sender, receiver, msg.as_string())
    except Exception as e:
        print('error', e)

    finally:
        if smtp is not None:
            smtp.quit()


# 메일 내용 작성하기
send_plain_mail(sender, receiver, sender, password, '안녕하세요', '메일내용입니다')


# multipart사용해서 html로 메일내용 작성 가능














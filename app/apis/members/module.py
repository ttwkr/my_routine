import smtplib
from email.mime.text import MIMEText
from app.core.config import settings


class Verification:
    def __init__(self):
        self._mail = settings.MASTER_MAIL
        self._password = settings.MASTER_MAIL_PW

    def send_mail(self, code: str, mail: str):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(self._mail, self._password)

        msg = MIMEText(code)
        msg['Subject'] = '[마이루틴]인증메일 입니다.'
        msg['To'] = mail
        smtp.sendmail(self._mail, mail, msg.as_string())

        smtp.quit()

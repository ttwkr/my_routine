from app.core.config import settings


class Verification:
    def __init__(self):
        self._mail = settings.MASTER_MAIL
        self._password = settings.MASTER_MAIL_PW

    def send_mail(self):
        pass
from sqlalchemy.orm import Session

from app.database.models.members import EmailVerificationModel


class EmailVerifications:
    def __init__(self, db: Session):
        self._db = db

    def save(self, instance: EmailVerificationModel):
        self._db.add(instance)
        self._db.commit()

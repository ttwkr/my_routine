from sqlalchemy.orm import Session


class Verification:
    def __init__(self, db: Session):
        self._db = db



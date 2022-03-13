from db.core import Session


class DbSession:

    @staticmethod
    def create():
        return Session()

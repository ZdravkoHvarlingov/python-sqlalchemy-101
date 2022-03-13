import model
from db.core import Base, engine


def create_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_db()

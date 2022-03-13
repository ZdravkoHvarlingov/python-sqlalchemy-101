from db.core import Base, engine

from model.customer import Customer
from model.car import Car
from model.manufacturer import Manufacturer
from model.purchase import Purchase


def create_db():
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    create_db()

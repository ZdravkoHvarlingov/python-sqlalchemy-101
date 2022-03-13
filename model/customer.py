from db.core import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, UniqueConstraint


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    family_name = Column(String(255))
    age = Column(Integer)

    purchases = relationship('Purchase', back_populates='customer')

    def __init__(self, name, family_name, age):
        self.name = name
        self.family_name = family_name
        self.age = age

    __table_args__ = (UniqueConstraint('name', 'family_name', name='_name_family_name_uc'),)

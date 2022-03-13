from db.core import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, Date


class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, autoincrement=True)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id', ondelete='CASCADE'), nullable=False)
    model = Column(String(255))
    base_price_in_coins = Column(BigInteger)
    release_date = Column(Date)

    manufacturer = relationship('Manufacturer', lazy='joined')
    purchases = relationship('Purchase', back_populates='car')

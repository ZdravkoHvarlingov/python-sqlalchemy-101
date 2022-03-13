from db.core import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, ForeignKey, BigInteger, DateTime


class Purchase(Base):
    __tablename__ = 'purchase'

    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey('car.id', ondelete='CASCADE'), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id', ondelete='CASCADE'), nullable=False)
    final_price_in_coins = Column(BigInteger, nullable=False)
    purchase_date = Column(DateTime, nullable=False)

    car = relationship('Car', back_populates='purchases', lazy='joined')
    customer = relationship('Customer', back_populates='purchases', lazy='joined')

    def __repr__(self) -> str:
        return (f'Purchase(car={self.car.manufacturer.name} - {self.car.model}, '
                f'customer={self.customer.name} {self.customer.family_name}, '
                f'price={self.final_price_in_coins}, datetime={self.purchase_date})')

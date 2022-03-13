from typing import List
from sqlalchemy import func
from sqlalchemy.sql.functions import coalesce

from db.connection import DbSession

from model.car import Car
from model.purchase import Purchase
from model.customer import Customer


class PurchaseRepository:
    
    @staticmethod
    def find_all():
        with DbSession.create() as session:
            return session.query(Purchase) \
                          .order_by(Purchase.purchase_date.desc()) \
                          .all()

    @staticmethod
    def find_by_customer_age_below_and_car_price_above(customer_age: int, car_price: int) -> List[Purchase]:
        with DbSession.create() as session:
            return session.query(Purchase) \
                          .join(Customer, Purchase.customer_id == Customer.id) \
                          .join(Car, Purchase.car_id == Car.id) \
                          .filter(Car.base_price_in_coins > car_price, Customer.age < customer_age) \
                          .all()

    @staticmethod
    def get_number_of_purchases_and_total_amount_per_customer():
        with DbSession.create() as session:
            return session.query(Customer.name,
                                 Customer.family_name,
                                 func.count(Purchase.id).label('purchases'),
                                 func.sum(coalesce(Purchase.final_price_in_coins, 0)).label('total')) \
                          .outerjoin(Purchase, Customer.id == Purchase.customer_id) \
                          .group_by(Customer.id, Customer.name, Customer.family_name) \
                          .all()

    @staticmethod
    def upsert(purchase: Purchase):
        with DbSession.create() as session:
            session.add(purchase)
            session.flush()
            session.commit()

            return purchase

    @staticmethod
    def delete(purchase: Purchase):
        if not purchase or not purchase.id:
            return
        
        PurchaseRepository.delete_by_id(purchase.id)

    @staticmethod
    def delete_by_id(purchase_id: int):
        with DbSession.create() as session:
            session.query(Purchase).filter(Purchase.id == purchase_id).delete()
            session.commit()

from sqlalchemy import func

from db.connection import DbSession
from model.customer import Customer
from model.purchase import Purchase


class CustomerRepository:
    
    @staticmethod
    def find_all():
        with DbSession.create() as session:
            return session.query(Customer).all()
    
    @staticmethod
    def find_by_name_and_family_name(name: str, family_name: str) -> Customer:
        with DbSession.create() as session:
            return session.query(Customer).filter(Customer.name == name, Customer.family_name == family_name).first()
    
    @staticmethod
    def upsert(customer: Customer):
        with DbSession.create() as session:
            session.add(customer)
            session.flush()
            session.commit()

            return customer

    @staticmethod
    def delete(customer: Customer):
        if not customer or not customer.id:
            return
        
        CustomerRepository.delete_by_id(customer.id)

    @staticmethod
    def delete_by_id(customer_id: int):
        with DbSession.create() as session:
            session.query(Customer).filter(Customer.id == customer_id).delete()
            session.commit()
    
    @staticmethod
    def delete_customers_without_purchases():
        with DbSession.create() as session:
            customers_with_no_orders = session.query(Customer.id) \
                                              .outerjoin(Purchase, Customer.id == Purchase.customer_id) \
                                              .group_by(Customer.id) \
                                              .having(func.count(Purchase.id) == 0) \
                                              .all()

            customers_to_delete = [customer.id for customer in customers_with_no_orders]
            session.query(Customer).filter(Customer.id.in_(customers_to_delete)).delete()
            session.commit()

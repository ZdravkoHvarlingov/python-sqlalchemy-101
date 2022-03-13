from db.connection import DbSession
from model.car import Car
from model.manufacturer import Manufacturer


class CarRepository:
    
    @staticmethod
    def find_all():
        with DbSession.create() as session:
            return session.query(Car).all()
    
    @staticmethod
    def find_by_manufacturer_name_and_model(manufacturer_name: str, model: str) -> Car:
        with DbSession.create() as session:
            return session.query(Car) \
                          .join(Manufacturer, Car.manufacturer_id == Manufacturer.id) \
                          .filter(Car.model == model, Manufacturer.name == manufacturer_name) \
                          .first()

    @staticmethod
    def update_car_prices_if_price_below(price_threshold, increase_percent):
        with DbSession.create() as session:
            session.query(Car) \
                   .filter(Car.base_price_in_coins < price_threshold) \
                   .update({Car.base_price_in_coins: Car.base_price_in_coins * (1 + increase_percent)})
            session.commit()


    @staticmethod
    def upsert(car: Car):
        with DbSession.create() as session:
            session.add(car)
            session.flush()
            session.commit()

            return car

    @staticmethod
    def delete(car: Car):
        if not car or not car.id:
            return
        
        CarRepository.delete_by_id(car.id)

    @staticmethod
    def delete_by_id(car_id: int):
        with DbSession.create() as session:
            session.query(Car).filter(Car.id == car_id).delete()
            session.commit()

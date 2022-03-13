import datetime

from model.car import Car
from model.customer import Customer
from model.manufacturer import Manufacturer
from model.purchase import Purchase

from repositories.car_repository import CarRepository
from repositories.customer_repository import CustomerRepository
from repositories.manufacturer_repository import ManufacturerRepository
from repositories.purchase_repository import PurchaseRepository


def insert_manufacturers():
    kia = Manufacturer('KIA', 1950)
    ManufacturerRepository.upsert(kia)

    audi = Manufacturer('Audi', 1900)
    ManufacturerRepository.upsert(audi)

    vw = Manufacturer('VW', 1850)
    ManufacturerRepository.upsert(vw)


def insert_cars():
    kia = ManufacturerRepository.find_by_name('KIA')
    sportage = Car()
    sportage.base_price_in_coins = 6_500_000
    sportage.model = 'Sportage 2022'
    sportage.manufacturer = kia
    sportage.release_date = datetime.date(2021, 12, 1)
    CarRepository.upsert(sportage)

    audi = ManufacturerRepository.find_by_name('Audi')
    a4 = Car()
    a4.base_price_in_coins = 10_000_000
    a4.model = 'A4 2022'
    a4.manufacturer = audi
    a4.release_date = datetime.date(2021, 6, 3)
    CarRepository.upsert(a4)


def insert_customers():
    zdravko = Customer('Zdravko', 'Hvarlingov', 24)
    CustomerRepository.upsert(zdravko)

    iveta = Customer('Iveta', 'Hvarlingova', 24)
    CustomerRepository.upsert(iveta)

    ivan = Customer('Ivan', 'Georgiev', 31)
    CustomerRepository.upsert(ivan)


def insert_purchases():
    # Set only foreign keys
    zdravko = CustomerRepository.find_by_name_and_family_name('Zdravko', 'Hvarlingov')
    sportage = CarRepository.find_by_manufacturer_name_and_model('KIA', 'Sportage 2022')

    purchase = Purchase()
    purchase.customer_id = zdravko.id
    purchase.car_id = sportage.id
    purchase.final_price_in_coins = sportage.base_price_in_coins - 30_000
    purchase.purchase_date = datetime.datetime.now()
    PurchaseRepository.upsert(purchase)

    # Use objects directly
    iveta = CustomerRepository.find_by_name_and_family_name('Iveta', 'Hvarlingova')
    audi_a4 = CarRepository.find_by_manufacturer_name_and_model('Audi', 'A4 2022')

    purchase2 = Purchase()
    purchase2.customer = iveta
    purchase2.car = audi_a4
    purchase2.final_price_in_coins = audi_a4.base_price_in_coins - 100_000
    purchase2.purchase_date = datetime.datetime.now()
    PurchaseRepository.upsert(purchase2)


if __name__ == '__main__':
    insert_purchases()

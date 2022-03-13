from repositories.manufacturer_repository import ManufacturerRepository
from repositories.purchase_repository import PurchaseRepository


def get_all_manufacturers():
    manufacturers = ManufacturerRepository.find_all()
    print(manufacturers)


def get_kia_manufacturer():
    kia = ManufacturerRepository.find_by_name('KIA')
    print(kia)


def get_all_purchases():
    purchases = PurchaseRepository.find_all()
    for purchase in purchases:
        print(purchase)


def get_expensive_purchases_for_young_customers():
    purchases = PurchaseRepository.find_by_customer_age_below_and_car_price_above(25, 9_000_000)
    for purchase in purchases:
        print(purchase)


def get_purchases_per_customer():
    purchases_per_customer = PurchaseRepository.get_number_of_purchases_and_total_amount_per_customer()
    for purchase in purchases_per_customer:
        print(purchase)


if __name__ == '__main__':
    get_purchases_per_customer()

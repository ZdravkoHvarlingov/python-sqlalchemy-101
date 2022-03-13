from repositories.purchase_repository import PurchaseRepository
from repositories.customer_repository import CustomerRepository


def delete_purchases():
    purchases = PurchaseRepository.find_by_customer_age_below_and_car_price_above(25, 7_500_000)
    for purchase in purchases:
        PurchaseRepository.delete(purchase)


def delete_customers_without_purchases():
    CustomerRepository.delete_customers_without_purchases()


if __name__ == '__main__':
    delete_customers_without_purchases()

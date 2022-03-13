from repositories.car_repository import CarRepository


def increase_car_prices():
    CarRepository.update_car_prices_if_price_below(7_000_000, 0.2)


def change_kia_price():
    kia = CarRepository.find_by_manufacturer_name_and_model('KIA', 'Sportage 2022')
    kia.base_price_in_coins = 6_000_000
    CarRepository.upsert(kia)


if __name__ == '__main__':
    change_kia_price()

import sys
from pathlib import Path
import pytest

sys.path.insert(1, str(Path(__file__).parents[1]))
from delivery import Delivery
from courier import Courier
from validate import find_courier
from datetime import datetime


@pytest.fixture
def deliveries(scope='session'):
    delivery1 = Delivery(delivery_id=1, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=3.45, city='london', distance=2_500)
    delivery2 = Delivery(delivery_id=2, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=2.5, city='london', distance=1_500)
    delivery3 = Delivery(delivery_id=3, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=1.25, city='london', distance=6_500)
    delivery4 = Delivery(delivery_id=4, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=5.00, city='london', distance=2_000)
    delivery5 = Delivery(delivery_id=5, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=7.12, city='london', distance=2_200)
    return [delivery1, delivery2, delivery3, delivery4, delivery5]


@pytest.fixture
def courier_list_1(scope='session'):
    return [
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='car', courier_id=1),
        Courier(first_name='Danny', surname='DeVito', city='paris', country='FR', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='unicycle', courier_id=2),
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='walk', courier_id=3),
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='bike', courier_id=4),
        Courier(first_name='Danny', surname='DeVito', city='birmingham', country='UK', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='unicycle', courier_id=5),
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='unicycle', courier_id=6),
    ]

@pytest.fixture
def courier_list_2(scope='session'):
    return [
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='car', courier_id=7),
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='bike', courier_id=8),
        Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='car', courier_id=9),
    ]


class TestFindCourier:
    @staticmethod
    def test_filters_to_correct_country(courier_list_1):
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2022/01/01', '%Y/%m/%d'), price=3.45, city='paris', distance=2.5)

        delivery = find_courier(delivery=delivery, couriers=courier_list_1)
        assert delivery.in_progress
        assert delivery.courier_id == 2

    @staticmethod
    def test_is_green_filter(courier_list_2):
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=3.45, city='london', distance=2.5)

        delivery = find_courier(delivery=delivery, couriers=courier_list_2)
        assert delivery.in_progress
        assert delivery.courier_id == 8

    @staticmethod
    def test_speed_filter():
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=3.45, city='london', distance=2.5)

        green_couriers = [
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='moped', courier_id=1),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='car', courier_id=2),
            ]

        delivery = find_courier(delivery=delivery, couriers=green_couriers)
        assert delivery.in_progress
        assert delivery.courier_id == 2

    @staticmethod
    def test_speed_filter_green():
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=3.45, city='london', distance=2.5)

        green_couriers = [
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='walk', courier_id=7),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='bike', courier_id=8),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='unicycle', courier_id=9)
            ]

        delivery = find_courier(delivery=delivery, couriers=green_couriers)
        assert delivery.in_progress
        assert delivery.courier_id == 8

    @staticmethod
    def test_car_only():
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2023/01/01', '%Y/%m/%d'), price=3.45, city='birmingham', distance=2.5)

        couriers = [
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='walk', courier_id=7),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='bike', courier_id=8),
            Courier(first_name='Danny', surname='DeVito', city='birmingham', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='car', courier_id=9)
            ]

        delivery = find_courier(delivery=delivery, couriers=couriers)
        assert delivery.in_progress
        assert delivery.courier_id == 9

    @staticmethod
    def test_dates():
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2022/01/01', '%Y/%m/%d'), price=3.45, city='london', distance=2.5)

        couriers = [
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='walk', courier_id=7),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='bike', courier_id=8),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2022/01/01', '%Y/%m/%d'), vehicle='car', courier_id=9)
            ]

        delivery = find_courier(delivery=delivery, couriers=couriers)
        assert delivery.in_progress
        assert delivery.courier_id == 9

    @staticmethod
    def test_no_courier_found():
        delivery = Delivery(delivery_id=1, delivery_date=datetime.strptime('2022/01/01', '%Y/%m/%d'), price=3.45, city='london', distance=2.5)

        couriers = [
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='walk', courier_id=7),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='bike', courier_id=8),
            Courier(first_name='Danny', surname='DeVito', city='london', country='UK', valid_from=datetime.strptime('2023/01/01', '%Y/%m/%d'), vehicle='car', courier_id=9)
            ]

        with pytest.raises(Exception):
            delivery = find_courier(delivery=delivery, couriers=couriers)
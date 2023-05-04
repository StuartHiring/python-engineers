import pandas
from datetime import datetime
from typing import Optional


class Delivery:

    def __init__(self,
        delivery_id : int,
        delivery_date: datetime,
        city: str,
        distance: int,
        price: float,
        in_progress: bool = False,
        courier_id: Optional[int] = None):

        self.delivery_id = delivery_id
        self.delivery_date = delivery_date
        self.city = city
        self.distance = distance
        self._price = price
        self.in_progress = in_progress
        self.courier_id = courier_id

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0.0:
            raise BaseException
        self._price = value


    def add_vat(self, vat):
        vat = 1.2
        price_plus_vat = self.price * vat
        return price_plus_vat



class DeliveryFunctions:
    @staticmethod
    def sum_green_deliveries(deliveries):
        london_deliveries = []
        ###Consider london deliveries only
        for delivery in deliveries:
            if delivery.city != 'london':
                continue
            london_deliveries.append(delivery)
        total_price = 0.0
        for green_delivery in london_deliveries:
            total_price += green_delivery.price
        return total_price

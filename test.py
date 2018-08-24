from abc import ABCMeta, abstractmethod

class Car():
    def __init__(self, age, price_per_day, make, model, year, premium, car_type):
        self._age = age
        self._price_per_day = price_per_day
        self._make = make
        self._model = model
        self._year = year
        self._premium = premium
        self._car_type = car_type
        
        @abstractmethod
        def calculate_fee(self):
            pass
        
class Customer():
    def __init__(self, name, age, licence_number, email_address, rental_period, pickup_location, drop_off_location):
        self._name = name
        self._age = age
        self._licence_number = licence_number
        self._email_address = email_address
        self._rental_period = rental_period
        self._pickup_location = pickup_location
        self._drop_off_location = drop_off_location

class Rental(Car, Customer):
    def calculate_fee(self, Car, Customer):
        if rental_period > 7:
            if car_type is small:
                print("Hello")




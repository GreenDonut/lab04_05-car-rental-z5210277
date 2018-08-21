from abc import ABC, abstractmethod

class Car(ABC):
	def __init__(self):
		self._age = age
		self._price_per_day = pricePerDay
		self._make = make
		self._model = model
		self._year = year
		self._size = ''
		self._premium = premium

	@abstractmethod
	def get_price(self):
		pass

	@abstractmethod
	def apply_discount(self):
		pass

	def __str__(self):
		return str(self.id)


class SmallCar(Car):
	def get_price_multiplier(self):
		if car.premium:
			return 1.15
		else:
			return 1
	def apply_discount(self):
		if car.premium and rental_period > 7:
			return 0.95				
class MediumCar(Car):
	def get_price_multiplier(self):
		if car.premium:
			return 1.15
		else:
			return 1
	def apply_discount(self):
		if car.premium and rental_period > 7:
			return 0.95				

class LargeCar(Car):
	def get_price_multiplier(self):
		if car.premium:
			return 1.15
		else:
			return 1
	def apply_discount(self):
		if rental_period > 7:
			return 0.95		
					
class Customer():
	def __init__(self):
		self._name = name
		self._age = age
		self._licence_number = licence_number
		self._email = email 
		self._credit_card = credit_card

	def book_car(name, age, licence_number, email):
		pass

	

class Rental():
	def __init__(self):
		self._rental_period = rental_p
		self._insurance = insurance
		self._net_price = netPrice
		self._location = location

	def compute_rental_fee(self, car):
		rental_fee = car.get_price_multiplier() * self.rental_period * apply_discount()
		return rental_fee
class Staff():
	def __init__(self):
		self._username = username
		self._password = password


class Manager():
	def __init__(self):
		self._username = username
		self._password = password

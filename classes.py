# instantiate - create an instance of a class
# instance = object
# encapsulation - bundle data + methods that use that data together
# setter method - method used to control changes to a variable 
# getter  ''    -  ''     ''  returns value of variable
# def - start of functions lmao
# __init__ - constructor. is called when a new instance is created
# self. - refers to newly created object
# arguments passed for __init__ so constructor knows where to store
# what info (order should match below)

from abc import ABC, abstractmethod
from tests import tests

class Car(ABC):
	def __init__(self, age, price_per_day,make,model,year,premium):
		self._age = age
		self._price_per_day = pricePerDay
		self._make = make
		self._model = model
		self._year = year
		self._premium = premium

	@abstractmethod
	def get_price(self):
		pass

	@abstractmethod
	def apply_discount(self):
		pass

	def __str__(self, rental):
		return 'customer name: {}, car booked: {}, rental period: {}, total fee: ${:.2f}'.format(
            self._name, self._description, rental._rental_period, rental.rental_fee)




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


class Rental():
	def __init__(self, rental_period, insurance, net_price, location):
		self._rental_period = rental_p
		self._insurance = insurance
		self._net_price = netPrice
		self._location = location

	def compute_rental_fee(self, car):
		rental_fee = car.get_price_multiplier() * self.rental_period * apply_discount()
		return rental_fee

class Customer():
	def __init__(self,name,age,licence_number,email,credit_card):
		self._name = name
		self._age = age
		self._licence_number = licence_number
		self._email = email 
		self._credit_card = credit_card

	def book_car(self, customer):
		#take details
		#compute rental fee
		#get booking confirmation
		pass
	

class Staff():
	def __init__(self,username,password):
		self._username = username
		self._password = password


class Manager():
	def __init__(self,username,password):
		self._username = username
		self._password = password


test1 = SmallCar(13, 59.95,'Mazda','MX5',1998,False)
test2 = LargeCar(7,100.00,'Toyota','Land Rover',2003,False)
test3 = MediumCar(10,75.00,'Subaru', 'Liberty',2005,True)
test4 = MediumCar(25,64.99,'Toyota','Trueno AE86', 1983, False)

tai_lopez = Customer('Tai Lopez', 41, 6771920,'hereinmygarage@yahoo.com','Calabasas')
tai_lopez.book_car()
#def __init__(self, age, price_per_day,make,model,year,premium):

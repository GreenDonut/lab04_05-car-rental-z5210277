from abc import ABC, abstractmethod

class Car(ABC):
	def __init__(self, age, price_per_day,make,model,year,premium):
		self._age = age
		self._price_per_day = price_per_day
		self._make = make
		self._model = model
		self._year = year
		self._premium = premium

	@abstractmethod
	def get_price_multiplier(self):
		pass

	@abstractmethod
	def apply_discount(self):
		pass

	def __str__(self):
		return 'Make: {}, Model: {}, Year: {}, Age: {}, Price/Day: {}, Premium {}'.format(
            self._make, self._model, self._year, self._age, self._price_per_day,self._premium)

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
		self._rental_period = rental_period
		self._insurance = insurance
		self._net_price = net_price
		self._location = location

	def compute_rental_fee(self, car):
		self.net_price = car.get_price_multiplier(car) * self.rental_period * apply_discount(car)
		return net_price

class Customer():
	def __init__(self,name,age,licence_number,email,credit_card):
		self._name = name
		self._age = age
		self._licence_number = licence_number
		self._email = email 
		self._credit_card = credit_card

	def book_car(self, car, rental,rental_period, insurance, net_price, location):
		#calculate rental fee
		net_price = rental.compute_rental_fee(car)
		new_rental = rental(rental_period,insurance,net_price,location)

		#booking confirmation
		print('BOOKING CONFIRMATION') 
		print('Customer Name: ' + customer.name)
		print(str(car))
		print('Booking Period: ' + str(rental.rental_period) + ' Days')
		print('Total Rental Fee: $' + str(net_price))
		return new_rental


class Staff():
	def __init__(self,username,password):
		self._username = username
		self._password = password


class Manager():
	def __init__(self,username,password):
		self._username = username
		self._password = password

#tests 

test1 = SmallCar(13, 59.95,'Mazda','MX5',1998,False)
test2 = LargeCar(7,100.00,'Toyota','Land Rover',2003,False)
test3 = MediumCar(10,75.00,'Subaru', 'Liberty',2005,True)
test4 = MediumCar(25,64.99,'Toyota','Trueno AE86', 1983, False)

customer = Customer('Tai Lopez', 41, 6771920,'hereinmygarage@yahoo.com',54701928493815732)
customer.book_car(test1, rental, 14, True, net_price, 'Sydney')

#book car method should take in : customerdetails, then compute net price, then print
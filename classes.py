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
# override - ability of a class to change implementation of a method
# provided by one of its ancestors 
# import - access code from another module 
# module - document w/ python code?
# abstract class - contain one or more abstract methods
# abstract method - declared but contains no implementation
# encapsulation - keep attributees of a class private and only accessible or
# modifiable with public methods (keep attributes private, only accessible 
# through methods) - for maintaining state 

from abc import ABC, abstractmethod

# ABC = can't create instance of this class 
# Car is encapsulated - can't change attributes 
class Car(ABC):
    def __init__(self, age, price_per_day, make, model, year):
        self._age = age
        self._price_per_day = price_per_day
        self._make = make
        self._model = model
        self._year = year

    # all subclasses have this method, from ABC
    # @ - features of a function
    @abstractmethod
    def get_price(self):
        pass           

class Customer():
    def __init__(self, name, age, licence_number, email, credit_card):
        self._name = name
        self._age = age
        self._licence_number = licence_number
        self._email = email 
        self._credit_card = credit_card

class Rental():
    def __init__(self, rental_period, insurance, pickup_location,
                 drop_off_location):
        self._rental_period = rental_period
        self._insurance = insurance
        self._pickup_location = pickup_location
        self._drop_off_location = drop_off_location
        # LHS class attributes
        # RHS initial values (passed through constructor)
    
    def book_car(self, car, customer, rental_period, insurance, net_price,
                 pickup_location, drop_off_location):
        self._car = car
        self._customer = customer
        self._rental_period = rental_period
        self._insurance = insurance
        self._net_price = car.get_price(self._rental_period)
        self._pickup_location = pickup_location
        self._drop_off_location = drop_off_location

class SmallCar(Car):
    def get_price(self, rental):
        return rental * self._price_per_day
            
class MediumCar(Car):
    def get_price(self, rental):
        return rental * self._price_per_day

class LargeCar(Car):
    def get_price(self, rental):
        if rental < 7:
            return (rental * self._price_per_day) * 1.15
        else:
            return ((rental * self._price_per_day) * 1.15) * 0.95

class PremiumCar(Car):
    def get_price(self, rental):
        if rental < 7:
            return (rental * self._price_per_day) * 1.15
        else:
            return ((rental * self._price_per_day) * 1.15) * 0.95

class Staff():
    def __init__(self,username,password):
        self._username = username
        self._password = password


class Manager():
    def __init__(self,username,password):
        self._username = username
        self._password = password


# TESTS !!!

# CAR DETAILS - test for every type of car
car1 = SmallCar(7, 100, 'Toyota', 'Yaris', 2003)
car2 = MediumCar(2, 3, 'Toyota', 'Camry', 2008)
car3 = LargeCar(10, 56, 'Jeep', 'Cherokee', 2010)
car4 = PremiumCar(1, 7, 'Range Rover', '???', 2005)

''' 
print('CAR DETAILS')
print('Age: {}'.format(car1._age))
print('Price per day: {}'.format(car1._price_per_day))
print('Make: {}'.format(car1._make))
print('Model: {}'.format(car1._model))
print('Year: {}'.format(car1._year))
'''

# RENTAL DETAILS - test for every type of car too
customer1 = Customer('Tai Lopez', 41, 6771920, 'hereinmygarage@yahoo.com', 
                     'Calabasas')
rental1 = Rental(50, 'Yes', 'Central', 'Town Hall')
test1 = rental1.book_car(car1, customer1._name, rental1._rental_period, 1, 1,
                         rental1._pickup_location, rental1._drop_off_location)

print('{}'.format(test1._customer))


'''
print('RENTAL DETAILS')
print('Car: {}'.format(test1._car))
print('Customer: {}'.format(test1._customer))
print('Rental period: {}'.format(test1._rental_period))
print('Insurance: {}'.format(test1._insurance))
print('Net price: {}'.format(test1._net_price))
'''

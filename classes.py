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
    
    def book_car(self, customer, car, rental_period, insurance, net_price,
                 pickup_location, drop_off_location):
        print('BOOKING CONFIRMATION')
        print('Customer Name: ' + customer2._name)
        print('Car: ' + car3._make + ' ' + car3._model)
        print('Rental period: ' + str(rental2._rental_period) + ' days')
        print('Insurance: ' + str(rental2._insurance))
        print('Net price: ' + str(car2.get_price(self._rental_period)))
        print('Pickup location: ' + str(rental2._pickup_location))
        print('Dropoff location: ' + str(rental2._drop_off_location))

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

# CAR DETAILS - test for every type of car. Details called from SmallCar,
# MediumCar, LargeCar and PremiumCar since parent Car class instantiable.
# Tests located here for efficiency (they would have to be in all classes
# listed above if they weren't here)
car1 = SmallCar(7, 100, 'Toyota', 'Yaris', 2003)
car2 = MediumCar(2, 3, 'Toyota', 'Camry', 2008)
car3 = LargeCar(10, 56, 'Jeep', 'Cherokee', 2010)
car4 = PremiumCar(1, 7, 'Range Rover', 'Big Car', 2005)

# Replace car1 with 2, 3, 4 to test
'''
print('CAR DETAILS')
print('Age: {}'.format(car1._age))
print('Price per day: {}'.format(car1._price_per_day))
print('Make: {}'.format(car1._make))
print('Model: {}'.format(car1._model))
print('Year: {}'.format(car1._year))
'''

# CUSTOMER DETAILS - testing if customer details go through 
customer1 = Customer('Tai Lopez', 41, 6771920,'hereinmygarage@yahoo.com',
                     54701928493815732)
customer2 = Customer('Katrina Davis', 89, 5728508, 'wowemail@hotmail.com',
                           47195284620917492)
customer3 = Customer('Myfirstname Andlastname', 17, 4820682,
                     'coolies@wow.com', 38105729572840275)

'''                 
print('CUSTOMER DETAILS')
print('Name: ' + customer1._name)
print('Age: ' + str(customer1._age))
print('Licence number: ' + str(customer1._licence_number))
print('Email: ' + customer1._email)
print('Credit card: ' + str(customer1._credit_card))
'''

# RENTAL DETAILS - have to change values in book_car for details to print
# out properly
#rental1 = Rental(14, False, 'Sydney', 'Town Hall')
#rental1.book_car(customer1, car1, rental1, rental1, car1, rental1, rental1)
#rental2 = Rental(3, True, 'Bondi', 'Manly')
#rental2.book_car(customer2, car3, rental2, rental2, car3, rental2, rental2)
#rental3 = Rental(93, False, 'Sydney', Los Angeles')
#rental3.book_car(cistomer3, car4, rental3, rental3, car4, rental3, rental3)

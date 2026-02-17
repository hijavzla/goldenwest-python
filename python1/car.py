# This file contains the class Car with private attributes and methods 
class Car:
    # The __init__ method initializes the data attributes __year_model, __make, and __speed
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    # The ccelerate function increases speed by 5mph
    def accelerate(self): 
        self.__speed += 5
    
    # The brake method substracts speed by 5mph
    def brake(self): 
        if self.__speed <= 5:
            self.__speed = 0
        else: 
            self.__speed -= 5
    
    # The get_speed method returns the current speed
    def get_speed(self): 
        return self.__speed
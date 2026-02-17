# Laura Rodriguez-Adjunta, CS131
# Project 5a: Shiftsupervisor class
# This file contains the Employee class and Shiftsupervisor subclass 

# The Employee class holds general data about an employee
class Employee:

    # The __init__ method initializes the data attributes __name and __number
    def __init__(self, name, number): 
        self.__name = name
        self.__number = number 

    # Getter functions 
    def get_name(self): 
        return self.__name

    def get_number(self):
        return self.__number

    # Setter functions
    def set_name(self, name): 
        self.__name = name
    
    def set_number(self, number): 
        self.__number = number

# The Shiftsupervisor is a sublcass of the Employee class, with a couple of subclass only attributes 
class Shiftsupervisor(Employee): 
    
    def __init__(self, name, number, bonus, salary): 
        # Call the superclass's __init__ method and pass the required arguments 
        Employee.__init__(self, name, number)

        # Initialize the sub class only attributes
        self.__bonus = bonus
        self.__salary = salary 

    # Getter functions
    def get_bonus(self): 
        return self.__bonus

    def get_salary(self): 
        return self.__salary
    
    # Setter functions
    def set_bonus(self, bonus): 
        self.__bonus = bonus
    
    def set_salary(self, salary): 
        self.__salary = salary 

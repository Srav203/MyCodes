from abc import ABC, abstractmethod

# Abstract base class
class Vehicle(ABC):  # base class / super class

    @abstractmethod
    def no_of_wheels(self):
        pass

# Subclass for Bicycle
class Bicycle(Vehicle):  # subclass

    # Overriding abstract method
    def no_of_wheels(self):
        print("Bicycle: I have 2 wheels")

# Subclass for Car
class Car(Vehicle):  # subclass

    # Overriding abstract method
    def no_of_wheels(self):
        print("Car: I have 4 wheels")

# Subclass for Truck
class Truck(Vehicle):  # subclass

    # Overriding abstract method
    def no_of_wheels(self):
        print("Truck: I have 6 wheels")

# Subclass for Motorcycle
class Motorcycle(Vehicle):  # subclass

    # Overriding abstract method
    def no_of_wheels(self):
        print("Motorcycle: I have 2 wheels")

# Driver code
# Creating the objects to call the abstract method.
bike = Bicycle()
bike.no_of_wheels()

auto = Car()
auto.no_of_wheels()

lorry = Truck()
lorry.no_of_wheels()

moto = Motorcycle()
moto.no_of_wheels()

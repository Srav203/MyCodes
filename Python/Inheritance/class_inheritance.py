class Vehicle:
    def start_engine(self):
        print("Engine started")

    def drive(self):
        print("Driving the vehicle")

class Car(Vehicle):
    def play_music(self):
        print("Playing music")

    def drive(self):
        print("Driving the car")

class ElectricCar(Car):
    def charge_battery(self):
        print("Charging the battery")

    def drive(self):
        print("Driving the electric car silently")

# Driver code
vehicle = Vehicle()
vehicle.start_engine()
vehicle.drive()

car = Car()
car.start_engine()
car.play_music()
car.drive()

electric_car = ElectricCar()
electric_car.start_engine()
electric_car.charge_battery()
electric_car.drive()

from car import Car

class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


my_Car = ElectricCar('audi', 'a4', 2020)
print(my_Car.get_descriptive_name())
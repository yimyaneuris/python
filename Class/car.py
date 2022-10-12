class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        return (f"{self.year} {self.make} {self.model}")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


    def fill_gas_tank(self):
        print("This car need a gas tank!")
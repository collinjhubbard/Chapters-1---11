class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        full_name = f"{self.year} {self.make} {self.model}"
        return full_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles")

    def update_odometer(self, mileage):
        """Set the odometer reading to a given value"""
        #self.odometer_reading = mileage
        """Set the odometer. Reject attempts top tole back"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't rollback the odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles

my_used_car = Car('toyota', 'prius', 2023)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()




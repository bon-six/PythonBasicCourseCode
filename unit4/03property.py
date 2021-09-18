



class Car:

    # class variable, common for all instances
    category = '4 wheels small vehicle'
    # all car must be less then 10.0l fuel per 100km
    fuel_efficiency_threshold = 10.0  

    # class method
    @classmethod
    def how_far_can_go(cls,fuel,fuel_per_100km):
        if fuel_per_100km > cls.fuel_efficiency_threshold:
            return -1
        return fuel/fuel_per_100km * 100



    # constructor method
    def __init__(self,seats,fuel,status = 'parked'):
        self.seats = seats
        self._fuel = fuel
        self.status = status
        print(f'a new car with {seats} seats, {fuel:.2f}l fuel loaded, now it is {status}.')

    @property
    def fuel(self):
        print('Reading current fuel number')
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        print('Changing current fuel number')
        self._fuel = fuel

    @fuel.deleter
    def fuel(self):
        print('fuel variable no more valid')
        del self._fuel

    # instance method
    def start(self):
        print('engine started! runninng!')
        self.status = 'moving'
        print(f'this car have {self.seats} seats')

    def brake(self):
        pass

    def stop(self):
        print('car stopped.')
        self.status = 'parked'
        print(f'this car have {self.seats} seats')

    def turn_left(self):
        pass

    def turn_right(self):
        pass

my_car1 = Car(4,28.5)

print(my_car1.fuel)
my_car1.fuel += 1
print(my_car1.fuel)
del my_car1.fuel
print(my_car1.fuel)  # this line will cause error



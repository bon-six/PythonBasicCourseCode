



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
        self.fuel = fuel
        self.status = status
        print(f'a new car with {seats} seats, {fuel:.2f}l fuel loaded, now it is {status}.')

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


my_car2 = Car(5, 48.8,'moving')


print(my_car1.category)
print(my_car2.category)

print(f'my_car1 is {my_car1.seats} seats car.')
print(f'my_car2 is {my_car2.seats} seats car.')

print()
print(Car.category)
print('calculat how far can go',Car.how_far_can_go(26,5.6))
print('calculat how far can go',Car.how_far_can_go(26,15.6))
Car.fuel_efficiency_threshold = 16.0
print('calculat how far can go',Car.how_far_can_go(26,15.6))

print('instance call to class method',my_car1.how_far_can_go(40,8.8))

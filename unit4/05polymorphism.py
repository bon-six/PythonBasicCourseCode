
class Vehicle:
    def __init__ (self,fuel_capacity=0,status='parked'):
        self.fuel_capacity = fuel_capacity
        self.status = status
        print(f'a new vehicle with {fuel_capacity:.2f}l fuel tank, now it is {status:s}.')

    # instance method
    def start(self):
        print('engine started! vehicle runninng!')
        self.status = 'moving'
        print(f'this vehicle have {self.fuel_capacity:.2f}l fuel tank')

    def brake(self):
        print('vehicle speed reduced')
        pass

    def stop(self):
        print('vehicle stopped.')
        self.status = 'parked'
        print(f'this vehicle have {self.fuel_capacity:.2f}l fuel tank')

class Car(Vehicle):
    # class variable, common for all instances
    category = '4 wheels small vehicle'
    # all care must be less then 10.0l fuel per 100km
    fuel_efficiency_threshold = 10.0  

    # class method
    @classmethod
    def how_far_can_go(cls,fuel,fuel_per_100km):
        if fuel_per_100km > cls.fuel_efficiency_threshold:
            return -1
        return fuel/fuel_per_100km * 100

    # constructor method
    def __init__(self,seats,fuel,status = 'parked'):
        super().__init__(30,status)
        self.seats = seats
        self.fuel = fuel
        self.status = status
        print(f'a new car with {seats:d} seats, {fuel:.2f}l fuel loaded, now it is {status:s}.')

    # instance method
    def start(self):
        print('engine started! Car runninng!')
        self.status = 'moving'
        print(f'this car have {self.seats:d} seats')

    def stop(self):
        print('car stopped.')
        self.status = 'parked'
        print(f'this car have {self.seats:d} seats')

class Truck(Vehicle):
    # class variable, common for all instances
    category = 'cargo loading vehicle'

    # class method. there is no class method now.

    # constructor method
    def __init__(self,seats,load_capacity=0,status = 'parked'):
        super().__init__(60,status)
        self.seats = seats
        self.load_capacity = load_capacity
        self.status = status
        print(f'a new truck with {seats:d} seats, {load_capacity:.2f}ton capacity, now it is {status:s}.')

    # instance method
    def start(self):
        print('engine started! Truck runninng!')
        self.status = 'moving'
        print(f'this truck have {self.load_capacity:.2f}ton capacity')

    def stop(self):
        print('Truck stopped')
        self.status = 'parked'
        print(f'this truck have {self.load_capacity:.2f}ton capacity')

    def check_can_load(self,load):
        if self.load_capacity > 0:
            if load <= self.load_capacity:
                return True
            else:
                return False
        else:
            print('load capacity not defined')
            return False

def run_test1():
    my_car = Car(4,20)
    print(my_car)
    print(type(my_car))
    print(my_car.fuel_capacity)
    my_car.brake()  # sub class not defined method, will use the base class version
    print('-'*10)

def run_test2():
    my_truck = Truck(2,1.2)
    print(my_truck)
    print(type(my_truck))
    print(my_truck.fuel_capacity)
    can_load = my_truck.check_can_load(2.5)
    print(f'check loading is {can_load}')

def run_test3():
    my_car = Car(4,20)
    my_truck = Truck(2,1.2)
    for my_vehicle in [my_car, my_truck]:
        # brake() will go to base class version
        # start() and stop() will go to sub-class version
        my_vehicle.start()
        my_vehicle.brake()
        my_vehicle.stop()
        print('-'*60)
    del Truck.start
    for my_vehicle in [my_car, my_truck]:
        # because now Truck class don't have the start()
        # so the truck.start() will call to base class version.
        my_vehicle.start()
        my_vehicle.brake()
        my_vehicle.stop()
        print('-'*60)

if __name__ == '__main__':
    run_test1()
    print('+'*60)
    run_test2()
    print('+'*60)
    run_test3()

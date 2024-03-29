
class Car:
    # constructor method
    def __init__(self,seats,fuel,status = 'parked'):
        self.seats = seats
        self.fuel = fuel
        self.status = status
        print(f'a new car with {seats} seats, {fuel:.2f}l fuel, now it is {status}.')

    # instance method
    def start(self):
        print('engine started! runninng!')
        self.status = 'moving'
        print(f'this car have {self.seats:d} seats')

    def brake(self):
        pass

    def stop(self):
        print('car stopped.')
        self.status = 'parked'
        print(f'this car have {self.seats:d} seats')

    def turn_left(self):
        pass

    def turn_right(self):
        pass

def run_test1():
    my_car1 = Car(4,28.5)
    print(my_car1)
    print(type(my_car1))

    my_car2 = Car(5, 48.8,'moving')
    print(my_car2)
    print(type(my_car2))

    my_car1.start()
    my_car2.start()
    my_car2.stop()
    my_car1.stop()

    print(f'my_car1 is {my_car1.seats} seats car.')
    print(f'my_car2 is {my_car2.seats} seats car.')

    car_start = my_car1.start
    car_start()
    print(car_start)
    print(type(car_start))

    car_start = my_car2.start
    car_start()
    print(car_start)
    print(type(car_start))

if __name__ == '__main__':
    run_test1()

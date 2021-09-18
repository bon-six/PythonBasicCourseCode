

def calc_total(a, b):
    return(a+b)

print(calc_total(b=32.0, a=3))


print(calc_total(3,2))



a = calc_total(3.5, 40)
print(a)



def add_all_of_list(source_list):
    total = 0
    for item in source_list:
        total = total+item
    return total


list1 = [1,3,5,7,9]
s1 = add_all_of_list(list1)
print(s1)


def area_of_rect(width, length=5):
    return width * length

#print(area_of_rect())
print(area_of_rect(3))
print(area_of_rect(3,4))

def calc_total(number1, *numbers):
    total = number1
    for item in numbers:
        total += item
    return total

print(calc_total(10,20,30))


def print_student_rec(**student):
    for key, value in student.items():
        print(key, ':', value)

print_student_rec(name='John',age=18,sex='Male',address='some place in Malaysia')




# variable defined outside any function is global
a = 10
b = 20


# argument name are local to the function
def square(a):
    return a*a


print(square(20))  # inside square() function the 'a' will take value 20, not 10.

print(a)  # here the a is only 10, does not have any relation with the argument inside square() function


# variable inside the function are also local to the function
def square2(a):
    b = a*a
    return b


print(square2(20))
print(b)


# using global decalare to refer to variable outside of function
def square3(a):
    global b
    b = a*a
    return b

print(square3(20))
print(b)  # b changed by the square3() function, inside that used global variable.

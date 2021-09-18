
number_list = [i for i in range(2, 101)]

i = 0
j = number_list[i]
while j*j <= number_list[-1]:
    k = j
    while (c:=j*k) <= number_list[-1]:
        if c in number_list:
            number_list.remove(c)
        k+=1
    i+=1
    j = number_list[i]

print(number_list)

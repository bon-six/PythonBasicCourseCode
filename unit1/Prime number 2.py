
prime_list = []

for i in range(2,101):
    is_prime = 1
    for j in prime_list:
        if j*j > i: break
        if i%j == 0 :
            is_prime = 0
            break;
    if is_prime:
        prime_list.append(i)

print(prime_list)
        

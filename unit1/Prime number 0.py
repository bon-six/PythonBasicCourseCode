
for i in range(2,101):
    for j in range(2,i+1):
        if i%j == 0 :
            break;
    if j==i:  # only j==i is a factor. before i, every number is not a factor. so i is prime.
        print(i)
print("End!")
        

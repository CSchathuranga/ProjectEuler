tota=0
totb=0
for i in range(1,1000):
    if(i%3==0):
        tota=tota+i
    elif(i%5==0):
        totb=totb+i
total=tota+totb
print(total)

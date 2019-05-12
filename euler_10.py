import time
start = time.time()

def is_prime(num):
    prime = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            prime = False
            break
    return prime
sum_prime = 0
for i in range(2,2000000):
    if is_prime(i):
        sum_prime += i
print("sum: ",sum_prime)

elapsed = (time.time() - start)
print("This code took: " + str(elapsed) + " seconds")
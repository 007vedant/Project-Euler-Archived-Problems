import math
check=[]
for num in range(2,110001):
   if num > 1:
       for i in range(2,int(math.sqrt(num))+1):
           if (num % i) == 0:
               break
       else:
           check.append(num)
print(len(check))
print(check[10000])

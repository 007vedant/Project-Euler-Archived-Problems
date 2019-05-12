first=0
second=1
sum=0
while second<=4000000:
 if second%2==0:
  sum+=second
 first,second=second, first+second
print(sum)
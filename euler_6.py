_sumofsquare=0
sum=0
for i in range(1,101):
 _sumofsquare+=i**2
 sum+=i
diff=(sum**2)-_sumofsquare
print(diff)
 
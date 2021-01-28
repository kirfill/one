sum = 0
with open("Perepis.txt", "r") as f:
     for i in f:
         print(i)
         if int(i[-5:])<1978:
             sum+=1
print(sum)



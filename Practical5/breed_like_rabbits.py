# create variables:n,t
# calculate the total number of the rabbits:t=n*2
t = 1
n = 1
# caculate the total number of rabbits that will be born each generation
for n in range(1,100):
    t = t*2
    if t<=100:
       print ("the number of rabbits of the",n,"generation is",t)
    else:
         print ("the number of generations required to exceed 100 rabbits is",n)
         break

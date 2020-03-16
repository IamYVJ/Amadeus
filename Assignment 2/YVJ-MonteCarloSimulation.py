import random

t = int(input("No of tests: "))
n = int(input("No of buckets: "))
m = int(input("No of items in each bucket: "))

s = 0

for _ in range(t):
    a = [m]*n
    while True:
        x = random.randint(0, n-1)
        a[x] -=1 
        if 0 in a:
            break
    b = sum(a)/(n-1)
    s += b 

print("Average Left: ", (s/t))
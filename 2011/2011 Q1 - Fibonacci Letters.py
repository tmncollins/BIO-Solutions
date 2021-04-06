import time

a, b, c = input().split()
c = int(c)
start = time.time()

if c == 1: print(a)
if c == 2: print(b)

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
a = alpha.index(a) + 1
b = alpha.index(b) + 1

for i in range(max(0, c-2)):
    A = (a+b) % 26
    if A == 0: A = 26
    a = b
    b = A
#    print(A)
#    print(alpha[b-1])

if c > 2:
    print(alpha[b-1])

print("Time:", time.time() - start)

"""
b) F + R = X
   Q + Q = H
   
c) 
"""
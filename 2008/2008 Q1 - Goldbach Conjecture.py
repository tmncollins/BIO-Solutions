import time
import math

primes = [2]

for i in range(3,10000):
    prime = True
    for p in primes:
        if p > i**0.5: break
        if i % p == 0:
            prime = False
            break
    if prime:
        primes.append(i)

n = int(input())
start = time.time()

tot = 0
for p in primes:
    if p > n: break
    q = n - p
    if q in primes:
#        print(p, "+", q)
        tot += 1

print(math.ceil(tot / 2))


print("Time:", time.time() - start)

"""
b)
3 + 43
5 + 41
17 + 29
23 + 23

c) 
"""

# code for c
"""
tot = 0
for i in range(5, 50, 2):
    valid = False
    for p in primes:
        if p > i: break
        w = i - p
        if w in primes:
            valid = True
            break
    if not valid:
        tot += 1

print(tot)
"""

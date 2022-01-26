from functools import lru_cache
from time import time

def isPat(n):
    if len(n) == 1: return True
    if len(n) == 2:
        return n[0] > n[1]

    for i in range(1, len(n)):
        if isPat(n[:i][::-1]) and isPat(n[i:][::-1]):
            if min(n[:i]) > max(n[i:]): return True
    return False

a,b = input().split()
start = time()

if isPat(a):
    print("YES")
else:
    print("NO")
if isPat(b):
    print("YES")
else:
    print("NO")
if isPat(a+b):
    print("YES")
else:
    print("NO")

#print(time() - start)

def d():
    # initialise with number of pats for 0 and 1 length strings
    pats = [0, 1]
    for i in range(2, 25):
        a, b = 1, i - 1
        counter = 0
        while b > 0 and a < i:
            counter += pats[a] * pats[b]
            a += 1
            b -= 1
        pats.append(counter)
    print(pats[24])



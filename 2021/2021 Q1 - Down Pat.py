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


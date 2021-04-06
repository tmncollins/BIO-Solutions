from collections import defaultdict
from itertools import combinations_with_replacement as combs
from functools import lru_cache
from time import time

"""
THIS SOLUTION IS FAR TOO SLOW FOR SOME TEST CASES
"""

#@lru_cache(maxsize=None)
def getFreq(arr1,arr2):
    freq = defaultdict(int)
    for a in arr1:
        for b in arr2:
            freq[a+b] += 1
    return freq

def getSums(n):
    sums = set()
    for i in range(1,n//2+1):
        sums.add((i, n-i))
    return sums


n = int(input())
dieA = tuple(map(int, input().split()))
dieB = tuple(map(int, input().split()))
DIEA = sorted(dieA)
DIEB = sorted(dieB)

start = time()

freq = getFreq(dieA, dieB)
minimum = min(dieA) + min(dieB)
maximum = max(dieA) + max(dieB)

# generate possible smallest numbers
smallest = getSums(minimum)
largest = 0
for item in smallest:
    largest = max(largest, maximum - min(item))

tot = sum(dieA) + sum(dieB)

nums = list("123456789ABC")
conv = dict(zip(nums, [i for i in range(1,14)]))

options = list(combs(nums[:largest-1], n))
p = len(options)
c = 0
impossible = True
for dieA in options:
    dieA = [conv[i] for i in dieA]
    for dieB in options:
        c += 1
        dieB = [conv[i] for i in dieB]
        if dieA < dieB: break
        if sum(dieA) + sum(dieB) != tot: continue
        if min(dieA) + min(dieB) != minimum: continue
        if max(dieA) + max(dieB) != maximum: continue
        if getFreq(dieA, dieB) == freq:
            if sorted(dieA) in [DIEA, DIEB] and sorted(dieB) in [DIEA, DIEB]: continue
            print(" ".join(list(map(str, dieA))))
            print(" ".join(list(map(str, dieB))))
            print("Time:", time() - start)
            impossible = False

if impossible:
    print("Impossible")

print("Time:", time() - start)

"""
b) 1 5 6 7 9 10, 3 4 5 7 8 9
   2 3 4 6 7 8, 2 6 7 8 10 11
   1 2 3 5 6 7, 3 7 8 9 11 12
   The minimum is 4 and the maximum is 19
   
c) Largest: n^2
   Smallest: 1 
   
d) 
   
"""





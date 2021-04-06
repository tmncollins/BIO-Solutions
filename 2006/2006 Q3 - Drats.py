import time
from functools import lru_cache

s, d = list(map(int, input().split()))
start = time.time()

c = 0

@lru_cache(maxsize=None)
def perm_drats(drats, score):
#    print(drats, score)
    if drats == 0 and score == 0:
        return 1
    elif drats <= 0 or score <= 0:
        return 0
    return sum([perm_drats(drats - 1, score - i) for i in range(1,21)])

print(sum([perm_drats(d - 1, s - i*2) for i in range(1,21)]))

"""
b) 61 for 2; 81 for 3

c) 510176

d) No. Numbers which are high and even must be next to low and odd numbers and vice versa. If a board contains high and 
even numbers, it cannot therefore contain high and odd or low and even numbers. The numbers 1 to 20 contain numbers 
which are low and odd, low and even, high and odd, and high and even.

"""

# code for c
"""
from itertools import combinations, permutations
combs = list(combinations([i for i in range(1,21)], 6))
print(len(combs))
tot = 0
c = 0
for it in combs:
    c += 1
    if c % 100 == 0: print(c)
    p = permutations(it)
    for item in list(p):
        a = item[0] * 2 + item[1] + item[2]
        b = item[3] * 2 + item[4] + item[5]
#        print(a,b)
        if a == b:
            tot += 1
print(tot)
"""

import time
import functools
from itertools import combinations_with_replacement as combs
from functools import lru_cache

p, i, n, w = list(map(int, input().split()))

start = time.time()

@lru_cache(maxsize=None)
def perm_weight(weight, items, maxWeight):
    if weight == 0 and items == 0:
        return 1
    elif weight <= 0 or items <= 0:
        return 0
    return sum([perm_weight(weight - i, items - 1) for i in range(1, maxWeight+1)])

def perm_parcels(parcels, maxWeight, items, weight):
    if parcels == 0 and items == 0:
        return 1
    elif parcels <= 0 and items <= 0:
        return 0
    return sum([perm_parcels(parcels - 1, maxWeight, items - i, weight) * perm_weight(weight, i, maxWeight) for i in range(1, items + 1)])

print(perm_parcels(p,i,n,w))



print("Time:", time.time() - start)

"""
b) 

"""



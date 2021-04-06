from functools import lru_cache
import time

n = int(input())
points = set(map(int, input().split()))

@lru_cache(maxsize=None)
def sumFactors(n):
    global points
    factors = []
    for i in range(min(points),n//2+1):
        factors.append((i, n-i))
    return factors

m = int(input())
scores = list(map(int, input().split()))
start = time.time()

#print(points)

@lru_cache(maxsize=None)
def minPoints(n):
    global points
#    print(n)
    if n == 0 or n in points:
        return 1, [n]
    ans = []
    items = []
    for pair in sumFactors(n)[::-1]:
        tot = minPoints(pair[0])[0] + minPoints(pair[1])[0]
        ans.append(tot)
#        print(pair[0], minPoints(pair[0]))
        items.append(minPoints(pair[0])[1] + minPoints(pair[1])[1])
    if len(sumFactors(n)) == 0:
        return float("inf"), []
    return min(ans), items[ans.index(min(ans))]

for s in scores:
    ans = minPoints(s)
    if ans[0] == float("inf"):
        print("Impossible")
    else:
        print(ans[0], end=" ")
        for item in set(ans[1]):
            print(str(ans[1].count(item)) + "x" + str(item), end=" ")
        print()

print("Time:", time.time() - start)

"""
b) For difference of 80 - 2 rounds between them ([1], [81])
   For difference of 50 - 4 rounds ([1,3,27 = 41], [81])
   
c) 1333
"""

points = [1,4,5,17,28,43,100]
def c(last, score):
    if score == 100: return 1
    if score > 100: return 0
    tot = []
    for item in points:
        if item >= last:
            tot.append(c(item, score + item))
    return sum(tot)
#print(c(0, 0))
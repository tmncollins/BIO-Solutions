from collections import defaultdict
import time

p, s, n = list(map(int, input().split()))
p -= 1
seq = list(map(int, input().split()))

start = time.time()

places = defaultdict(int)

def pToPos(a):
    y = a // 5
    x = a % 5
    return (x,y)

def draw():
    for y in range(5):
        for x in range(0,5):
            print(places[(x,y)],end="")
        print()
    print()

for i in range(n):
    places[pToPos(p)] += 1

    while True:
        handled = True
        for item in list(places.keys()):
            while places[item] >= 4:
                places[item] -= 4
                places[(item[0]-1, item[1])] += 1 # left
                places[(item[0]+1, item[1])] += 1 # right
                places[(item[0], item[1]-1)] += 1 # up
                places[(item[0], item[1]+1)] += 1 # down
                handled = False
        if handled:
            break

    p = (p + seq[i % len(seq)]) % 25

draw()

print("Time:", time.time() - start)

"""
b) 4 * 4 = 16 people 
c) 20
Example:
21 3 8
12 18 5

Code is below

d) No. Some ending landscapes can be created by multiple different starting landscapes. If a migration occurred
from the position and the there is still someone remaining at that position then it is also possible that a migration
didn't occur and that the person was just placed there. For example:

0 0 0 0    0 1 0 0
0 3 0 0    1 0 1 0
0[3]0 0 -> 1 1 1 0
0 0 0 0    0 1 0 0

but also

0 1 0 0    0 1 0 0
1 0 1 0    1 0 1 0
1[0]1 0 -> 1 1 1 0
0 1 0 0    0 1 0 0
"""

"""
Code for part C

from _collections import defaultdict

ans = "1010010100100001010010000"

for i in range(25):
    print(i)
    for a in range(24):
        for b in range(24):
            for c in range(24):
                seq = [a,b,c]
                p = i - 1
                places = defaultdict(int)
                for k in range(8):
                    places[p] += 1
                    p = (p + seq[k % len(seq)]) % 25

                n = ""
                for k in range(25):
                    n += str(places[k])
                if n == ans:
                    print(i, 3, 8)
                    print(a, b, c)
                    print()
"""

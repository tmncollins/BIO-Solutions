"""

AUTHOR: Isaac Eason
GITHUB: codethat01

"""

import time as TIME

def putchar(depth, b1, b2, x):
    if x == b1 or x == b2:
        char = "X"
    elif depth == 0:
        char = "-"
    elif depth > 0:
        char = "*"
    else:
        char = "o"
    print(char, end="")

p = int(input())
pebbles = []
for _ in range(p):
    pebbles.append(list(map(int, input().split())))
b1, b2 = map(int, input().split())
gap = b2-b1-1
left = []
mid = []
right = []
for pebble in pebbles:
    if pebble[0] < b1:
        left.append(pebble)
    elif pebble[0] > b2:
        right.append(pebble)
    else:
        mid.append(pebble)
t = int(input())

start = TIME.time()

for y in range(4, -5, -1):
    for x in range(-4, 5):
        depth = 0
        if x < b1:
            for time, value in ((t, 1), (t-2, -1)):
                for pebble in left:
                    tdiff = time - pebble[2]
                    dx, dy = abs(pebble[0]-x), abs(pebble[1]-y)
                    dwall = b1-pebble[0]
                    dpix = b1-x-1
                    if dy + dx == tdiff:
                        depth += value
                    if dy + dpix + dwall == tdiff:
                        depth += value
        elif x > b2:
            for time, value in ((t, 1), (t-2, -1)):
                for pebble in right:
                    tdiff = time - pebble[2]
                    dx, dy = abs(pebble[0]-x), abs(pebble[1]-y)
                    dwall = pebble[0]-b2
                    dpix = x-b2-1
                    if dy + dx == tdiff:
                        depth += value
                    if dy + dpix + dwall == tdiff:
                        depth += value
        elif b1 < x and x < b2:
            for time, value in ((t, 1), (t-2, -1)):
                for pebble in mid:
                    tdiff = time-pebble[2]+1
                    ldx, rdx, dy = pebble[0]-b1, b2-pebble[0], abs(pebble[1]-y)
                    lpix, rpix = x-b1, b2-x
                    dxreq = tdiff-dy
                    if (dxreq-ldx-lpix) % (2*gap) == 0 and dxreq-ldx-lpix >= 0:
                        depth += value
                    if (dxreq-ldx-rpix+gap) % (2*gap) == 0 and dxreq-ldx-rpix+gap > 0:
                        depth += value
                    if (dxreq-rdx-rpix) % (2*gap) == 0 and dxreq-rdx-rpix >= 0:
                        depth += value
                    if (dxreq-rdx-lpix+gap) % (2*gap) == 0 and dxreq-rdx-lpix+gap > 0:
                        depth += value
                    if dxreq-1 == abs(pebble[0]-x):
                        depth += value

        putchar(depth, b1, b2, x)
    print()

print("Time taken:", TIME.time() - start)

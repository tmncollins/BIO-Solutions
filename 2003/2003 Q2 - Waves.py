import time
from collections import defaultdict

"""
NOTE THAT THIS SOLUTION IS FAR TO SLOW FOR SOME TEST CASES
LOOPS NEED TO BE SKIPPED FOR INSTANCE
"""

p = int(input())

pebbles = []
for i in range(p):
    x,y,t = list(map(int, input().split()))
    pebbles.append((t,(x,y)))
pebbles = sorted(pebbles)

banks = list(map(int, input().split()))
r = int(input())

waves = defaultdict(set)
pebbleThrow = dict()
dir = ["UL", "UR", "DL", "DR"]
allD = "A"

# draw the location
def draw():
    for y in range(4, -5, -1):
        for x in range(-4, 5):
            if x in banks:
                print("X", end="")
            elif (x,y) in waves.keys():
                h = 0
                seen = set()
                for item in waves[(x,y)]:
                    H, w = item[1]
                    if w not in seen:
                        seen.add(w)
                        h += H
                if h > 0: print("*", end="")
                elif h < 0: print("O", end="")
                else: print("-", end="")
            else:
                print("-", end="")
        print()

start = time.time()

waveID = 0

for i in range(1, r+1):
#    print(i, len(waves), time.time() - start)
    # Update waves
    newWaves = defaultdict(set)
    for key in waves.keys():
        for wave in waves[key]:
            # REMEMBER TO TRIM INFO!

            d, h = wave
            if "U" in d and key[1] - 1 > -7:
                newWaves[(key[0], key[1] - 1)].add((d, h))  # up
            if "L" in d:
                # check if hit bank
                if key[0] - 1 in banks:
                    newWaves[(key[0], key[1])].add((d.replace("L", "R"), h))  # hit bank
                else: newWaves[(key[0] - 1, key[1])].add((d, h))  # left
            if "R" in d:
                if key[0] + 1 in banks:
                    newWaves[(key[0], key[1])].add((d.replace("R", "L"), h))  # hit bank
                else: newWaves[(key[0] +1, key[1])].add((d, h))  # right
            if "D" in d and key[1] - 1 < 6:
                newWaves[(key[0], key[1] + 1)].add((d, h))  # down

    # Condense this
    """
    for wave in lisnewWaves.keys():
        d = defaultdict(int)
        for item in newWaves[wave]:
            direction, h = item
            print(item)
            d[direction] += h[0]
        newWaves.pop(wave)
        for k in d.keys():
            newWaves[wave].add((k, (d[k], waveID)))"""

    waves = newWaves.copy()

    # update second waves
    if len(pebbleThrow) > 0:
        toRemove = []
        for key in pebbleThrow.keys():
            item = pebbleThrow[key]
            item -= 1
            if item == 0:
                toRemove.append(key)
                waveID += 1
                for d in dir:
                    waves[key].add((d, (-1, waveID)))
            else:
                pebbleThrow[key] = item
        for item in toRemove:
            pebbleThrow.pop(item, None)

    while len(pebbles) > 0 and i == pebbles[0][0]:
        # throw in some pebbles
        peb = pebbles.pop(0)
        loc = peb[1]
        pebbleThrow[loc] = 2
        waveID += 1
        for d in dir:
            waves[loc].add((d, (1, waveID)))


#    draw()
#    print()

draw()

print("Time:", time.time() - start)

"""
2
-3 0 1
0 0 2
4 100
4 

"""
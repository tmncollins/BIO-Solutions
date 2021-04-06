from _collections import defaultdict
import time


def explore(t, instructions, m, partd=False):
    trail = defaultdict(int)
    pos = (0, 0)
    d = 0
    # 0 - up, 1 - right, 2 - down, 3 - left
    right = {0: 1, 1: 2, 2: 3, 3: 0}
    left = {1: 0, 0: 3, 3: 2, 2: 1}
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for i in range(m):
        if not partd:
            toRemove = []
            for item in trail:
                trail[item] -= 1
                if trail[item] == 0:
                    toRemove.append(item)
            for item in toRemove:
                trail.pop(item)
        trail[pos] = t
#        print(len(trail))
        move = instructions[i%len(instructions)]
        if move == "L":
            d = left[d]
        elif move == "R":
            d = right[d]

        moved = False

        for _ in range(4):
            if (pos[0] + dir[d][0], pos[1] + dir[d][1]) not in trail:
                moved = True
                pos = (pos[0] + dir[d][0], pos[1] + dir[d][1])
                break
            d = right[d]

        if not moved:
            # part d
            print("stuck")
            if partd: return i
            break
    return pos


t, instructions, m = input().split()
t, m = int(t), int(m)

start = time.time()

print(explore(t,instructions,m))
#print(trail)
print("Time:", time.time() - start)

"""
b) 00000
   00345
   01206
   0D017
   00000
   
c) 21 * 21 - 1 = 440

d) 
"""
#print(explore(1, "LLRFFF", 9999999, partd=True))

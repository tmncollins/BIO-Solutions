from collections import deque
import time

grid = [list(input()) for _ in range(4)]

original = []
for x in range(4):
    a = []
    for y in range(4):
        a.append(grid[y][x])
    original.append(deque(a))

blocks = list()
seen = set()

def getBlocks():
    global grid, blocks, seen
    seen = set()
    blocks = []

    for y in range(4):
        for x in range(4):
            if (x,y) not in seen:
                curr = []
                pending = [(x,y)]
                t = grid[y][x]
                while len(pending) > 0:
                    item = pending.pop(0)
                    if grid[item[1]][item[0]] == t:
                        if item not in seen: curr.append(item)
                        seen.add(item)
                        if item[1] > 0 and (item[0], item[1] - 1) not in seen:
                            pending.append((item[0], item[1] - 1))
   #                         seen.add((item[0], item[1] - 1))
                        if item[0] > 0 and (item[0] - 1, item[1]) not in seen:
                            pending.append((item[0] - 1, item[1]))
  #                          seen.add((item[0] - 1, item[1]))
                        if item[1] < 3 and (item[0], item[1] + 1) not in seen:
                            pending.append((item[0], item[1] + 1))
 #                           seen.add((item[0], item[1] + 1))
                        if item[0] < 3 and (item[0] + 1, item[1]) not in seen:
                            pending.append((item[0] + 1, item[1]))
#                            seen.add((item[0] + 1, item[1]))
                if len(curr) > 1:
                    blocks.append(curr)

def removeBlanks():
    global grid
    while True:
        moved = False
        for x in range(4):
            for y in range(3):
                if grid[y][x] != "-" and grid[y+1][x] == "-":
                    grid[y+1][x] = grid[y][x]
                    grid[y][x] = "-"
                    moved = True
        if not moved: break

    # moves things down
    while True:
        for x in range(4):
            if grid[0][x] == "-":
                grid[0][x] = original[x][-1]
                original[x].rotate(1)
        moved = False
        for x in range(4):
            for y in range(3):
                if grid[y][x] != "-" and grid[y+1][x] == "-":
                    grid[y+1][x] = grid[y][x]
                    grid[y][x] = "-"
                    moved = True
        if not moved: break


def draw():
    for y in range(4):
        print("".join(grid[y]))


gameOver = False
score = 0
while True:
    n = int(input())
    start = time.time()
    if n == 0: break
    for i in range(n):
        getBlocks()
        if len(blocks) == 0:
            gameOver = True
            break

        # Remove blocks
        for block in blocks:
            for b in block:
                grid[b[1]][b[0]] = "-"

        # calculate score
        s = 1
        for block in blocks:
            s *= len(block)
        score += s

        removeBlanks()
    if gameOver:
        print("GAME OVER")
        print(score)
        break

    draw()
#    print(blocks)
    print(score)
    print("Time:", time.time() - start)

"""
b) 105 = 5 * 3 * 7
RRRR
BBBR
GGGG
GGGR

c) 3 * 3 * 3 * 4 = 324


"""

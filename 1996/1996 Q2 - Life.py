alive = set()
dead = set()
for y in range(11):
    for x in range(11):
        dead.add((x,y))

def getNumNeighbours(pos, alive):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1), (1, 0), (1, -1)]
    neighbours = 0
    for d in directions:
        if (pos[0] + d[0], pos[1] + d[1]) in alive: neighbours += 1
    return neighbours

def nextGeneration(alive, dead, n):
    if n == 0: return alive
    next = set()
    nextD = set()
    for item in alive:
        num = getNumNeighbours(item, alive)
        if num in {2,3}:
            # lives
            next.add(item)
        else:
            nextD.add(item)
    for item in dead:
        num = getNumNeighbours(item, alive)
        if num == 3:
            # birth
            next.add(item)
        else:
            nextD.add(item)

    return nextGeneration(next, nextD, n-1)

def output(alive):
    for y in range(11):
        for x in range(11):
            if (x,y) in alive:
                print("0", end="")
            else:
                print(".", end="")
        print()

def setup():
    global alive, dead
    alive = set()
    dead = set()
    for y in range(11):
        for x in range(11):
            dead.add((x, y))

    for y in range(5):
        line = list(input())
        for x in range(len(line)):
            if line[x] == "0":
                pos = (x+3, y+3)
                dead.remove(pos)
                alive.add(pos)

curr = 0
setup()
output(alive)
while True:
    val = input()
    a = set(alive)
    if val == "-1": break
    if val[0] == "#":
        n = int(val[1:])
        a = nextGeneration(a, set(dead), n)
        curr = n
    if val[0] == "+":
        n = int(val[1:])
        curr += n
        a = nextGeneration(a, set(dead), curr)

    output(a)

"""
b) It is not feasible to have an -n function because several different boards can have identical future generations, 
thus there may not be a unique preceding generation to the current one. Furthermore, there might not even be a preceding
generation, for example, if the entire board is full. 

c) 262,144
Note that survival and death rules are the same, and that survival and birth are the same, but with a different centre.
As there are 9 cells that affect the current cell (including the cell itself), there are 2^9 birth conditions and
2^9 survival conditions, giving 512 * 512 conditions

d) 
"""
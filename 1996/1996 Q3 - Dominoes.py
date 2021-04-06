from _collections import defaultdict

connectors = defaultdict(tuple)
values = defaultdict(int)

dominoes = set()
doubles = [(i, i) for i in range(7)]

validPlaces = set()

def generateDominoes():
    global dominoes
    dominoes = set()
    for a in range(7):
        for b in range(7):
            if a < b:
                dominoes.add((a,b))

    for y in range(7):
        for x in range(8):
            validPlaces.add((x,y))

    for item in validPlaces:
        values[item] = -1

def output():
    for y in range(7):
        linebelow = ""
        for x in range(8):
            space = " "
            spaceb = "  "
            if connectors[(x,y)] == (x+1, y):
                space = "-"
            elif connectors[(x,y)] == (x, y+1):
                spaceb = "| "
            linebelow += spaceb
            if values[(x,y)] > -1:
                print(str(values[(x,y)]) + space, end="")
            else:
                print("."+ space, end="")
        print()
        print(linebelow)

generateDominoes()

# place fixed dominoes
ans = ""
while True:
    line = input()
    if line == "-1": break
    x,y,d = line.split()
    x, y = int(x) - 1, int(y) - 1
    second = (0,0)
    if d == "B":
        second = (x, y+1)
    elif d == "R":
        second = (x+1, y)
    else:
        ans = "Impossible"
    if (x,y) in validPlaces and second in validPlaces:
        validPlaces.remove((x,y))
        validPlaces.remove(second)
        tile = doubles.pop(0)
        values[(x,y)] = tile[0]
        values[second] = tile[0]
        connectors[(x,y)] = second
        connectors[second] = (x,y)
    else:
        ans = "Impossible"

def getAround(pos):
    around = set()
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    for d in directions:
        p = (pos[0] + d[0], pos[1] + d[1])
        if p in validPlaces:
            around.add(values[p])
    return around

def tryPlace(left, pos):
    global validPlaces, connectors, values, dominoes
    if left:
        second = (pos[0] + 1, pos[1])
        left = getAround(pos)
        right = getAround(second)
        dir = None
        for d in dominoes:
            if d[0] not in left and d[1] not in right:
                dir = d
                break
            d = d[::-1]
            if d[0] not in left and d[1] not in right:
                dir = d
                break
        if dir != None:
            values[pos] = dir[0]
            values[second] = dir[1]
            validPlaces.remove(pos)
            validPlaces.remove(second)
            connectors[pos] = second
            connectors[second] = pos
            if dir in dominoes:
                dominoes.remove(dir)
            else:
                dominoes.remove(dir[::-1])
            return True

        return False
    else:
        second = (pos[0], pos[1] + 1)
        left = getAround(pos)
        right = getAround(second)
        dir = None
        for d in dominoes:
            if d[0] not in left and d[1] not in right:
                dir = d
                break
            d = d[::-1]
            if d[0] not in left and d[1] not in right:
                dir = d
                break
        if dir != None:
            values[pos] = dir[0]
            values[second] = dir[1]
            validPlaces.remove(pos)
            validPlaces.remove(second)
            connectors[pos] = second
            connectors[second] = pos
            dominoes.remove(dir)
            return True

        return False

# place all other dominoes
dominoes = dominoes.union(set(doubles))
for y in range(7):
    for x in range(8):
        if (x,y) in validPlaces:
            # try placing left-right first
            if (x+1, y) in validPlaces:
                result = tryPlace(True, (x,y))
                if not result:
                    if (x, y+1) in validPlaces:
                        result = tryPlace(False, (x,y))
                        pass
                    if not result:
                        ans = "Impossible"
            # try placing up-down else
            elif (x, y+1) in validPlaces:
                result = tryPlace(False, (x,y))
                if not result:
                    ans = "Impossible"
            else:
                ans = "Impossible"

if ans == "Impossible":
    print(ans)
else:
    output()
#    print(dominoes)

"""
b) Yes. When can iterate through the permutations of the fixed doubles: 0-6, each of which will give another
valid solution.

c) 

"""




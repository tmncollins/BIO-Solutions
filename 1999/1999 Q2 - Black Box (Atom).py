atoms = set()
entered = set()

def screenToBoard(x,y):
    x -= 1
    y = 10 - y
    return x,y

def boardToScreen(x,y):
    x += 1
    y = 10 - y
    return x,y

def printBoard():
    for y in range(10):
        for x in range(10):
            if (x,y) in entered:
                if (x,y) in atoms: print("*", end="")
                else: print("+",end="")
            elif(x,y) in atoms: print("A", end="")
            else: print(".",end="")
        print()

sideToDir = {"T":"D", "L":"R", "R":"L", "B":"U"}
dirToSide = {"D":"B", "L":"L", "R":"R", "U":"T"}
directions = {"U":(0,-1), "L":(-1,0), "R":(1,0), "D":(0,1)}

def onBoard(x,y):
    return x >= 0 and y >= 0 and y < 10 and x < 10

def fireRay(side, loc):
    global entered, atoms
    entered = set()
    d = sideToDir[side]
    pos = (0,0)
    if side == "L": pos = (0, 10-loc)
    if side == "R": pos = (9, 10-loc)
    if side == "T": pos = (loc-1, 0)
    if side == "B": pos = (loc-1, 9)
#    print(pos, d)
    while True:
        entered.add(pos)
        if pos in atoms:
            return "Absorbed"
        if not onBoard(pos[0], pos[1]):
            if dirToSide[d] in ["T","B"]:
                return "Exits at " + dirToSide[d] + " " + str(boardToScreen(pos[0], pos[1])[0])
            return "Exits at " + dirToSide[d] + " "+ str(boardToScreen(pos[0], pos[1])[1])

        move = directions[d]
        next = (pos[0] + move[0], pos[1] + move[1])
        if next in atoms:
            pass
        # up right
        elif (pos[0]+1, pos[1]-1) in atoms:
            d = "D" if d == "R" else "L"
            if (pos[0]+1, pos[1]+1) in atoms or (pos[0]-1, pos[1]-1) in atoms: return "Reflected"
        # down right
        elif (pos[0]+1, pos[1]+1) in atoms:
            d = "U" if d == "R" else "L"
            if (pos[0]+1, pos[1]-1) in atoms or (pos[0]-1, pos[1]+1) in atoms: return "Reflected"
        # up left
        elif (pos[0]-1, pos[1]-1) in atoms:
            d = "D" if d == "L" else "R"
            if (pos[0]-1, pos[1]+1) in atoms or (pos[0]+1, pos[1]-1) in atoms: return "Reflected"
        # down left
        elif (pos[0]-1, pos[1]+1) in atoms:
            d = "U" if d == "L" else "R"
            if (pos[0]-1, pos[1]-1) in atoms or (pos[0]+1, pos[1]+1) in atoms: return "Reflected"
        move = directions[d]
        pos = (pos[0] + move[0], pos[1] + move[1])







for i in range(5):
    x,y = list(map(int, input().split()))
    x,y = screenToBoard(x,y)
    atoms.add((x,y))

printBoard()

while True:
    side, loc = input().split()

    if side == "X": break
    loc = int(loc)

    result = fireRay(side, loc)
    printBoard()
    print(result)

"""
b) 4
..........
.A........
..........
..........
....A.....
..........
.......A..
..........
........A.
..........

c) 
It can travel straight from top to bottom.
It can be deflected in a kink to the right, up to 4 places, with 
It can be deflected in a king to the left, up to 3 places, with 

d) A ray cannot enter a square exactly 3 times. If a ray enters a square twice in the same direction, it must be stuck
in an infinite loop, and so will enter the square infinitely many times. If the ray has entered a square 3 times it 
must have either entered that square from the top and bottom, or from the left and right, meaning it must have been
reflected at some point. A reflected ray will always enter squares an even number of times, x times going forwards and
x times going backwards. 

A ray can enter a square exactly 4 times. A ray can enter a square twice due to deflections. If the ray is then reflected,
it passes back through the square twice again. For example:

..A...A
...+++.
A..+.+.
.+++++.
A..+..A
...+...

"""
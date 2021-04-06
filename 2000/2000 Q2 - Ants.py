

board = [["." for _ in range(11)] for _ in range(11)]

clockwise = {"T":"R", "R":"B", "B":"L", "L":"T"}
anticlock = {"T":"L", "L":"B", "B":"R", "R":"T"}
directions = {"T":(0,-1), "R":(1,0), "B":(0,1), "L":(-1,0)}
flip = {"*":".", ".":"*"}

def convertToBoard(x,y):
    x -= 1
    y = 11 - y
    return x,y

def convertToScreen(x,y):
    x += 1
    y = 11 - y
    return x,y

ant1 = input().split()
x,y = convertToBoard(int(ant1[0]), int(ant1[1]))
ant1 = (x,y,ant1[2])

ant2 = input().split()
x,y = convertToBoard(int(ant2[0]), int(ant2[1]))
ant2 = (x,y,ant2[2])
removed1 = False
removed2 = False



def drawBoard():
    for line in board:
        print("".join(line))

def outside(x,y):
    return x < 0 or y < 0 or x >= 11 or y >= 11

def move(ant):
    global board
    x,y,d = ant
    dir = directions[d]

    # move
    x += dir[0]
    y += dir[1]
    if outside(x,y): return ant, True

    # rotate
    if board[y][x] == "*": d = anticlock[d]
    else: d = clockwise[d]

    # change colour
    board[y][x] = flip[board[y][x]]

    # return ant
    return (x,y,d), False



while True:
    n = int(input())
    if n == -1: break
    for i in range(n):
        if not removed1:
            ant1, removed1 = move(ant1)
        if not removed2:
            ant2, removed2 = move(ant2)
    drawBoard()
    if removed1: print("Removed")
    else:
        x,y = convertToScreen(ant1[0], ant1[1])
        print(x,y, ant1[2])
    if removed2: print("Removed")
    else:
        x,y = convertToScreen(ant2[0], ant2[1])
        print(x,y, ant2[2])

"""
b) 
.....
..*..
.*...
.*...
.....
..*..
3 4 T
3 6 B

c) No. Ants only turn 90* clockwise or anticlockwise every turn, so they alternate facing horizontally and vertically. 
After an even number of turns, the ant must still be facing horizontally. The ant can only return to its starting square
after an even number of turns and so it must still be facing horizontally.
"""
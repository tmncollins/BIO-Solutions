
board = [[0 for i in range(10)] for _ in range(10)]

def draw():
    for y in range(10):
        for x in range(10):
            print(board[y][x], end="")
        print()

def isValid(x,y):
    if x >= 10 or x < 0 or y < 0 or y >= 10:
        return False
    if board[y][x] == 1:
        return False
    dir = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,-1)]
    for d in dir:
        a = x + d[0]
        b = y + d[1]
        if a < 10 and a >= 0 and b < 10 and b >= 0:
            if board[b][a] == 1: return False
    return True

ships = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

a,c,m = list(map(int, input().split()))
r = 0
for ship in ships:
    placed = False
    while not placed:
        r = ((a*r)+c) % m
        x = r % 10
        y = (r // 10) % 10
        print(x,y, r)
        r = ((a*r)+c) % m
        if r % 2 == 0:
            # right
            canPlace = True
            for i in range(ship):
                if not isValid(x+i, y):
                    canPlace = False
                    break
            if canPlace:
                placed = True
                for i in range(ship):
                    board[y][x+i] = 1
                print(x,y,"H")
        else:
            # up (acc down)
            canPlace = True
            for i in range(ship):
                if not isValid(x, y+i):
                    canPlace = False
                    break
            if canPlace:
                placed = True
                for i in range(ship):
                    board[y+i][x] = 1
                print(x,y,"V")
#    draw()

"""
b) (3,0), (4,0), (8,0), (7,0)

c) 18
A square is guaranteed empty if it is next to at least 2 ships
"""

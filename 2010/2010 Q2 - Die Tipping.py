import time

class Die():
    def __init__(self):
        self.top = 1
        self.bottom = 6
        self.back = 5
        self.front = 2
        self.left = 3
        self.right = 4
        self.heading = "u"
    def tipUp(self):
        a = self.top
        self.top = self.back
        self.back = self.bottom
        self.bottom = self.front
        self.front = a
        self.heading = "u"
    def tipDown(self):
        a = self.top
        self.top = self.front
        self.front = self.bottom
        self.bottom = self.back
        self.back = a
        self.heading = "d"
    def tipLeft(self):
        a = self.top
        self.top = self.right
        self.right = self.bottom
        self.bottom = self.left
        self.left = a
        self.heading = "l"
    def tipRight(self):
        a = self.top
        self.top = self.left
        self.left = self.bottom
        self.bottom = self.right
        self.right = a
        self.heading = "r"

def draw():
    global board, pos
    for y in range(pos[1]-1,pos[1]+2):
        for x in range(pos[0]-1, pos[0]+2):
            if y < 0 or y > 10 or x < 0 or x > 10:
                print("x", end="")
            else:
                print(board[y][x], end="")
        print()


board = [[1 for _ in range(11)] for _ in range(11)]

for i in range(3):
    l = input().split()
    for j in range(len(l)):
        board[4+i][4+j] = int(l[j])

start = time.time()

die = Die()
pos = (5,5)

clock = {"u":"r", "r":"d", "d":"l", "l":"u"}
anticlock = {"u":"l", "l":"d", "d":"r", "r":"u"}

while True:
    n = int(input())
    if n == 0: break
    for _ in range(n):
        v = board[pos[1]][pos[0]] + die.top
        if v > 6: v -= 6
        board[pos[1]][pos[0]] = v
        curr = board[pos[1]][pos[0]]
        if curr in [1,6]:
            # move according to heading
            move = die.heading
        elif curr == 2:
            # move 90* clockwise to heading
            move = clock[die.heading]
        elif curr in [3,4]:
            # move 180* to heading
            move = clock[clock[die.heading]]
        else:
            # move 90* anticlock
            move = anticlock[die.heading]

        if move == "u":
            pos = (pos[0], pos[1] - 1)
            die.tipUp()
        elif move == "r":
            pos = (pos[0] + 1, pos[1])
            die.tipRight()
        elif move == "d":
            pos = (pos[0], pos[1] + 1)
            die.tipDown()
        elif move == "l":
            pos = (pos[0] - 1, pos[1])
            die.tipLeft()

        if pos[0] < 0: pos = (10, pos[1])
        if pos[0] > 10: pos = (0, pos[1])
        if pos[1] < 0: pos = (pos[0], 10)
        if pos[1] > 10: pos = (pos[0], 0)

    draw()

"""
b) 32
   The centre must be a 2 after sum and the other 5 tiles must be 1 or 6 after sum, so 2^5
   
c) 8 for 4 tips
   The die must move in a square of length 1 tip. There are 4 such squares, each of which can be traversed in 2 directions
   160 for 6 tips
   The die can take 2 different shaped paths: 1 square with a forward-back part way through or a 3x2 rectangle.
   There are 4 such squares which can be traversed in 2 directions. At each of the 4 corners of the squares, there are
   4 directions for the forward-back move, giving 4*2*4*4 = 128 paths
   There are 4 such rectangle paths which can be traversed in 2 directions. Each of these rectangles can also be rotated
   in 4 different directions, giving 4*2*4 = 32 path
   
d) No. The numbers on the grid and the die's heading and orientation determines which way the die will move, and so 
   will determine all subsequent moves. There are a finite number of headings and orientations that the die can have
   and a finite number of possible grids. Therefore, eventually the die will come back to a position on a grid that it 
   has been before with the same orientation and heading. Whenever the die returns like this, it must be stuck in a loop
   as it will follow the path it took the last time around as everything is identical and so its moves will be identical.
"""
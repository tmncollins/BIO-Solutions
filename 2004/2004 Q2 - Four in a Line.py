board =[["-" for _ in range(7)] for _ in range(6)]

def willMoveWin(col, p):
    row = len(board) - 1
    for i in range(len(board)):
        if board[i][col] != "-":
            row = i - 1
            break
    if row == -1: return False

    playMove(col, p)

#    draw()

    # check left/right in row
    if p * 4 in "".join(board[row]):
        removeMove(col)
        return True

    # check up/down
    h = ""
    for i in range(len(board)): h += board[i][col]
    if p * 4 in h:
        removeMove(col)
        return True

    # check diagonals including this point
    # check \
    x = max(0, col - row)
    y = max(0, row - col)
    h = ""
    while True:
        if x > 6 or y > 5:
            break
        h += board[y][x]
        x += 1
        y += 1
    if p * 4 in h:
        removeMove(col)
        return True

    # Check / diagonal
    h = ""
    # go left first
    x = col
    y = row
    while True:
        if x < 0 or y >= len(board):
            break
        h = board[y][x] + h
        x -= 1
        y += 1
    # go right
    x = col + 1
    y = row - 1
    while True:
        if x >= len(board[0]) or y < 0:
            break
        h += board[y][x]
        x += 1
        y -= 1
    if p * 4 in h:
        removeMove(col)
        return True

    # otherwise
    removeMove(col)
    return False

def removeMove(col):
    for i in range(len(board)):
        if board[i][col] != "-":
            board[i][col] = "-"
            return

def canPlayMove(col):
    return board[0][col] == "-"

def playMove(col, p):
    row = -1
    for i in range(len(board)):
        if board[i][col] != "-":
            row = i - 1
            break
    board[row][col] = p

def draw():
    for y in range(len(board)):
        print("".join(board[y]))

n = int(input())
m = list(map(int, input().split()))

p1 = "*"
p2 = "o"
player1 = True

for item in m:
    p = p1 if player1 else p2
    playMove(item-1, p)
    player1 = not player1

noWinner = False
def playOneMove():
    global player1, board, noWinner
    p = p1 if player1 else p2
    other = p2 if player1 else p1

    # check if can win
    for col in range(len(board[0])):
        if willMoveWin(col, p):
            playMove(col, p)
            return True # we have won!

    # check if other player will win
    for col in range(len(board[0])):
        if willMoveWin(col, other):
            playMove(col, p)
            return False

    # check if can play anywhere
    for i in range(len(board[0])):
        if canPlayMove(i):
            playMove(i, p)
            return False

    # No more spaces to play
    noWinner = True
    return True

draw()

result = False
while not result:
    q = input()
    if q == "n":
        # play 1 move
        result = playOneMove()
        if result: break
        player1 = not player1
    else:
        # play until finishes
        while True:
            result = playOneMove()
            if result: break
            player1 = not player1
        break
    draw()

draw()
if noWinner: print("Draw")
elif player1: print("Player 1 wins")
else: print("Player 2 wins")

"""
b) Player 2 wins
oo**oo-
**oo**-
oo**oo-
**oo**-
oo*oooo
***o***

c) 15 moves
Players take it in turns to play pieces, player 1 plays the odd numbered turns, player 2 plays the even numbered turns.
When player one plays, they have more pieces in play than player 2. The winning move was first played by player 1, 
where they have at least 8 pieces in play, thus player 2 would have had 7 pieces in play at this point. 
In total, 15 pieces were played to get to this winning moving. The moves to achieve this are below
1 2 2 3 4 3 4 1 3 2 1 1 2 5 1

41 moves is maximum

d) 60691
"""
"""
code for d  ==========================================================================================================

lists = set()
seen = set()

def check(item):
    if (sum(list(item)) == 21):
        print(sum(list(item)), len(lists))
        lists.add(item)
        return
    for i in range(7):
        if item[i] < 6:
            q = list(item)
            q[i] += 1
            if tuple(q) not in seen:
                seen.add(tuple(q))
                check(tuple(q))

check((0,0,0,0,0,0,0))
print(len(lists))
"""
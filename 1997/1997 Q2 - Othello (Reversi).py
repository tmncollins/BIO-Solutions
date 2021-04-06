from collections import defaultdict

board = defaultdict(int) # 0 - empty, 1 - white, 2 - black
tiles = ".0*"
change = {1:2, 2:1}
dir = [(0,1), (0,-1), (1,1), (1,0), (1,-1), (-1,-1), (-1,0), (-1,1)]

def reset():
    global board
    board = defaultdict(int)

def score():
    global board
    black, white = 0, 0
    for y in range(8):
        for x in range(8):
            if board[(x,y)] == 1: white += 1
            elif board[(x,y)] == 2: black += 1
    # return white score, then black
    return white, black

def validMoves():
    global board, dir
    moves = []
    for y in range(8):
        for x in range(8):
            for d in dir:
                if board[(x,y)] == 0 and board[(x + d[0], y + d[1])] > 0:
                    moves.append((x,y))
                    break
    return moves

def validPos(x,y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

def getFlips(x,y,c):
    global board, dir
    flips = set()
    for d in dir:
        i = 0
        curr = set()
        while True:
            i += 1
            if board[(x+d[0]*i,y+d[1]*i)] == 0 or not validPos(x,y): break
            if board[(x+d[0]*i,y+d[1]*i)] == c:
                flips = flips.union(curr)
                break
            curr.add((x+d[0]*i,y+d[1]*i))
    return flips

def printBoard():
    for y in range(8):
        for x in range(8):
            print(tiles[board[(x,y)]], end="")
        print()
    print()

def flipAll(flips):
    global board, change
    for pos in flips:
        board[pos] = change[board[pos]]

def getInput():
    global board, tiles
    for i in range(4):
        line = input()
        for j in range(len(line)):
            l = line[j]
            board[(2+j, 2+i)] = tiles.index(l)

def screenToPos(x,y):
    return (x-1, 8-y)

def displayWinner():
    scores = score()
    d = str(abs(scores[0] - scores[1]))
    if scores[0] > scores[1]:
        # white has won
        print("White wins by " + d + ".")
    elif scores[1] > scores[0]:
        # black has won
        print("Black wins by " + d + ".")
    else:
        # draw
        print("Black and White draw.")

def strategy1():
    reset()
    getInput()
    print("Strategy 1")
    printBoard()

    whiteTurn = True
    while True:
        moves = validMoves()
        if not moves:
            # game is over!
            gameOver = True
            break

        m = int(input())
        if m == -1: break
        if m == 0:
            pos = list(map(int, input().split()))
            pos = screenToPos(pos[0], pos[1])
            flips = getFlips(pos[0], pos[1], 1 if whiteTurn else 2)
            board[pos] = 1 if whiteTurn else 2
            flipAll(flips)

            whiteTurn = not whiteTurn
        else:
            gameOver = False
            for _ in range(m):
                moves = validMoves()
                if not moves:
                    # game is over!
                    gameOver = True
                    printBoard()
                    break

                bestMove = (0,0)
                moveFlips = []
                c = 1 if whiteTurn else 2
                for move in moves:
                    f = getFlips(move[0], move[1], c)
                    if len(f) >= len(moveFlips):
                        moveFlips = f
                        bestMove = move

                board[bestMove] = c
                flipAll(moveFlips)

                whiteTurn = not whiteTurn

            if gameOver: break

        printBoard()


    moves = validMoves()
    if not moves:
        # game is over!
        displayWinner()

def strategy2():
    reset()
    getInput()
    print("Strategy 2")
    printBoard()

    whiteTurn = True
    while True:
        moves = validMoves()
        if not moves:
            # game is over!
            gameOver = True
            break

        m = int(input())
        if m == -1: break
        if m == 0:
            pos = list(map(int, input().split()))
            pos = screenToPos(pos[0], pos[1])
            flips = getFlips(pos[0], pos[1], 1 if whiteTurn else 2)
            board[pos] = 1 if whiteTurn else 2
            flipAll(flips)

            whiteTurn = not whiteTurn
        else:
            gameOver = False
            for _ in range(m):
                moves = validMoves()
                if not moves:
                    # game is over!
                    gameOver = True
                    printBoard()
                    break

                bestMove = moves[0]
                moveScore = float("-inf")
                c = 1 if whiteTurn else 2
                other = 2 if whiteTurn else 1
                for move in moves:
                    f = getFlips(move[0], move[1], c)
                    flipAll(f)
                    board[move] = c

                    # now get best move for other player
                    nextScore = 0
                    otherMoves = validMoves()
                    for mo in otherMoves:
                        f2 = getFlips(mo[0], mo[1], other)
                        if len(f2) > nextScore:
                            nextScore = len(f2)

                    # undo flips
                    flipAll(f)
                    board[move] = 0

                    s = len(f) - nextScore

                    if s >= moveScore:
                        bestMove = move
                        moveScore = s

                moveFlips = getFlips(bestMove[0], bestMove[1], c)
                board[bestMove] = c
                flipAll(moveFlips)

                whiteTurn = not whiteTurn

            if gameOver: break

        printBoard()


    moves = validMoves()
    if not moves:
        # game is over!
        displayWinner()


strategy2()

"""
b) 19. Shown below

*...*...
.0..0..*
..0.0.0.
...000..
*000X00*
...000..
..0.0.0.
.*..*..*

c) There is a strategy: If white plays on a square next to a corner, then black can take the next move. As the square is
in the corner, it cannot be taken by white. If white avoids playing on squares next to corners and so does black, then 
the game includes a board where the only squares remaining are the corners and the squares next to the corners. There 
was an even number of squares to start with, meaning an even number of squares have been played, meaning it is white's go.
Therefore, black can force white to play in a square neighbouring the corner, and thus black can ensure that at least one
corner is black at the end of the game. 
"""
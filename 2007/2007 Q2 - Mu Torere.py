board = list(input())
centre = board[0]
board = board[1:]

drawLim = 9999
EMPTY = "E"

def canMove(piece, board, centre):
    posMoves = []
    if centre == piece:
        for i in range(len(board)):
            if board[i] == EMPTY:
                posMoves.append(("c", i))
    for i in range(len(board)):
        if board[i] == piece:
            if board[i-1] == EMPTY: posMoves.append((i, i-1))
            if board[i-len(board)+1] == EMPTY: posMoves.append((i, i-len(board)+1))
    if centre == EMPTY:
        for i in range(len(board)):
            if board[i] == piece:
                if board[i-1] == piece and board[i-len(board)+1] == piece:
                    pass
                else:
                    posMoves.append((i, "c"))

    return posMoves

player1move = True


def playMove():
    global player1move, board, centre
    piece = "O" if player1move else "X"
    otherPiece = "X" if player1move else "O"
    moves = canMove(piece, board, centre)

    if len(moves) == 0:
        return 2 if player1move else 1
    moved = False

    # check if move will make us win
    copy = list(board)
    c = centre
    for m in moves:
        copy = list(board)
        c = centre
        if m[0] == "c":
            c = EMPTY
            copy[m[1]] = piece
        elif m[1] == "c":
            c = piece
            copy[m[0]] = EMPTY
        else:
            copy[m[0]] = EMPTY
            copy[m[1]] = piece
        if len(canMove(otherPiece, copy, c)) == 0:
            moved = True
            break
    if moved:
        board = list(copy)
        centre = c
        return 1 if player1move else 2

    # stop moves which will make us lose
    toRemove = []
    copy = list(board)
    c = centre
    for m in moves:
        copy = list(board)
        c = centre
        if m[0] == "c":
            c = EMPTY
            copy[m[1]] = piece
        elif m[1] == "c":
            c = piece
            copy[m[0]] = EMPTY
        else:
            copy[m[0]] = EMPTY
            copy[m[1]] = piece
        for m2 in canMove(otherPiece, list(copy), c):
            copy2 = list(copy.copy())
            c2 = c
            if m2[0] == "c":
                c2 = EMPTY
                copy2[m2[1]] = otherPiece
            elif m2[1] == "c":
                c2 = piece
                copy2[m2[0]] = EMPTY
            else:
                copy2[m2[0]] = EMPTY
                copy2[m2[1]] = otherPiece
            if len(canMove(piece, copy2, c2)) == 0:
                toRemove.append(m)
    for item in toRemove:
        moves.remove(item)

    if len(moves) == 0:
        moves = canMove(piece, board, centre)

    # do the left hand most move
    m = moves[0]
    if m[0] == "c":
        centre = EMPTY
        board[m[1]] = piece
    elif m[1] == "c":
        centre = piece
        board[m[0]] = EMPTY
    else:
        board[m[0]] = EMPTY
        board[m[1]] = piece

    return 0

def draw():
    print(centre, end="")
    print("".join(board))

win = 0
counter = 0
while True:
    q = input()
    if q == "n":
        win = playMove()
        if win > 0: break
        player1move = not player1move
    else:
        while True:
            win = playMove()
            if win > 0: break
            player1move = not player1move
            counter += 1
            if counter > drawLim: break
        break
    draw()
if win > 0: draw()
if win == 1: print("Player 1 wins")
elif win == 2: print("Player 2 wins")
else: print("Draw")

"""
b) 
XOEXXXOOO
XOOXXXOOE
strategy gives XOOXXXOOE, else player 1 would lose

c) No. If a player has a piece in the centre they will always be able to move. For a position to be losing there must be
a piece in the centre. If neither player has a piece in the centre, then they will both have at least one piece adjacent
to one of the other player's pieces and so will be able to move that piece into the centre.

d) 46? Why not 48?
Layouts where centre is empty: 8
Layouts where X is in centre: 19? Why not 20?
Layouts where O is in centre: 19? Why not 20?
"""
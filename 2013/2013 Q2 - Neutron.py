import time

neutron = (2,2)
player1 = {i:(i, 4) for i in range(5)}
player2 = {i:(i, 0) for i in range(5)}

order1 = [int(i)-1 for i in input().split()]
order2 = [int(i)-1 for i in input().split()]

start = time.time()

border = []
for i in range(-1, 6):
    border.append((i, -1))
    border.append((i, 5))
    border.append((5, i))
    border.append((-1, i))

def draw():
    for y in range(5):
        for x in range(5):
            if (x,y) == neutron:
                print("*", end="")
            elif (x,y) in player1.values():
                print("F", end="")
            elif (x,y) in player2.values():
                print("S", end="")
            else:
                print(".", end="")
        print()
    print()

def canMove(piece, dir):
    moves = [(0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0), (-1,-1)]
    dir = moves[dir]
    piece = (piece[0] + dir[0], piece[1] + dir[1])
    if piece == neutron or piece in player1.values() or piece in player2.values() or piece in border:
        return False
    while True:
        piece = (piece[0] + dir[0], piece[1] + dir[1])
        if piece == neutron or piece in player1.values() or piece in player2.values() or piece in border:
            return (piece[0] - dir[0], piece[1] - dir[1])

def canMoveAtAll(piece):
    for dir in range(7):
        m = canMove(piece, dir)
        if m: return m
    return False

def moveNeutron(p1, piece):
    # return the player number of the winner
    global neutron
    if p1:
        for move in [3,4,5]:
            m = canMove(neutron, move)
            if m and m[1] == 4:
                neutron = m
                return 1
        for move in [0,1,2,3,4,5,6,7]:
            m = canMove(neutron, move)
            if m and m[1] != 0:
                n = neutron
                neutron = m
                # need to check that we will still be able to move our piece
                if canMoveAtAll(player1[piece]):
                    return False
                neutron = n
        for move in [0,1,7]:
            if canMove(neutron, move):
                neutron = canMove(neutron, move)
                return 2

    else:
        # try to win
        for move in [0,1,7]:
            m = canMove(neutron, move)
            if m and m[1] == 0:
                neutron = m
                return 2
        # move if other player doesn't win
        for move in [0,1,2,3,4,5,6,7]:
            m = canMove(neutron, move)
            if m and m[1] != 4:
                n = neutron
                neutron = m
                # need to check that we will still be able to move our piece
                if canMoveAtAll(player2[piece]):
                    return False
                neutron = n
        # move to make other player win
        for move in [3,4,5]:
            if canMove(neutron, move):
                neutron = canMove(neutron, move)
                return 1

    for move in range(7):
        if canMove(neutron, move):
            neutron = canMove(neutron, move)
            return False
    return 2 if p1 else 1

def movePiece(p1, n):
    # return true if successful move
    if p1:
        for move in range(7):
            m = canMove(player1[n], move)
            if m:
                player1[n] = m
                return True
    else:
        for move in range(7):
            m = canMove(player2[n], move)
            if m:
                player2[n] = m
                return True
    return False


turn = 0
print(order1, order1[turn % 5])
always = False
while True:
    # player 1 move
    winner = moveNeutron(True, order1[turn % 5])
    if winner: break
    movePiece(True, order1[turn % 5])

    if turn == 0 or always: draw()

    # player 2 move
    winner = moveNeutron(False, order2[turn % 5])
    if winner: break
    movePiece(False, order2[turn % 5])

    if turn == 0 or always: draw()

    turn += 1

draw()

print("Time:", time.time() - start)

"""
b) 65
The neutron can be moved in 6 directions. 
UP = 1 move as we will win
RIGHT = 15 moves
DOWN = 15 moves
DOWNLEFT = 1 move as we will lose
LEFT = 16 moves
UPLEFT = 17 moves
1 + 15 + 15 + 1 + 16 + 17 = 65

c) 
"""
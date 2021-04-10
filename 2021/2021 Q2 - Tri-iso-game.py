from _collections import defaultdict, deque
import time

board = dict()
board[(0,0)] = -1

def nextPos(pos):
    up = abs(pos[1]) % 2 == 0
    if up:
        # on an up triangle
        if pos[2] == 0:
            # left
            if (pos[0]-1, pos[1]+2) in board:
                return (pos[0]-1, pos[1]+2, 2)
            elif (pos[0]-1, pos[1]+3) in board:
                return (pos[0]-1, pos[1]+3, 0)
            if   (pos[0], pos[1] + 2) in board:
                return (pos[0], pos[1] + 2, 0)
            elif (pos[0], pos[1] + 1) in board:
                return (pos[0], pos[1] + 1, 1)
            else:
                return (pos[0], pos[1], 1)
        elif pos[2] == 1:
            # right
            if (pos[0] + 1, pos[1]) in board:
                return (pos[0] + 1, pos[1], 0)
            elif (pos[0] + 1, pos[1] - 1) in board:
                return (pos[0] + 1, pos[1] - 1, 1)
            if   (pos[0] + 1, pos[1] - 2) in board:
                return (pos[0] + 1, pos[1] - 2, 1)
            elif (pos[0], pos[1] - 1) in board:
                return (pos[0], pos[1] - 1, 2)
            else:
                return (pos[0], pos[1], 2)
        else:
            # down
            if (pos[0], pos[1] - 2) in board:
                return (pos[0], pos[1] - 2, 1)
            elif (pos[0] - 1, pos[1] - 1 ) in board:
                return (pos[0] - 1, pos[1] - 1, 2)
            if   (pos[0] - 1, pos[1]) in board:
                return (pos[0] - 1, pos[1], 2)
            elif (pos[0] - 1, pos[1] + 1) in board:
                return (pos[0] - 1, pos[1] + 1, 0)
            else:
                return (pos[0], pos[1], 0)
    else:
        # on a down triangle
        if pos[2] == 0:
            # left
            if (pos[0] - 1, pos[1]) in board:
                return (pos[0] - 1, pos[1], 2)
            elif (pos[0] - 1, pos[1] + 1) in board:
                return (pos[0] - 1, pos[1] + 1, 2)
            if   (pos[0] - 1, pos[1] + 2) in board:
                return (pos[0] - 1, pos[1] + 2, 0)
            elif (pos[0], pos[1] + 1) in board:
                return (pos[0], pos[1] + 1, 0)
            else:
                return (pos[0], pos[1], 1)

        elif pos[2] == 1:
            # up
            if (pos[0], pos[1] + 2) in board:
                return (pos[0], pos[1] + 2, 0)
            elif (pos[0] + 1, pos[1] + 1) in board:
                return (pos[0] + 1, pos[1] + 1, 0)
            if   (pos[0] + 1, pos[1]) in board:
                return (pos[0] + 1, pos[1], 1)
            elif (pos[0] + 1, pos[1] - 1) in board:
                return (pos[0] + 1, pos[1] - 1, 1)
            else:
                return (pos[0], pos[1], 2)
        else:
            # right
            if (pos[0] + 1, pos[1] - 2) in board:
                return (pos[0] + 1, pos[1] - 2, 1)
            elif (pos[0] + 1, pos[1] - 3) in board:
                return (pos[0] + 1, pos[1] - 3, 1)
            if   (pos[0], pos[1] - 2) in board:
                return (pos[0], pos[1] - 2, 2)
            elif (pos[0], pos[1] - 1) in board:
                return (pos[0], pos[1] - 1, 2)
            else:
                return (pos[0], pos[1], 0)

# returns the number of points scored
def canWin(pos, v):
    up = abs(pos[1]) % 2 == 0
    score = 0
    if up:
        # top?
        if (pos[0], pos[1] - 2) in board and board[(pos[0], pos[1] - 2)] == v:
            if (pos[0] + 1, pos[1] - 2) in board and board[(pos[0] + 1, pos[1] - 2)] == v: score += 1
        # bot left?
        if (pos[0], pos[1] + 2) in board and board[(pos[0], pos[1] + 2)] == v:
            if (pos[0] + 1, pos[1]) in board and board[(pos[0] + 1, pos[1])] == v: score += 1
        #bot right?
        if (pos[0] - 1, pos[1] + 2) in board and board[(pos[0] - 1, pos[1] + 2)] == v:
            if (pos[0] - 1, pos[1]) in board and board[(pos[0] - 1, pos[1])] == v: score += 1
    else:
        # bot?
        if (pos[0], pos[1] + 2) in board and board[(pos[0], pos[1] + 2)] == v:
            if (pos[0] - 1, pos[1] + 2) in board and board[(pos[0] - 1, pos[1] + 2)] == v: score += 1
        # top left?
        if (pos[0] + 1, pos[1]) in board and board[(pos[0] + 1, pos[1])] == v:
            if (pos[0] + 1, pos[1] - 2) in board and board[(pos[0] + 1, pos[1] - 2)] == v: score += 1
        # top right?
        if (pos[0] - 1, pos[1]) in board and board[(pos[0] - 1, pos[1])] == v:
            if (pos[0], pos[1] - 2) in board and board[(pos[0], pos[1] - 2)] == v: score += 1
    return score


def fill(pos,v):
#    print(pos)
    if (pos[0], pos[1]) not in board:
        board[(pos[0], pos[1])] = v
        return
    up = abs(pos[1]) % 2 == 0
    if up:
        # on an up triangle
        if pos[2] == 0:
            # left
            if not (pos[0] - 1, pos[1] + 1) in board:
                board[(pos[0] - 1, pos[1] + 1)] = v
        if pos[2] == 1:
            # right
            if not (pos[0], pos[1] + 1) in board:
                board[ (pos[0], pos[1] + 1)] = v
        if pos[2] == 2:
            # down
            if not (pos[0], pos[1] - 1) in board:
                board[(pos[0], pos[1] - 1) ] = v
    else:
        # on a down triangle
        if pos[2] == 0:
            # left
            if not (pos[0], pos[1] - 1) in board:
                board[(pos[0], pos[1] - 1)] = v
        if pos[2] == 1:
            # up
            if not (pos[0], pos[1] + 1) in board:
                board[(pos[0], pos[1] + 1)] = v
        if pos[2] == 2:
            # right
            if not (pos[0] + 1, pos[1] - 1) in board:
                board[ (pos[0] + 1, pos[1] - 1)] = v

def getAdj(pos):
    up = abs(pos[1]) % 2 == 0
    if up:
        # on an up triangle
        if pos[2] == 0:
            # left
            return  (pos[0] - 1, pos[1] + 1)
        if pos[2] == 1:
            # right
            return (pos[0], pos[1] + 1)
        if pos[2] == 2:
            # down
            return (pos[0], pos[1] - 1)
    else:
        # on a down triangle
        if pos[2] == 0:
            # left
            return (pos[0], pos[1] - 1)
        if pos[2] == 1:
            # up
            return (pos[0], pos[1] + 1)
        if pos[2] == 2:
            # right
            return (pos[0] + 1, pos[1] - 1)


def perimeter(pos):
    seen = {pos}
    while True:
        pos = nextPos(pos)
        if pos in seen:
#            print(seen)
            return len(seen)
        seen.add(pos)

def holes(pos):
    # generate perimeter
    perim = {pos}
    seen = set()
    while True:
        pos = nextPos(pos)
        if pos in perim:
            break
        perim.add(pos)

    for edge in perim:
        seen.add((edge[0], edge[1]))
    h = 0
    pos = (0, 0)
    pending = deque([pos])
    moves = [[(0,1), (0,-1), (1, -1)], [(0,1), (0,-1), (-1, 1)]]

    while pending:
        look = pending.popleft()

        if not look in board: h += 1
        up = abs(look[1]) % 2 == 0

        for m in moves[up]:
            npos = (m[0] + look[0], m[1] + look[1])
            if not npos in seen:
                seen.add(npos)
                pending.append(npos)

    return h



def adj(pos):
    if board[(pos[0], pos[1])] == 0: return True
    up = abs(pos[1]) % 2 == 0
    if up:
        # on an up triangle
        if pos[2] == 0:
            # left
            return not (pos[0] - 1, pos[1] + 1) in board
        if pos[2] == 1:
            # right
            return not (pos[0], pos[1] + 1) in board
        if pos[2] == 2:
            # down
            return not (pos[0], pos[1] - 1) in board
    else:
        # on a down triangle
        if pos[2] == 0:
            # left
            return not (pos[0], pos[1] - 1) in board
        if pos[2] == 1:
            # up
            return not (pos[0], pos[1] + 1) in board
        if pos[2] == 2:
            # right
            return not (pos[0] + 1, pos[1] - 1) in board
    return False

def repos():
    a = board.keys()
#    print(a)
    b = []
    for c in a:
        if c[1] % 2 == 0:
            b.append((-c[1], c[0]))
        else:
            b.append((-(c[1]-1), c[0]+0.5))

    y,x = sorted(b)[0]
    if int(x) != x:
        return (int(x - 0.5), (-y) + 1, 0)
    else:
        return (x,-y,0)


pos = [(0, 0, 0)]


def q2(p, m, tra):
    global board, pos
    pos = [(0, 0, 0) for _ in range(p)]
    board = dict()
    board[(0, 0)] = -1
    score = [0 for _ in range(p)]
    moves = 0
    while True:
        for player in range(p):
            if moves >= m: break
            moves += 1
            ori = (pos[player][0], pos[player][1], pos[player][2])
            # move
            for i in range(tra[player]):
                pos[player] = nextPos(pos[player])
                if (pos[player][0], pos[player][1]) not in board:
                    if canWin((pos[player][0], pos[player[1]]), player + 1):
                        break
                else:
                    if adj(pos[player]):
                        if canWin(getAdj(pos[player]), player + 1): break
    #            print(pos[player])
    #        print()

            # fill in
            fill(ori, player + 1)
            # see if scored
            sc = canWin(getAdj(ori), player+1)
            if sc: score[player] += sc

    #        print(board, ori, player)
            # reposition players
            for pl in range(p):
                if not adj(pos[pl]):
                    pos[pl] = repos()
    #                print("move", pos[pl])

        if moves >= m: break
    return score

p, m = list(map(int, input().split()))
tra = list(map(int, input().split()))

start = time.time()

score = q2(p, m, tra)
#print(board)
#print(score)
for i in score:
    print(i)
#    print(len(i))
print(perimeter(repos()))
print(time.time() - start)

# part c
# val = 2 5000, 5 7
#print(holes(repos()))
# ans : 377
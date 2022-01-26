from _collections import defaultdict, deque
import time

board = dict()
board[(0,0)] = -1
scores = []

def next_pos(pos):
    # are we on an upwards facing tile?
    up = abs(pos[1]) % 2 == 0

    if up:
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
def can_win(pos, player):
    # is this an upwards pointing triangle?
    up = (abs(pos[1]) % 2 == 0)
    score = 0

    if up:
        # top tile?
        if (pos[0], pos[1] - 2) in board and board[(pos[0], pos[1] - 2)] == player:
            if (pos[0] + 1, pos[1] - 2) in board and board[(pos[0] + 1, pos[1] - 2)] == player:
                score += 1
        # bottom left tile?
        if (pos[0], pos[1] + 2) in board and board[(pos[0], pos[1] + 2)] == player:
            if (pos[0] + 1, pos[1]) in board and board[(pos[0] + 1, pos[1])] == player:
                score += 1
        # bottom right tile?
        if (pos[0] - 1, pos[1] + 2) in board and board[(pos[0] - 1, pos[1] + 2)] == player:
            if (pos[0] - 1, pos[1]) in board and board[(pos[0] - 1, pos[1])] == player:
                score += 1

    else:
        # bottom tile?
        if (pos[0], pos[1] + 2) in board and board[(pos[0], pos[1] + 2)] == player:
            if (pos[0] - 1, pos[1] + 2) in board and board[(pos[0] - 1, pos[1] + 2)] == player:
                score += 1
        # top left tile?
        if (pos[0] + 1, pos[1]) in board and board[(pos[0] + 1, pos[1])] == player:
            if (pos[0] + 1, pos[1] - 2) in board and board[(pos[0] + 1, pos[1] - 2)] == player:
                score += 1
        # top right tile?
        if (pos[0] - 1, pos[1]) in board and board[(pos[0] - 1, pos[1])] == player:
            if (pos[0], pos[1] - 2) in board and board[(pos[0], pos[1] - 2)] == player:
                score += 1

    return score


def fill(pos, player):
    # is this the unclaimed tile?
    if (pos[0], pos[1]) not in board:
        board[(pos[0], pos[1])] = player
        scores[player - 1] += can_win((pos[0], pos[1]), player)
        return

    # else claim the adjacent tile
    pos = get_adj(pos)
    if pos not in board:
        scores[player - 1] += can_win(pos, player)
        board[pos] = player

def get_adj(pos):
    # is this an upwards facing tile?
    up = abs(pos[1]) % 2 == 0

    if up:
        if pos[2] == 0:
            # left edge
            return  (pos[0] - 1, pos[1] + 1)
        if pos[2] == 1:
            # right edge
            return (pos[0], pos[1] + 1)
        if pos[2] == 2:
            # down edge
            return (pos[0], pos[1] - 1)

    else:
        # on a down triangle
        if pos[2] == 0:
            # left edge
            return (pos[0], pos[1] - 1)
        if pos[2] == 1:
            # up edge
            return (pos[0], pos[1] + 1)
        if pos[2] == 2:
            # right edge
            return (pos[0] + 1, pos[1] - 1)


def count_perimeter(pos):
    seen = {pos}
    while True:
        pos = next_pos(pos)
        if pos in seen:
#            print(seen)
            return len(seen)
        seen.add(pos)

def holes(pos):
    # generate perimeter
    perim = {pos}
    seen = set()
    while True:
        pos = next_pos(pos)
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

def reposition():
    tiles = board.keys()
#    print("r!")

    claimed_tiles = []
    for c in tiles:
        if c[1] % 2 == 0:
            claimed_tiles.append((-c[1], c[0]))
        else:
            claimed_tiles.append((-(c[1]-1), c[0]+0.5))

    y, x = min(claimed_tiles)

    if int(x) != x:
        return (int(x - 0.5), (-y) + 1, 0)
    else:
        return (x, -y, 0)


positions = [(0, 0, 0)]

# player is the number of the player that is moving
# position is a 3D point giving its current position
# max_traversals is the maximum number of traversals it can make
def move(player, position, max_traversals):
    # process each step one at a time
    for _ in range(max_traversals):
        position = next_pos(position)
        # has this tile already been filled in?
        if (position[0], position[1]) not in board:
            # helper function. will filling in this tile score a point?
            if can_win((position[0], position[1]), player + 1):
                break
        # remember, we are on an edge that connects 2 triangles.
        # is the other tile filled in?
        # helper function, gets the tile position is adjacent to
        elif get_adj(position) not in board:
            # helper function. will filling in this tile score a point?
            if can_win(get_adj(position), player + 1):
                break

    return position

def q2(p, m, max_traversals):
    global board, positions, scores
    # initialise player positions
    positions = [(0, 0, 0) for _ in range(p)]
    board = dict()
    # the starting tile belongs to no player
    board[(0, 0)] = -1
    # initialise player scores
    scores = [0 for _ in range(p)]
    moves = 0

    while True:
        for player in range(p):
            if moves >= m: break
            moves += 1
            starting_position = (positions[player][0], positions[player][1], positions[player][2])
            # move
            positions[player] = move(player, positions[player], max_traversals[player])

            # fill in tile
            fill(starting_position, player + 1)

            # reposition players
            for player in range(p):
                if get_adj(positions[player]) in board:
                    positions[player] = reposition()

        if moves >= m: break


    return scores

p, m = list(map(int, input().split()))
max_traversals = list(map(int, input().split()))

start = time.time()

q2(p, m, max_traversals)
#print(board)
#print(score)
for i in scores:
    print(i)
#    print(len(i))
print(count_perimeter(reposition()))
print("Time taken:", time.time() - start)

# part c
# val = 2 5000, 5 7
#print(holes(reposition()))
# ans : 377
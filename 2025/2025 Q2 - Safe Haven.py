from _collections import deque

n, r, g = list(map(int, input().split()))

grid = [["." for _ in range(n)] for _ in range(n)]

def coord(i):
    return (i%n, i//n)

def output():
    global grid
    for y in range(n):
        print("".join(grid[y]))

def fill_grid():
    global r, g, grid
    # FILL GRID
    i = 0
    free_cells = deque([i for i in range(1,n*n)])
    grid[0][0] = "R"
    for j in range(n*n-1):
        if j % 2:
            # red's go
            free_cells.rotate(-(r-1))
            pos = coord(free_cells.popleft())
            grid[pos[1]][pos[0]] = "R"
        else:
            # green's go
            free_cells.rotate(-(g-1))
            pos = coord(free_cells.popleft())
            grid[pos[1]][pos[0]] = "G"
#        output()
#        print(free_cells)
#        print()

def in_grid(u):
    if u[0] < 0 or u[1] < 0 or u[0] >= n or u[1] >= n: return False
    return True

def bfs(u):
    seen = set()
    q = deque()
    q.append(u)
    seen.add(u)
    green = 0
    red = 0
    haven = []
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    while q:
        u = q.popleft()
        if grid[u[1]][u[0]] == "R": red += 1
        elif grid[u[1]][u[0]] == "G": green += 1
        haven.append(u)
        for d in directions:
            v = (u[0] + d[0], u[1] + d[1])
            if v not in seen and in_grid(v) and grid[v[1]][v[0]] != ".":
                seen.add(v)
                q.append(v)
    return haven, red, green

def get_havens():
    global grid
    seen = set()
    havens = []
    for y in range(n):
        for x in range(n):
            if (x,y) not in seen and grid[y][x] != ".":
                # bfs from here
                haven = bfs((x,y))
                for item in haven[0]:
                    seen.add(item)
                havens.append(haven)
    return havens

def score(havens):
    score_r = 0
    score_g = 0
    for h, red, green in havens:
        if red == 0: score_g += 1
        if green == 0: score_r += 1

    return score_r, score_g

def from_coord(coord):
    x,y = coord
    return y*n+x

def max_pos(positions):
    m = 0
    for p in positions:
        m = max(m, from_coord(p))
    return m

def choose_haven(havens, player):
    options = []
    for i in range(len(havens)):
        if havens[i][1] != 0 and havens[i][2] != 0:
            # unsafe
            if player == 0: # red
                options.append((havens[i][2], -havens[i][1], -max_pos(havens[i][0]), havens[i][0]))
            else: # green
                options.append((havens[i][1], -havens[i][2], -max_pos(havens[i][0]), havens[i][0]))
    if len(options) == 0: return False # game has ended
    options = sorted(options)
    return options[0][-1]

def move(haven, player):
    # find lowest square that neighbours two
    opponent = "GR"[player]
    player = "RG"[player]
    directions = [(0,-1), (-1,0), (1,0), (0,1)]
    for i in range(n*n):
        u = coord(i)
        if u in haven and grid[u[1]][u[0]] == player:
            for d in directions:
                v = (d[0] + u[0], d[1] + u[1])
                if in_grid(v) and grid[v[1]][v[0]] == opponent:
                    # make move here
                    grid[u[1]][u[0]] = "." # relinquish control
                    grid[v[1]][v[0]] = player # gain control
                    return

def makes_safe_haven(u, v):
    old_u = grid[u[1]][u[0]]
    old_v = grid[v[1]][v[0]]
    # update
    grid[v[1]][v[0]] = grid[u[1]][u[0]]
    grid[u[1]][u[0]] = "."
    # is safe haven?
    haven = bfs(v)
    safe_haven = False
    if haven[1] == 0 or haven[2] == 0: safe_haven = True # created new safe haven!
    # reset grid
    grid[v[1]][v[0]] = old_v
    grid[u[1]][u[0]] = old_u
    return safe_haven

def move2(player):
    p_num = player
    opponent = "GR"[player]
    player = "RG"[player]
    directions = [(0,-1), (-1,0), (1,0), (0,1)]

    # prioritise making a move that will create a safe haven
    for i in range(n*n):
        u = coord(i)
        if grid[u[1]][u[0]] == player:
            for d in directions:
                v = (d[0] + u[0], d[1] + u[1])
                if in_grid(v) and grid[v[1]][v[0]] == opponent:
                    # make move here
                    if makes_safe_haven(u, v):
                        grid[u[1]][u[0]] = "." # relinquish control
                        grid[v[1]][v[0]] = player # gain control
                        return True
    return False

def run():
    fill_grid()
    output()
    player = 0
    while True:
        havens = get_havens()
#        print(havens)
        haven = choose_haven(havens, player)
        if not haven: # game has ended
            red, green = score(havens)
            print(red, green)
            return
        move(haven, player)
#        output()
#        print()
        # switch player
        player += 1
        player %= 2

def run2():
    fill_grid()
    output()
    player = 0
    while True:
        if not move2(player):
            havens = get_havens()
            #        print(havens)
            haven = choose_haven(havens, player)
            if not haven:  # game has ended
                red, green = score(havens)
                print(red, green)
                return
            move(haven, player)
        #        output()
        #        print()
        # switch player
        player += 1
        player %= 2


run()
output()

def c():
    global r, g, grid
    ans = [list("RGRG"), list("GRGR"), list("RGRG"), list("GRGR")]
    for r in range(1, 50):
        for g in range(1, 50):
            grid = [["." for _ in range(n)] for _ in range(n)]
            fill_grid()
            if ans == grid:
                output()
                print("r:", r, "g:", g)
                return

#c()

"""
b)
.R.
...
.R.

c) r = 25, g = 41

d) red = 10, green = 9
"""
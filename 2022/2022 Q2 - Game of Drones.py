from time import *

edges = [[0 for _ in range(25)] for _ in range(25)]

def control(hex, debug=False):
    r = 0
    b = 0
    for i in range(6):
        if edges[hex][i] > 0:
            r += 1
            if debug:
                print("red e", i+1, hex+1)
        elif edges[hex][i] < 0:
            b += 1
            if debug:
                print("blue e", i+1, hex+1)

    if r == b: return 0
    if r > b: return 1
    return -1

def opposite(edge):
    return (edge + 3) % 6

def own(v, hex, edge):
    switched = False
    if edges[hex][edge] not in [v, 0]: switched = True
    edges[hex][edge] = v
    h = hex
    hex += 1
    e = opposite(edge)
    row = h // 5
    x, y = 0, 0
    if row % 2 == 1:
        y = 1
        x = 0
    else:
        y = 0
        x = 1
    # capture other side of edge
    newhex = -1
    if edge == 0 and hex > 5 and (hex % 5 > 0 or row % 2 == 0):
        newhex = h-4-x
    if edge == 1 and hex % 5 > 0:
        newhex = h+1
    if edge == 2 and hex < 21 and (hex % 5 > 0 or row % 2 == 0):
        newhex = h+5+y
    if edge == 3 and hex < 21 and (hex % 5 != 1 or row % 2 == 1):
        newhex = h+4+y
    if edge == 4 and hex % 5 != 1:
        newhex = h-1
    if edge == 5 and hex > 5 and (hex % 5 != 1 or row % 2 == 1):
        newhex = h-5-x

    if newhex != -1:
        if edges[newhex][edge] not in [v, 0]: switched = True
        edges[newhex][e] = v

    return switched

r, b = list(map(int, input().split()))
s, f = list(map(int, input().split()))

start = time()

# set up game state
def reset():
    global edges, rpos, bpos, redge, bedge
    rpos = 0
    bpos = 24
    redge = 0
    bedge = 5
    edges = [[0 for _ in range(25)] for _ in range(25)]


reset()

def skirmish():
    global rpos, bpos, redge, bedge, r, b
    #red
    switch = own(1, rpos, redge)
    redge += 1
    redge %= 6
    rpos += r
    rpos %= 25
    # blue
    s = own(-1, bpos, bedge)
    switch = switch or s
    bedge -= 1
    if bedge < 0: bedge += 6
    bpos += b
    bpos %= 25

    return switch

def score(debug = False):
    rown, bown = 0, 0
    for hex in range(25):
        c = control(hex, debug)
        if c == 1:
            rown += 1
            if debug:
                print(hex+1, "red")
        elif c == -1:
            bown += 1
            if debug:
                print(hex+1, "blue")
    return rown, bown

def feud():
    # red
    e = []
    rscore, bscore = score()
    for hex in range(25):
        for edge in range(6):
            if edges[hex][edge] != 0: continue
            own(1, hex, edge)
            nr, nb = score()
            con = nr - rscore
            uncon = bscore - nb
            # disown edge
            own(0, hex, edge)
            e.append((con, uncon, -hex, -edge))
    e = sorted(e)
    if len(e) > 0:
        hex, edge = -e[-1][2], -e[-1][3]
        own(1, hex, edge)

    # blue
    e = []
    rscore, bscore = score()
    for hex in range(25):
        for edge in range(6):
            if edges[hex][edge] != 0: continue
            own(-1, hex, edge)
            nr, nb = score()
            con = nb - bscore
            uncon = rscore - nr
            # disown edge
            own(0, hex, edge)
            e.append((con, uncon, hex, edge))
    e = sorted(e)
    if len(e) > 0:
        hex, edge = e[-1][2], e[-1][3]
        own(-1, hex, edge)

for i in range(s):
    skirmish()

for i in range(f):
    feud()

rown, bown = score()

print(rown)
print(bown)

#print(time() - start)

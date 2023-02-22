
# define pentomino as 4x4 char matrix

F = [".##.",
     "##..",
     ".#..",
     "...."]
I = [".#..",
     ".#..",
     ".#..",
     ".#..",
     ".#.."]
L = [".#..",
     ".#..",
     ".#..",
     ".##."]
N = ["..#.",
     ".##.",
     ".#..",
     ".#.."]
P = ["##..",
     "##..",
     "#...",
     "...."]
T = ["###.",
     ".#..",
     ".#..",
     "...."]
U = ["#.#.",
     "###.",
     "....",
     "...."]
V = ["#...",
     "#...",
     "###.",
     "...."]
W = ["#...",
     "##..",
     ".##.",
     "...."]
X = [".#..",
     "###.",
     ".#..",
     "...."]
Z = ["##..",
     ".#..",
     ".##.",
     "...."]
Y = [".#..",
     "##..",
     ".#..",
     ".#.."]


# flip pentomino through Y axis
def flip(pentomino):
    return [pentomino[i][::-1] for i in range(len(pentomino))]


pentominoes = {"F": F, "G": flip(F), "I": I, "J": flip(L), "L": L, "N": N, "M": flip(N), "P": P, "Q": flip(P),
               "T": T, "U": U, "V": V, "W": W, "X": X, "Z": Z, "S": flip(Z), "Y": Y, "A": flip(Y)}


# output pentomino
def output(pentomino):
    print()
    for line in pentomino:
        print("".join(line))


# returns the overlap of two points
def overlap(p1, p2, q1, q2, x, y):
    q1 = ()


# combine pentominoes
# combination is achieved by placing p1
def combine(p1, p2, q1, q2):
    x = len(p1[0]) + len(p2[0])
    y = len(p1) + len(p2)
    combination = [["." for _ in range(x)] for _ in range(y)]

    for Y in range(len(p1)):
        for X in range(len(p1[0])):
            if p1[Y][X] == "#":
                combination[Y + q1[1]][X + q1[0]] = "#"
    for Y in range(len(p2)):
        for X in range(len(p2[0])):
            if p2[Y][X] == "#":
                combination[Y + q2[1]][X + q2[0]] = "#"

    for i in range(y):
        combination[i] = "".join((combination[i]))

    return combination


# is a combination valid?
def valid(combination, exp=10):
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    filled = 0
    loc = (0, 0)
    for y in range(len(combination)):
        for x in range(len(combination[0])):
            if (combination[y][x] == "#"):
                filled += 1
                loc = (x,y)
    # incorrect number of tiles
    if filled != exp: return False

    # check if connected
    seen = {loc}
    q = [loc]
    visited = 1
    while q:
        curr = q.pop()
        for d in directions:
            next_loc = (curr[0] + d[0], curr[1] + d[1])
            if next_loc[0] < 0 or next_loc[0] >= len(combination[0]) or next_loc[1] < 0 or next_loc[1] >= len(combination):
                continue
            if combination[next_loc[1]][next_loc[0]] == "#":
                if next_loc not in seen:
                    seen.add(next_loc)
                    q.append(next_loc)
                    visited += 1
    return visited == filled


# trim excess space around a combination
def trim(combination):
    new_combination = []
    # remove blank lines
    for line in combination:
        if "#" in line:
            new_combination.append(line)
    # rotate 90*
    combination = list(zip(*new_combination[::-1]))
    new_combination = []
    for line in combination:
        if "#" in line:
            new_combination.append(line)
    # rotate 270*
    for i in range(3):
        new_combination = list(zip(*new_combination[::-1]))

    return new_combination


# count the number of valid combinations of 2 pentominoes
def count_combinations(p1, p2, exp=10):
    ans = []
    for x1 in range(len(p1[0])+1):
        for x2 in range(len(p2[0])+1):
            for y1 in range(len(p1)+1):
                for y2 in range(len(p2)+1):
                    try:
                        combination = combine(p1, p2, (x2, y2), (x1, y1))
                        if valid(combination, exp):
                            combination = trim(combination)
                            if combination not in ans:
                                combination = trim(combination)
#                                output(combination)
                                ans.append(combination)
                    except:
                        pass
    return ans


comb = input()
a = pentominoes[comb[0]]
b = pentominoes[comb[1]]
output(a)
output(b)
print(len(count_combinations(a, b)))

"""
b) 
ANS: only 1
..#.
####
###.
.##.
made from QA


# get XW all combinations
P = "FGILJNMPQTUVZSYA"
xw_combinations = count_combinations(X, W)
for c in xw_combinations:
    output(c)

# get all other combinations
all_combinations = []
for p1 in P:
    for p2 in P:
        combs = count_combinations(pentominoes[p1], pentominoes[p2])
        for c in combs:
            if c not in all_combinations:
                all_combinations.append(c)

b = 0
print("XW")
for xw in xw_combinations:
    if xw in all_combinations:
        b += 1
        output(xw)
print("b:", b)
"""

"""
c) 122 for III; 672 for LIV
"""

def part_c():

    all_iii = []
    ii = count_combinations(I, I)

    for comb in ii:
        triplet = count_combinations(comb, I, 15)
        for c in triplet:
            if c not in all_iii:
                all_iii.append(c)

#    for c in all_iii:
#        output(c)

    print("III:", len(all_iii))

    all_liv = []
    li = count_combinations(L, I)
    iv = count_combinations(I, V)
    lv = count_combinations(L, V)

    for comb in li:
        triplet = count_combinations(comb, V, 15)
        for c in triplet:
            if c not in all_liv:
                all_liv.append(c)
    for comb in iv:
        triplet = count_combinations(comb, L, 15)
        for c in triplet:
            if c not in all_liv:
                all_liv.append(c)
    for comb in lv:
        triplet = count_combinations(comb, I, 15)
        for c in triplet:
            if c not in all_liv:
                all_liv.append(c)

    print("LIV:", len(all_liv))

#part_c()


"""
d) 
ANS : 84 combinations
forming 113 unique shapes
"""


def has_hole(combination):

    seen = set()

    def dfs_hole(p):
        moves = [(0,1), (1,0), (-1,0), (0,-1)]
        q = [p]
        hole = True
        while q:
            curr = q.pop()
            for m in moves:
                new = (curr[0] + m[0], curr[1] + m[1])
                # not a hole
                if new[0] < 0 or new[1] < 0 or new[0] >= len(combination[0]) or new[1] >= len(combination):
                    hole = False
                # continue dfs
                elif new not in seen and combination[new[1]][new[0]] == ".":
                    seen.add(new)
                    q.append(new)
        return hole




    for y in range(1, len(combination) - 1):
        for x in range(1, len(combination[y]) - 1):
            if (x,y) not in seen and combination[y][x] == ".":
                seen.add((x,y))
                if dfs_hole((x,y)): return True
    return False

def part_d():

    P = "FGILJNMPQTUVZSYAXW"

    holes = []
    d = 0
    for i in range(len(P)):
        for j in range(i+1):
            combs = count_combinations(pentominoes[P[j]], pentominoes[P[i]])
            holed = False
            for c in combs:
                if has_hole(c):
                    holed = True
#                    output(c)
                    if c not in holes:
                        holes.append(c)
            if holed:
                print(P[i], P[j])
                d += 1

    print("d:", d)
#    print(len(holes))

#part_d()


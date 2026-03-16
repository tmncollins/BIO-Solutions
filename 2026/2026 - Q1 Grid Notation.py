
from itertools import product

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXY'
grid = dict()
inv_grid = dict()

i = 0
for y in range(4, -1, -1):
    for x in range(5):
        grid[ALPHA[i]] = (x,y)
        inv_grid[(x,y)] = ALPHA[i]
        i += 1

#print(grid)
def a(text):
    p = pow(5, len(text)-1)

    x,y=0,0
    for letter in text:
        dx,dy = grid[letter]
        x += dx * p
        y += dy * p
        p /= 5
    x = int(x) + 1
    y = int(y) + 1
    return x, y

text = input().strip().upper()
x, y = a(text)
print(x, y)

def b(x, y, n):
    x -= 1; y -= 1
    p = pow(5, n-1)
    word = ''
    while len(word) < n:
        _x = x // p
        _y = y // p
        word += inv_grid[(_x, _y)]
        x %= p
        y %= p
        p /= 5
    return word


def shared_letters(a, b):
    counter = 0
    for i in a:
        if i in b: counter += 1
    return counter

def c(size):
    # 5 letters
    loc = dict()
    for word in product(ALPHA, repeat=size):
        word = ''.join(word)
        x,y = a(word)
        loc[(x,y)] = word
    print('done')

    adj = [(1,0), (0,1), (-1,0), (0,-1)]

    print(len(loc.keys()))

    counter = 0
    for k in loc.keys():
        x,y = k
        flag = False
        for dx, dy in adj:
            _x = x+dx; _y = y+dy
            if (_x, _y) in loc:
#                print((x, y), (_x, _y), loc[(_x, _y)], loc[(x, y)])
                if shared_letters(loc[(_x,_y)], loc[(x,y)]) == 0:
#                    print((x,y))
                    flag = True
                    break
        if flag: counter += 1
    return counter

print(b(209, 217, 4), b(606445, 9161058, 10))
#print(b(45 , 118, 3))
#for i in range(2,6):
print('c', 5, c(5))

x = 5
y = 19
for dx, dy in [(0,0), (1,0), (0,1), (-1,0), (0,-1)]:
    print(b(x+dx, y+dy, 2))

"""
b) QIGS, AGMSTKGMSO

c) 35176




"""

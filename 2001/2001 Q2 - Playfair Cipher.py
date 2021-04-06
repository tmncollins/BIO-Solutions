left = list(input())
right = list(input())

grid1 = []
alpha = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
for y in range(5):
    line = ""
    for x in range(5):
        letter = "4"
        while letter not in alpha and len(left) > 0:
            letter = left.pop(0)
        if len(left) == 0 and letter == "4":
            letter = alpha.pop(0)
        else:
            alpha.remove(letter)
        line += letter
    grid1.append(line)

grid2 = []
alpha = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
for y in range(5):
    line = ""
    for x in range(5):
        letter = "4"
        while letter not in alpha and len(right) > 0:
            letter = right.pop(0)
        if len(right) == 0 and letter == "4":
            letter = alpha.pop(0)
        else:
            alpha.remove(letter)
        line += letter
    grid2.insert(0, line[::-1])

for i in range(5):
    print(grid1[i], grid2[i])

def findline(grid, letter):
    for i in range(len(grid)):
        if letter in grid[i]: return i

def getNext(grid, letter, n):
    for i in range(len(grid)):
        if letter in grid[i]:
            p = grid[i].index(letter)
            p = (p+n) % len(grid[i])
            return grid[i][p]

def getCol(grid, letter, n):
    i = 0
    for line in grid:
        if letter in line:
            i = line.index(letter)
    return grid[n][i]

inp = ""
while inp != "Q":
    inp = input()
    if inp == "E":
        word = input()
        output = ""
        if len(word) % 2 == 1: word += "X"
        for i in range(0, len(word), 2):
            a = word[i]
            b = word[i+1]
            if findline(grid1, a) == findline(grid2, b):
                output += getNext(grid1, a, 1) + getNext(grid2, b, 1)
            else:
                output += getCol(grid1, a, findline(grid2, b)) + getCol(grid2, b, findline(grid1, a))

        print(output)

    elif inp == "D":
        word = input()
        output = ""
        for i in range(0, len(word), 2):
            a = word[i]
            b = word[i+1]
            if findline(grid1, a) == findline(grid2, b):
                output += getNext(grid1, a, -1) + getNext(grid2, b, -1)
            else:
                output += getCol(grid1, a, findline(grid2, b)) + getCol(grid2, b, findline(grid1, a))
        if output[-1] == "X": output = output[:-1]
        print(output)

"""
b) 9 (there are 2 Fs)
c) Each Row must be preserved in order but can be shifted there are 5 ways to achieve this shift. The rows in both 
squares can be shifted by any amount. The rows can be ordered in 5! ways, however the ordering has to be the same in
both squares
Therefore there are (5*5)*(5!) equivalent squares = 3000 
 
"""

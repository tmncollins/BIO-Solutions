import time
from collections import deque, defaultdict

def add(a,b):
    return tuple([(a[i] + b[i]) % 3 for i in range(len(a))])


basicV = "010001110001"
leftV = "10000110001"
rightV = "000010001100001"

vector = defaultdict(tuple)
def createVectors():
    letters = list("BCDGHILMNQRSVWX")
    lletters = list("AFKPU")
    rletters = list("EJOTY")
    for y in range(5):
        for x in range(3):
            before = y * 5 + x
            after = 25 * "0"
            v = before * "0" + basicV + after
            v = v[5:30]
            vector[letters[y*3 + x]] = tuple(map(int, list(v)))
    for y in range(5):
        before = y * 5
        v = before * "0" + leftV + 25 * "0"
        v = v[5:30]
        vector[lletters[y]] = tuple(map(int, list(v)))
    for y in range(5):
        before = y * 5
        v = before * "0" + rightV + 25 * "0"
        v = v[5:30]
        vector[rletters[y]] = tuple(map(int, list(v)))

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXY")

def boardToVector(word):
    board = [0 for i in range(25)]
    for l in word:
        if l in alpha:
            board[alpha.index(l)] = 2
        else:
            board[alpha.index(l.upper())] = 1
    return tuple(board)

def solve(startV, allPos = False):
    createVectors()
    endV = tuple([0 for i in range(25)])
    solved = False
    allConfig = []
    for a in range(3):
        for b in range(3):
            for c in range(3):
                for d in range(3):
                    for e in range(3):
                        # brute force the top row
#                        print(a,b,c,d,e)
                        board = tuple(startV)
                        for _ in range(a): board = add(vector["A"], board)
                        for _ in range(b): board = add(vector["B"], board)
                        for _ in range(c): board = add(vector["C"], board)
                        for _ in range(d): board = add(vector["D"], board)
                        for _ in range(e): board = add(vector["E"], board)
                        solution = "A" * a + "B" * b + "C" * c + "D" * d + "E" * e
                        # deduce the required moves for the rest of the board
                        for i in range(20):
#                            print(board)
                            if board[i] == 2:
#                                print(alpha[i+5])
                                board = add(vector[alpha[i+5]], board)
                                solution += alpha[i+5]
                            elif board[i] == 1:
                                board = add(vector[alpha[i+5]], add(vector[alpha[i+5]], board))
                                solution += alpha[i+5] * 2
                        if board == endV:
                            solved = True
                            if allPos:
                                display(solution)
                                allConfig.append(solution)
                            else:
                                return solution
    if not solved:
        print("IMPOSSIBLE")

    return allConfig


def display(word):
    for letter in alpha:
        if word.count(letter) == 1:
            print(letter.lower(), end="")
        elif word.count(letter) == 2:
            print(letter, end="")
    print()

# PRINT ALL
#solve(input(), True)
# PRINT ONE
display(solve(boardToVector(input())))



"""
For each combination of buttons on the top row, there is only 1 button on the row below that effects that button, so we
now know how many times we can press that button. We can use this to work our way along the rows, row by row. If we 
finish and the grid is not zero we know this solution does not work. This means we only have to brute force the top row:
3^5 = 243 combinations
"""

"""
b) 11110 = abcdghiJNot
   01112
   00021
   00001
   00000

c) 598
Lights will only become bright if 2 presses over lap


d) No. Every time a button is pressed, the lights change in a manner that is not effected by their current state. If 
two systems have different configurations then at least 1 light must be in a different state. By pressing buttons in a
specific sequence, the lights will change in a consistent manner. The sequence of buttons to unlock the first configuration
leaves all lights off. However, since at least one light is in a different state in the second configuration, the same
sequence of button presses will leave the lights in different states in states that are not off.
"""

def c():
    start = [0 for i in range(25)]
    ans = 0
    for a in alpha:
        for b in alpha:
            for c in alpha:
                if a < b and b < c:
                    output = add(vector[c], add(vector[b], add(start, vector[a])))
                    if 2 not in output: ans += 1
    print(ans)
c()
from functools import lru_cache
from math import *
from time import time
from itertools import combinations_with_replacement as comb, permutations

def parse(a, b, i):
    return a(b(a(i)))

def E(i):
    return i*2

def O(i):
    return i*2-1

@lru_cache(maxsize=None)
def T_brute(i):
    if i == 1: return 1
    j = 1
    x = 1
    while j < i:
        x += 1
        j += x
#        print(x, i, j)
    return x

def T(i):
    return T_brute(i)
    # TODO - DOESN'T WORK
    return int(sqrt((i)*2.5))

def get_bracket(string, i):
    depth = 1
    i += 1
#    print(string,i)
    while True:
        if string[i] == "(": depth += 1
        elif string[i] == ")":
            depth -= 1
            if depth == 0: return i
        i += 1

def expand_fully(string):
    if len(string) == 1: return string
    if "(" not in string:
        left = string[0]
        for i in range(1, len(string)):
            right = string[i]
            left = right + left + right

        return left

    left = ""
    right = ""
    right_ptr = 0

    if string[0] == "(":
        # cry
        bend = get_bracket(string, 0)
        left = expand_fully(string[1:bend])
        right_ptr = bend + 1
    else:
        left = string[0]
        right_ptr = 1

    while right_ptr < len(string):
        if string[right_ptr] == "(":
            # cry
            bend = get_bracket(string, right_ptr)
            right = expand_fully(string[right_ptr+1:bend])
            left = right + left + right
            right_ptr = bend + 1
        else:
            right = string[right_ptr]
            left = right + left + right
            right_ptr += 1

    return left

def parse_fully(string, i):
    string = string[::-1]
    for c in string:
        if c == "E": i = E(i)
        if c == "O": i = O(i)
        if c == "T": i = T(i)
    return i

string, i = input().split()
i = int(i)
start = time()
string = expand_fully(string)
print(parse_fully(string, i))
print("Time taken:", time() - start)

"""
b) 20
c) 41
"""

def b():
    i = 1
    count = 0
    x = 0
    while x <= 2:
        x = parse_fully(expand_fully("TT"), i)
        if x == 2:
            count += 1
        i += 1
    print(count)

#b()

def has_99(string):
    x = 0
    i = 1
    while x < 99 and i < 100000:
        x = parse_fully(string, i)
        i += 1
    if x == 99:
        return True


def c():
    letters = "ABCD"
    seen = set()
    count = 0
    options = ["A", "AB", "ABC", "A(BC)", "ABCD", "AB(CD)", "A(BC)D", "A(BCD)", "A(B(CD))"]
    for option in options:
        i = len(option) - option.count("(") - option.count(")")
        for c in comb("OTE", i):
            for p in permutations(c, i):
                string = option
                for j in range(i):
                    string = string.replace(letters[j], p[j])
                string = expand_fully(string)
                if string in seen:
                    continue
                seen.add(string)
                print(string, end=" ")
                if has_99(string):
                    print("YES")
                    count += 1
                else: print()
    print(count)
#c()

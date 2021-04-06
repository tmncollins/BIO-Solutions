def to_numeral(n):
    numerals = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
    num = ""
    while n > 0:
        for item in sorted(numerals.keys())[::-1]:
            if n >= item:
                num += numerals[item]
                n -= item
                break
    return num.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")

print(to_numeral(int(input())))

"""
b) LXIII + XXXVIII = CI
   MCCXLIX + DCXV = MDCCCLXIV

c) 3800 more
   55 less
"""

def c(n):
    more = 0
    less = 0
    for i in range(1, n):
        numeral = to_numeral(i)
        if len(numeral) > len(str(i)):
            more += 1
        elif len(numeral) < len(str(i)):
            less += 1
    print(more, "more")
    print(less, "less")
#c(4000)

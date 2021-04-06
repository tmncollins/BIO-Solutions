import time

number, n = input().split()
n = int(n)

start = time.time()

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


def look_and_say(n):
    new = ""
    curr = ""
    count = 0
    for l in n:
        if l != curr:
            if count > 0:
                new += to_numeral(count) + curr
            curr = l
            count = 1
        else:
            count += 1
    return new + to_numeral(count) + curr

for i in range(n):
    number = look_and_say(number)
#    print(number)

print(number.count("I"), number.count("V"))
print("Time:", time.time() - start)

"""
b) II, III, IV, IX

c) 3919 

"""

def c():
    seen = set()
    for i in range(1,4000):
        numeral = to_numeral(i)
        seen.add(look_and_say(numeral))
    print(len(seen))

#c()

m = input()

digits = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
print(len(m))
for d in digits:
    a = 0
    i = -1
    found = True
    n = list(m)
    while a < len(d):
        found = False
        q = i
        while d[a] in n:
            q = n.index(d[a])
            n.pop(q)
            if q > i:
                found = True
                break
            i -= 1
        i = q - 1
        a += 1
        if not found:
            break
    if found:
        print(digits.index(d) + 1)
        break
if not found:
    print("NO")

"""
b) 10
T[1]W[1]O[1]
T[1]W[1]O[2]
T[1]W[1]O[3]
T[1]W[2]O[2]
T[1]W[2]O[3]
T[1]W[3]O[3]
T[2]W[2]O[2]
T[2]W[2]O[3]
T[2]W[3]O[3]
T[3]W[3]O[3]

c) 12 (THWFIOURVNEE)
   18 (NSFEIGHTHWOURVENEX)
   
d) 
"""

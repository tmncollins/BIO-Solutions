num = int(input())


def anagram(num):
    numbers = []
    for i in range(2,10):
        q = str(num * i)
        if sorted(list(q)) == sorted(list(str(num))):
            numbers.append(i)
    return numbers

numbers = anagram(num)
if len(numbers) == 0:
    print("NO")
else:
    for n in numbers: print(n, end=" ")
    print()

"""
b) 28415970 [3], 17049582 [5], 14207985 [6]
c) 138
"""
"""
# code for c
tot = 0
for i in range(100000, 1000000):
    if i % 10000 == 0 : print(i)
    if len(anagram(i)) > 0:
        if len(str(i)) == len(set(list(str(i)))):
            tot += 1
print("tot:", tot)
"""

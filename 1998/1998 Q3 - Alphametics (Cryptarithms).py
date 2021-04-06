from itertools import permutations, combinations_with_replacement
import time

"""
NOTE THAT THIS SOLUTION IS FAR TOO SLOW FOR SOME TEST CASES
"""

n = int(input())

sumWords = []
totWord = ""
for i in range(n-1):
   sumWords.append(input())
totWord = input()

start = time.time()

def output(switch):
   global sumWords, totWord
   out = ""
   for item in sumWords:
       out += "".join(switch[l] for l in item)
       out += " + "
   out = out[:-2]
   out += "= " + "".join(switch[l] for l in totWord)
   print(out)

def test(words, tot):
   t = 0
   for item in words:
       t += int(item)
   return t == int(tot)


def solve(equation):

    # letters begin with startletters
    sumWords = equation.replace("=","+").replace(" ", "").split("+")
    startLetters = {word[0] for word in sumWords}
    letters = sorted(set("".join(sumWords)).difference(startLetters))
    numbers = "1234567890"
    letters = sorted(startLetters) + letters
    first = len(startLetters)

    options = list(permutations(numbers, len(letters)))

    solutions = 0
    for item in options:

        if "0" in item[:first]:
           continue

        switch = str.maketrans("".join(letters), "".join(item))
        w = equation.translate(switch)

        tot = 0
        for i in sumWords[:-1]:
            tot += int(i.translate(switch))
        if tot == int(sumWords[-1].translate(switch)):
            print(w)
            solutions += 1

    if solutions == 0:
        print("Impossible")
    if solutions == 1:
        print("Unique")

    return solutions

equation = ""
for item in sumWords:
    equation += item + " + "
equation = equation[:-2]
equation += "= " + totWord

solve(equation)

print("Time:", time.time() - start)

"""
b) 309 + 19865 += 20174
309 + 19847 += 20156
509 + 39862 += 40371
509 + 19674 += 20183
509 + 39817 += 40326
509 + 19638 += 20147
609 + 19574 += 20183
609 + 19538 += 20147
709 + 59832 += 60541
709 + 59814 += 60523
809 + 39562 += 40371
809 + 59732 += 60541
809 + 59714 += 60523
809 + 19365 += 20174
809 + 19347 += 20156
809 + 39517 += 40326

c) Yes.
  A+A+A+A+A+A+A+A+A+A+A = AA
  Valid for A = 1-9

d) 163
   1136

"""

def d():
    count = 0
    count2 = 0
    options = combinations_with_replacement("ABCDE", 3)
    seen = set()
    for item in options:
        for i in permutations(list(item)):
            i = "".join(i)
            if i not in seen:
                seen.add(i)
                s = solve("ABC + DEA = " + i)
                count2 += s
                if s: count += 1
    options = combinations_with_replacement("ABCDE", 4)
    for item in options:
        for i in permutations(list(item)):
            i = "".join(i)
            if i not in seen:
                seen.add(i)
                s = solve("ABC + DEA = " + i)
                count2 += s
                if s: count += 1

    print(count, count2)

#d()
from collections import deque, defaultdict
from time import time

def number_to_string(n):
    n = str(n)
    string = ""
    word = ["ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    for i in n:
        string += word[int(i)]
    return string

def count_differences(a,b):
  alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  diff = 0
  for letter in alpha:
    diff += abs(a.count(letter) - b.count(letter))
  return diff


def number_ladder(start, end):

    digits = set(str(start))
    for s in str(end): digits.add(s)
    digits.add("0")
    numbers = []
    for i in range(1, 1000):
        j = str(i)
        valid = True
        for s in j:
            if s not in digits:
                valid = False
                break
        if valid: numbers.append(i)

    q_start = deque()
    q_start.append(start)
    q_end = deque()
    q_end.append(end)

    dist_start = defaultdict(int)
    dist_start[start] = 1
    dist_end = defaultdict(int)
    dist_end[end] = 1

    while True:
        # start
        u = q_start.popleft()
        u_string = number_to_string(u)
        for i in numbers:
            if dist_start[i] == 0 and count_differences(number_to_string(i), u_string) <= 5:
                # can move here
                q_start.append(i)
                dist_start[i] = dist_start[u] + 1
                if dist_end[i] != 0:
                    # meet in the middle
                    return dist_start[i] + dist_end[i] - 2
        # end
        u = q_end.popleft()
        u_string = number_to_string(u)
        for i in numbers:
            if dist_end[i] == 0 and count_differences(number_to_string(i), u_string) <= 5:
                # can move here
                q_end.append(i)
                dist_end[i] = dist_end[u] + 1
                if dist_start[i] != 0:
                    # meet in the middle
                    return dist_start[i] + dist_end[i] - 2


total_time = 0
for i in range(3):
    start, end = list(map(int, input().split()))
    start_t = time()
    print(number_ladder(start, end))
    dtime = time() - start_t
    total_time += dtime
    print(dtime)
print(total_time)


# transformations between two numbers with different numbers of digits will also take < 6 steps as we can always add /
# remove a digit we need in one move
def c():
    graph = defaultdict(set)
    for i in range(1, 1000):
        i_str = number_to_string(i)
        for j in range(1, i):
            if count_differences(i_str, number_to_string(j)) <= 5:
                graph[i].add(j)
                graph[j].add(i)
    print("graphed")
    print(graph)

    sixes = set()
    for i in range(100, 1000):
        if i % 10 == 0:
            print(i)
        q = deque()
        q.append((i, 0))
        seen = {i}
        while q:
            u, d = q.popleft()
            if d == 6:
                sixes.add((i, u))
                continue
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    q.append((v, d+1))
    print(len(sixes))

"""
b) 15: [1, 2, 3, 4, 10, 14, 20, 30, 40, 41, 50, 60, 70, 80, 90]
c) 6, 10302
d) Yes. The digit 0 can be transformed to any other digit. Therefore any digit can be transformed to any other digit.
Thus, any integer can be transformed to any other integer. An integer of size n can be transformed to any other integer
of size n by changing each digit in turn. 
"""

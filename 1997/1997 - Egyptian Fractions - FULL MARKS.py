# With thanks to @h1b2k

import sys
import math
from fractions import Fraction

solutions = []


def remove_duplicates(lst):
    return [list(x) for x in dict.fromkeys(tuple(sorted(x, reverse=True)) for x in lst)]


def optimize(lst):
    return [sublist for (min_frac, sublist) in [(min(sublist), sublist) for sublist in lst] if min_frac == max([(min(sublist), sublist) for sublist in lst], key=lambda x: x[0])[0]]


def recursive_chunk(f, max_depth, path=[]):
    start = max(math.floor(f.denominator / f.numerator), path[-1].denominator + 1 if path else 1)

    for i in range(start, 32001):
        unit = Fraction(1, i)
        if unit * (max_depth - len(path)) < f:
            break

        new_path = path + [unit]
        if unit == f:
            solutions.append(new_path)
            return
        elif unit < f and len(new_path) <= max_depth:
            recursive_chunk(f - unit, max_depth, new_path)


def main():
    num, den = map(int, input("input: ").split())
    fra = Fraction(num, den)

    solutions.clear()
    for depth in range(1, num + 1):
        sys.stdout.write(f"\rdepth: {depth}      ")
        sys.stdout.flush()
        recursive_chunk(fra, depth)
        if solutions:
            break

    sys.stdout.write(f"\r")

    if solutions:
        filtered = remove_duplicates(solutions)
        optimized = optimize(filtered)
        for s in optimized:
            print(' '.join(str(f.denominator) for f in s))
    else:
        print("no solutions found.")


if __name__ == "__main__":
    while True:
        try:
            main()
        except Exception as e:
            print(f"Error: {e}")

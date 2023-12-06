import re
from math import sqrt, floor, ceil

with open("06.txt") as f:
    raw = f.read().split("\n")


def solve(t, d):
    x1 = (t + sqrt(t**2 - 4 * d)) / 2
    x2 = (t - sqrt(t**2 - 4 * d)) / 2
    return ceil(x1 - 1) - floor(x2 + 1) + 1


ts, ds = [map(int, re.findall("(\d+)", line)) for line in raw]
t2, d2 = [map(int, re.findall("(\d+)", line.replace(" ", ""))) for line in raw]

p1 = p2 = 1

for t, d in zip(ts, ds):
    p1 *= solve(t, d)

p2 = solve(*t2, *d2)

print(p1, p2)

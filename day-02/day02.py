import re
from math import prod

with open("day02.txt") as f:
    raw = f.read().split("\n")

COLOURS = {"blue": 14, "red": 12, "green": 13}
result_1 = result_2 = 0

for line in raw:
    is_ok = True
    dct = {}
    game = re.search("(\d+)", line).group()
    for colour in COLOURS.keys():
        groups = [re.findall("\d+", x) for x in re.findall(f"\d+ {colour}", line)]
        groups = [x for y in groups for x in y]
        groups = max(map(int, groups))
        dct[colour] = groups
    result_2 += prod(dct.values())
    for k, v in COLOURS.items():
        if dct[k] > v:
            is_ok = False
            break
    if is_ok:
        result_1 += int(game)


print(result_1)
print(result_2)

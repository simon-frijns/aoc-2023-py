import re

with open("day03.txt") as f:
    raw = f.read().split("\n")

raw = list(map(str, [("." + line + ".") for line in raw]))
padding = ["." * len(raw[0])]
raw[:0] = padding  # front
raw.extend(padding)  # end


def check_round(start, end, linenum):
    result = False
    scope = [line[start - 1 : end + 1] for line in raw[linenum - 1 : linenum + 2]]
    scope = "".join(list([ch for s in scope for ch in s]))
    a = re.findall("[^.\d]", scope)
    if a:
        result = True
    return result


part1 = 0
all_nums = []
for linenum, line in enumerate(raw):
    numbers = [
        [int(m[0]), m.start(), m.end(), linenum] for m in re.finditer("(\d+)", line)
    ]
    all_nums.extend(numbers)
    for match in numbers:
        part1 += match[0] * check_round(match[1], match[2], linenum)

part2 = 0
for linenum, line in enumerate(raw):
    gears = [m.start() for m in re.finditer("[*]", line)]
    for gear in gears:
        a = [
            num[0]
            for num in all_nums
            if (num[1] - 1) <= gear <= num[2] and num[3] - 1 <= linenum <= num[3] + 1
        ]
        if len(a) == 2:
            part2 += a[0] * a[1]

print(part1)
print(part2)

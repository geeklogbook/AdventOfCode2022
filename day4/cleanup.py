# 2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7 *
# 6-6,4-6 *
# 2-6,4-8


with open("day4\source.txt", "r") as f:
    elements = [line.strip() for line in f]


total = 0
for element in elements:
    el1, el2 = element.split(',')
    d1a, d2a = el1.split('-')
    d1b, d2b = el2.split('-')
    if (int(d1a) <= int(d1b) and int(d2a) >= int(d2b)):
        total += 1
    else:
        if (int(d1a) >= int(d1b) and int(d2a) <= int(d2b)):
            total += 1

print(total)

calories = []

with open("day1\source.txt", "r") as f:
    elements = [line.strip() for line in f]

total = 0
for e in elements:
    if e != '':
        total += int(e)
    if e == '' or elements.index(e) == len(elements) - 1:
        calories.append(total)
        total = 0


print(calories)

max = max(calories)
max_ren = calories.index(max) + 1

calories.sort(reverse=True)
print(sum(calories[0:3]))

# print(max)
# print(max_ren)

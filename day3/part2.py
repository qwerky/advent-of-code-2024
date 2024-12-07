import re

p = re.compile("mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don\\'t\\(\\)")
p2 = re.compile("[0-9]{1,3}")

input = open("day3/input.txt", "r")
sum = 0
enabled = True
for line in input:
    for match in p.findall(line):
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            numbers = p2.findall(match)
            result = int(numbers[0]) * int(numbers[1])
            sum += result

print(sum)
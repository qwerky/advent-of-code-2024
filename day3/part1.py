import re

p = re.compile("mul\\([0-9]{1,3},[0-9]{1,3}\\)")
p2 = re.compile("[0-9]{1,3}")

input = open("day3/input.txt", "r")
sum = 0
for line in input:
    for match in p.findall(line):
        numbers = p2.findall(match)
        result = int(numbers[0]) * int(numbers[1])
        sum += result

print(sum)
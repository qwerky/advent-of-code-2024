def mul(one, two):
    return int(one) * int(two)


def add(one, two):
    return int(one) + int(two)


def concat(one, two):
    return int(str(one) + str(two))

def reduce(candidates, target):
    # Failure state where there are no more combos to check
    if len(candidates) == 0:
        print("No more candidates: line is bad")
        return False

    numbers = candidates.pop()
    first = numbers.pop(0)
    second = numbers.pop(0)

    m = mul(first, second)
    a = add(first, second)
    c = concat(first, second)

    if len(numbers) == 0:
        # Success state where we checked the last two numbers and they are good
        if m == target or a == target or c == target:
            print("last two numbers work out, line is good")
            return True

    
    if len(numbers) > 0:
        if m <= target:
            newNumbers = numbers.copy()
            newNumbers.insert(0, m)
            candidates.append(newNumbers)

        if a <= target:
            newNumbers = numbers.copy()
            newNumbers.insert(0, a)
            candidates.append(newNumbers)

        if c <= target:
            newNumbers = numbers.copy()
            newNumbers.insert(0, c)
            candidates.append(newNumbers)

    return reduce(candidates, target)

###############################################################
# Fire up the recursion warp drive... see how deep we can go! #
###############################################################
import sys
sys.setrecursionlimit(88500)

input = open("day7/input.txt", "r")
lines = input.readlines()

total = 0
for line in lines:
    target = int(line.split(":")[0])
    numbers = line.split()[1:]

    candidates = []
    candidates.append(numbers)

    print("Checking " + line)
    if reduce(candidates, target):
        total += target

print(total)
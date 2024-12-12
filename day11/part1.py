import math

def blink(num):
    if num == 0:
        return [1]
    else:
        text = str(num)
        digits = len(text)
        if digits % 2 == 0:
            midpoint = int(digits/2)
            left = text[:midpoint]
            right = text[midpoint:]
            return [int(left), int(right)]
        else:
            return [num*2024]


input = open("day11/input.txt", "r").readline().strip()
stones = [int(n) for n in input.split()]
for round in range(25):
    newStones = []
    while len(stones) > 0:
        stone = stones.pop(0)
        newStones.extend(blink(stone))
    stones = newStones
    print(str(round) + " size is " + str(len(stones)))
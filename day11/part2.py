import math

def blink(item:tuple):
    if item[0] == 0:
        return [(1,item[1])]
    else:
        text = str(item[0])
        digits = len(text)
        if digits % 2 == 0:
            midpoint = int(digits/2)
            left = text[:midpoint]
            right = text[midpoint:]
            return [(int(left),item[1]), (int(right),item[1])]
        else:
            return [(item[0]*2024,item[1])]

# Compact the list of stones, merging duplicates together
def compact(stones:list):
    newStones = []
    stones.sort(key=lambda e: e[0])
    while len(stones) > 0:
        next = stones.pop(0)
        count = next[1]
        while len(stones) > 0 and stones[0][0] == next[0]:
            next = stones.pop(0)
            count += next[1]
        newStones.append((next[0],count))
    return newStones
    
    
def count(stones:list):
    c = 0
    for s in stones:
        c += s[1]
    return c
    



input = open("day11/input.txt", "r").readline().strip()
stones = [(int(n), 1) for n in input.split()]

# We were lied to. The order of the stones doesn't matter.
# Once this is realised, the list of stones can be sorted and represented as the engraved number and then the count of how many stones there are with that number.
# For example after 3 rounds the input looks like this;
#   2343241472, 2277696256, 40, 48, 40, 48, 20, 24, 21629, 92128, 191678872, 77932096, 2, 0, 2, 4, 21, 70, 74, 0, 4048, 14168, 18216, 1
# when sorted this looks like;
#   0, 0, 1, 2, 2, 4, 20, 21, 24, 40, 40, 48, 48, 70, 74, 4048, 14168, 18216, 21629, 92128, 77932096, 191678872, 2277696256, 2343241472
# so the list can be compacted like this;
#   (0,2), (1, 1), (2, 2), (4,1), (20,1), (21,1) etc

for round in range(75):
    newStones = []
    while len(stones) > 0:
        stone = stones.pop(0)
        newStones.extend(blink(stone))
    stones = compact(newStones)
print(count(stones))
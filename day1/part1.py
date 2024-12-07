input = open("day1/input.txt", "r")
lines = input.readlines()

l1 = []
l2 = []

for line in lines:
    l1.append(int(line.split()[0]))
    l2.append(int(line.split()[1]))
input.close()

l1.sort()
l2.sort()

distance = 0
for index in range(len(l1)):
    loc1 = l1[index]
    loc2 = l2[index]
    distance += abs(loc1-loc2)

print(distance)
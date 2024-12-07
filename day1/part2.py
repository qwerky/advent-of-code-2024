input = open("day1/input.txt", "r")
lines = input.readlines()

l1 = []
l2 = []

for line in lines:
    l1.append(int(line.split()[0]))
    l2.append(int(line.split()[1]))
input.close()

similarity = 0
for loc1 in l1:
    similarity += loc1 * l2.count(loc1)

print(similarity)
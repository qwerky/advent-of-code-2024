from safe import safe
    
input = open("day2/input.txt", "r")

count = 0
for line in input:
    report = line.split()
    if (safe(report)):
        count += 1
input.close()

print(count)


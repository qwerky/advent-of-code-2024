from safe import safe
    
input = open("day2/input.txt", "r")

count = 0
for line in input:
    report = line.split()
    if safe(report):
        count += 1
    else:
        # There must be a better way to do this, but with only 1000 reports, and the reports being small, optimisation is not required
        for index in range(len(report)):
            fixedReport = report.copy()
            del(fixedReport[index])
            if safe(fixedReport):
                count += 1
                break
    
input.close()

print(count)


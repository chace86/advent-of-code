lines = open("day2-data.txt")
reports = [list(map(int, line.split())) for line in lines]
passing = 0

for report in reports:
    length = len(report)
    sign = 0
    count = 0

    for i in range(0, length - 1):
        diff = report[i] - report[i + 1]

        # set sign based on first pair
        if sign == 0: sign = 1 if diff > 0 else -1

        # diff absolute value must be > 0 and <= 3
        abs = diff * sign
        if abs <= 0 or abs > 3: break
        count += 1
    
    if count == length - 1:
        passing += 1

print(passing)

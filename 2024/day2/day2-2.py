
def is_safe(report: list[int]) -> bool:
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

    return count == length - 1

lines = open("day2-data.txt")
reports = [list(map(int, line.split())) for line in lines]
passing = 0

for report in reports:
    if is_safe(report):
        passing +=1
    else:
        for i, level in enumerate(report):
            report_copy = report.copy()
            report_copy.pop(i)
            if is_safe(report_copy):
                passing +=1
                break

print(passing)

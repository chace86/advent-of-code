import re

with open("day1-data.txt") as file:
    lines = [line.rstrip() for line in file]

a = []
b = []
for line in lines:
    m = re.search("(\d+)\s+(\d+)", line)
    a.append(int(m.group(1)))
    b.append(int(m.group(2)))

a.sort()
b.sort()

sum = 0
for i, n in enumerate(a):
    sum += abs(n - b[i])

# we expect 1765812
print(sum)

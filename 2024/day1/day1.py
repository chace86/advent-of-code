import re

with open("day1-data.txt") as f:
    lines = [line.rstrip() for line in f]

score = {}
l = []
for line in lines:
    m = re.search("(\d+)\s+(\d+)", line)
    score[int(m.group(1))] = 0
    l.append(int(m.group(2)))

for n in l:
    if n in score:
        score[n] += 1

sum = 0
for key, value in score.items():
    sum += (key * value)

print(sum) # 20520794

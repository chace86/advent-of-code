import re

memory = open("day3-data.txt").read()
tuples = re.findall("mul\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)", memory)
total = 0

active = True
for tuple in tuples:
    if "do" in tuple:
        active = True
    elif "don't" in tuple:
        active = False
    elif active:
        total += int(tuple[0]) * int(tuple[1])


print(total)

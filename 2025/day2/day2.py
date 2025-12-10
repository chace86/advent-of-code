
data = open('day2.txt').readline().split(",")

results = []

for d in data:
    parts = d.split("-")
    start = int(parts[0])
    end = int(parts[1])

    for i in range(start, end + 1):
        s = str(i)
        l = len(s)
        
        if l % 2 == 0 and s[0:l // 2] == s[l // 2: l]:
            results.append(i)

answer = sum(results)
print(f"The answer is: {answer}")

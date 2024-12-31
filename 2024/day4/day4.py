
matrix = []
with open("day4-data.txt") as file:
    for line in file:
        matrix.append(line.rstrip())

xmas = r'XMAS'

def check_lines(lines: list[str]) -> int:
    count = 0
    for line in lines:
        count += line.count(xmas)
        count += line[::-1].count(xmas)

    return count

def vertical(lines: list[str]) -> int:
    horizontal_lines: list[str] = [''] * len(lines)

    for line in lines:
        for i in range(0, len(line)):
            horizontal_lines[i] += line[i]

    return check_lines(horizontal_lines)

def diagonal(lines: list[str]) -> int:
  diagonals = []
  rows, cols = len(lines), len(lines[0])

  # top-left to bottom-right
  for d in range(-(rows - 1), cols):
      diag = [lines[i][i - d] for i in range(max(0, d), min(rows, cols + d))]
      diagonals.append(''.join(diag))

  # top-right to bottom-left
  for d in range(rows + cols - 1):
      diag = [lines[i][d - i] for i in range(max(0, d - cols + 1), min(rows, d + 1))]
      diagonals.append(''.join(diag))

  return check_lines(diagonals)

h = check_lines(matrix) # horizontal
v = vertical(matrix)
d = diagonal(matrix)

total = h + v + d
print(total)

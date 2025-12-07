from operator import add, sub

input = open('day1_input.txt').read()

current_position = 50
num_zeros = 0

for line in input.splitlines():
    clicks = int(line[1:])
    op = sub if line.startswith('L') else add

    current_position = op(current_position, clicks) % 100

    if current_position == 0:
        num_zeros += 1

print(f"The password is: {num_zeros}")

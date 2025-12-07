
input = open('day1_input.txt').read()

current_position = 50
num_zeros = 0

for line in input.splitlines():
    sign = -1 if line.startswith('L') else 1

    clicks = int(line[1:])
    full_rotations = clicks // 100
    remainder = clicks - (full_rotations * 100)
    new_position = current_position + (sign * remainder)
    # add 1 if the remainder causes current_position to pass zero
    # edge case, if current_position starts on zero, cannot pass zero
    n = int(current_position != 0 and not (0 < new_position < 100))

    num_zeros += full_rotations + n
    current_position = new_position % 100

print(f"The password is: {num_zeros}")

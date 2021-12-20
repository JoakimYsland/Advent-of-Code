
# https://adventofcode.com/2021/day/2

input_file = open('input.txt', 'r').readlines()
x, depth = 0, 0

for line in input_file:
	direction, distance = line.split()

	if (direction == 'forward'): x += int(distance)
	if (direction == 'up'): depth -= int(distance)
	if (direction == 'down'): depth += int(distance)

print(x * depth)
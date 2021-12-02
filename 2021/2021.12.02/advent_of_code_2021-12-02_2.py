
# https://adventofcode.com/2021/day/2

input_file = open('input.txt', 'r').readlines()
x, depth, aim = 0, 0, 0

for line in input_file:
	direction, val = line.split()
	val = int(val)

	if (direction == 'forward'): 
		x += val
		depth += aim * val
	if (direction == 'up'): aim -= val
	if (direction == 'down'): aim += val

print(x * depth)

# https://adventofcode.com/2021/day/1

input_file = open('input.txt', 'r').readlines()
previous_line = input_file[0]
counter = 0

for line in input_file:
	if (int(line) > int(previous_line)): 
		counter += 1
	previous_line = line

print(counter)
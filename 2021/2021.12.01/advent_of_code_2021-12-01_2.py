
# https://adventofcode.com/2021/day/1

from collections import deque

input_file = open('input.txt', 'r').readlines()
counter = 0
groups = deque([
	sum(int(d) for d in input_file[0:3]), 
	sum(int(d) for d in input_file[0:2]), 
	sum(int(d) for d in input_file[0:1]), 
])
previous_group = groups[0]

for line in input_file[3:]:
	groups.rotate(-1)
	groups[0] += int(line)
	groups[1] += int(line)
	groups[2] = int(line)

	if (groups[0] > previous_group): 
		counter += 1

	previous_group = groups[0]

print(counter)
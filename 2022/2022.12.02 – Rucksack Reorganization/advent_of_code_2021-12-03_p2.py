
# https://adventofcode.com/2022/day/3

import string

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

def get_priority(item): 
	priority = string.ascii_lowercase.index(item.lower())
	if item.islower(): 
		priority += 1
	elif item.isupper(): 
		priority += 27
	return priority

sum_priorities = 0
groups = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	if i % 3 == 0: 
		groups.append([])
	groups[-1].append(line)

for group in groups: 
	for item in group[0]: 
		if item in group[1] and item in group[2]: 
			sum_priorities += get_priority(item)
			break

print("sum_priorities:", sum_priorities)
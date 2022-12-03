
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

for line in input_file:

	line = line.rstrip()

	num_items = len(line)
	compartments = [
		line[0:int(num_items / 2)], 
		line[int(num_items / 2): num_items], 
	]

	item_distribution = {}

	for i, compartment in enumerate(compartments): 
		for item in compartment: 
			if not item in item_distribution: 
				item_distribution[item] = [0,0]
			item_distribution[item][i] += 1

		for item, quantities in item_distribution.items(): 
			if quantities[0] > 0 and quantities[1] > 0: 
				sum_priorities += get_priority(item)

print("sum_priorities:", sum_priorities)
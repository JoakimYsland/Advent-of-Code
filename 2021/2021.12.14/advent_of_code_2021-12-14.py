
# https://adventofcode.com/2021/day/14

# import re
# import statistics
# from collections import deque
# from collections import namedtuple

# Vec2 = namedtuple("Vec2", ['x', 'y'])

def run(run_title, input_file):

	# --------------------------------------------------------------------------------

	# Test / Real – 1588 / 3906

	polymer_template = ''
	pair_insertion_rules = {}

	for line in input_file: 
		split = line.strip().split(' -> ')
		if (len(split) == 1):
			if len(line) > 1:
				polymer_template = split[0]
		else: 
			pair_insertion_rules[split[0]] = split[1]

	for step in range(0, 10): 
		new_polymer = polymer_template

		for i in range(0, len(polymer_template) - 1):
			pair = polymer_template[i] + polymer_template[i+1]
			new_element = pair_insertion_rules[pair]
			before = new_polymer[0:(i*2)+1]
			after = new_polymer[(i*2)+1:len(new_polymer)]
			new_polymer = before + new_element + after

		polymer_template = new_polymer

	polymer_dict = {}
	for element in polymer_template:
		if element in polymer_dict: 
			polymer_dict[element] += 1
		else: 
			polymer_dict[element] = 1

	min_max_element_difference = max(polymer_dict.values()) - min(polymer_dict.values())

	print(run_title, "min_max_element_difference:", min_max_element_difference)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())

# https://adventofcode.com/2021/day/14

import re
# import statistics
# from collections import deque

def run(run_title, input_file):

	def add_pair(pair, count):
		polymer_pairs.setdefault(pair, 0)
		polymer_pairs[pair] += count

	def remove_pair(pair, count):
		if pair in polymer_pairs:
			polymer_pairs[pair] -= count
			if (polymer_pairs[pair] < 1): 
				del polymer_pairs[pair]

	def count_element(element, count): 
		element_count.setdefault(element, 0)
		element_count[element] += count

	# --------------------------------------------------------------------------------

	# Test / Real – 2188189693529 / 4441317262452

	polymer_pairs = {}
	element_count = {}
	pair_insertion_rules = {}

	for line in input_file: 
		split = re.split(' -> ', line.strip())
		if len(split) == 1:
			if len(split[0]) > 1:
				for element in split[0]: 
					count_element(element, 1)
				for i in range(0, len(split[0]) - 1):
					pair = line[i] + line[i+1]
					add_pair(pair, 1)
		else: 
			pair, new_element = split[0], split[1]
			pair_insertion_rules[pair] = new_element

	for step in range(0, 40): 
		for pair, count in polymer_pairs.copy().items(): 
			new_element = pair_insertion_rules[pair]
			count_element(new_element, count)
			remove_pair(pair, count)
			add_pair(pair[0] + new_element, count)
			add_pair(new_element + pair[1], count)

	element_count_range = max(element_count.values()) - min(element_count.values())
	print(run_title, "element_count_range:", element_count_range)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
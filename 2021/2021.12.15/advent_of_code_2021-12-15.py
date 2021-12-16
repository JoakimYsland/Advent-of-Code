
# https://adventofcode.com/2021/day/15

import re

def run(run_title, input_file):

	# def add_pair(pair, count):
	# 	polymer_pairs.setdefault(pair, 0)
	# 	polymer_pairs[pair] += count

	# def remove_pair(pair, count):
	# 	if pair in polymer_pairs:
	# 		polymer_pairs[pair] -= count
	# 		if (polymer_pairs[pair] < 1): 
	# 			del polymer_pairs[pair]

	# def count_element(element, count): 
	# 	element_count.setdefault(element, 0)
	# 	element_count[element] += count

	# --------------------------------------------------------------------------------

	# Test / Real – 2188189693529 / 4441317262452

	# polymer_pairs = {}
	# element_count = {}
	# pair_insertion_rules = {}
	risk_map = []

	for line in input_file: 
		risk_map.append([int(c) for c in line.strip()])
	# 	split = re.split(' -> ', line.strip())
	# 	if len(split) > 1:
	# 		pair, new_element = split[0:2]
	# 		pair_insertion_rules[pair] = new_element
	# 	elif len(split[0]) > 1:
	# 		init_polymer = split[0]
	# 		for element in init_polymer: 
	# 			count_element(element, 1)
	# 		for i in range(0, len(init_polymer) - 1):
	# 			pair = line[i] + line[i+1]
	# 			add_pair(pair, 1)

	risk_map = [list(x) for x in zip(*risk_map)] # Transpose <3

	# for step in range(0, 40): 
	# 	for pair, count in polymer_pairs.copy().items(): 
	# 		new_element = pair_insertion_rules[pair]
	# 		count_element(new_element, count)
	# 		remove_pair(pair, count)
	# 		add_pair(pair[0] + new_element, count)
	# 		add_pair(new_element + pair[1], count)

	print(risk_map)

	# element_count_range = max(element_count.values()) - min(element_count.values())
	# print(run_title, "element_count_range:", element_count_range)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
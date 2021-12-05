
# https://adventofcode.com/2021/day/5

import re # Split string with multiple delimiters

def get_overlap_matrix(vent_lines):
	matrix = {}
	for vent_line in vent_lines:
		x = min(vent_line[0], vent_line[2])
		x2 = max(vent_line[0], vent_line[2])
		y = min(vent_line[1], vent_line[3])
		y2 = max(vent_line[1], vent_line[3])
		
		# Vertical
		if vent_line[0] == vent_line[2]: 
			for y in range(vent_line[1], vent_line[3]+1, 1):
				c = "{x},{y}".format(x = vent_line[0], y = y)
				matrix[c] = matrix[c] + 1 if (c in matrix) else 1

		# Horizontal
		if vent_line[1] == vent_line[3]: 
			for x in range(vent_line[0], vent_line[2]+1, 1):
				c = "{x},{y}".format(x = x, y = vent_line[1])
				matrix[c] = matrix[c] + 1 if (c in matrix) else 1

	return matrix

# --------------------------------------------------------------------------------

def run():
	# input_file = open('input.txt', 'r').readlines()
	input_file = open('input_test.txt', 'r').readlines()
	vent_lines = []

	for line in input_file: 
		vent_line = [int(c.strip()) for c in re.split(' -> |,', line)]
		vent_lines.append(vent_line)
	
	non_diagional_vent_lines = [v for v in vent_lines if v[0] == v[2] or v[1] == v[3]]
	overlap_matrix = get_overlap_matrix(non_diagional_vent_lines)
	print(overlap_matrix)

	overlaps = len([o for o in overlap_matrix.values() if o > 1])
	print(overlaps)

run()
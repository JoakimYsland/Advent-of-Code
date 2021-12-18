
# https://adventofcode.com/2021/day/5

import re # Split string with multiple delimiters

def get_overlap_matrix(vent_lines):
	matrix = {}
	for vl in vent_lines:
		vl_x, vl_x2 = min(vl[0], vl[2]), max(vl[0], vl[2])
		vl_y, vl_y2 = min(vl[1], vl[3]), max(vl[1], vl[3])

		# Vertical
		if vl_x == vl_x2: 
			for y in range(vl_y, vl_y2+1, 1):
				c = "{x},{y}".format(x=vl_x, y=y)
				matrix[c] = matrix[c] + 1 if (c in matrix) else 1

		# Horizontal
		if vl_y == vl_y2: 
			for x in range(vl_x, vl_x2+1, 1):
				c = "{x},{y}".format(x=x, y=vl_y)
				matrix[c] = matrix[c] + 1 if (c in matrix) else 1

	return matrix

# --------------------------------------------------------------------------------

def run():
	# input_file = open('input.txt', 'r').readlines()
	input_file = open('input.txt', 'r').readlines()
	vent_lines = []

	for line in input_file: 
		vent_line = [int(c.strip()) for c in re.split(' -> |,', line)]
		vent_lines.append(vent_line)
	
	non_diagional_vent_lines = [v for v in vent_lines if v[0] == v[2] or v[1] == v[3]]
	overlap_matrix = get_overlap_matrix(non_diagional_vent_lines)
	overlaps = len([o for o in overlap_matrix.values() if o > 1])
	print(overlaps)

run()
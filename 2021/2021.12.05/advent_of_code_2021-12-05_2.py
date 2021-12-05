
# https://adventofcode.com/2021/day/5

import re # Split string with multiple delimiters

def get_overlap_matrix(vent_lines):

	def plot(x, y):
		c = "{x},{y}".format(x=x, y=y)
		matrix[c] = matrix[c] + 1 if (c in matrix) else 1

	def traverse(p, p2):
		if 	 (p < p2): return p+1
		elif (p > p2): return p-1
		else: return p

	matrix = {}
	for vl in vent_lines:
		plot(vl[0], vl[1])
		while (vl[0] != vl[2]) or (vl[1] != vl[3]):
			vl[0] = traverse(vl[0], vl[2])
			vl[1] = traverse(vl[1], vl[3])
			plot(vl[0], vl[1])
	return matrix

# --------------------------------------------------------------------------------

def run():
	# input_file = open('input_test.txt', 'r').readlines()
	input_file = open('input.txt', 'r').readlines()
	vent_lines = []

	for line in input_file: 
		vent_line = [int(c.strip()) for c in re.split(' -> |,', line)]
		vent_lines.append(vent_line)
	
	# non_diagional_vent_lines = [v for v in vent_lines if v[0] == v[2] or v[1] == v[3]]
	overlap_matrix = get_overlap_matrix(vent_lines)
	overlaps = len([o for o in overlap_matrix.values() if o > 1])
	print("overlaps:", overlaps)

run()
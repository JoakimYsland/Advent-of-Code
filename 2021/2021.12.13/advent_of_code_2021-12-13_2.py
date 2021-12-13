
# https://adventofcode.com/2021/day/13

# import statistics
# from collections import deque
import re
from collections import namedtuple

Vec2 = namedtuple("Vec2", ['x', 'y'])
Fold = namedtuple("Fold", ['axis', 'pos'])

def run(run_title, input_file):

	def visualize():
		size_x, size_y = 0, 0
		for dot in manual:
			size_x = max(dot.x, size_x)
			size_y = max(dot.y, size_y)

		paper = [['.' for i in range(size_x + 1)] for j in range(size_y + 1)]
		for dot in manual:
			paper[dot.y][dot.x] = '#'
		
		for line in paper: 
			print(''.join(line))

	# --------------------------------------------------------------------------------

	# Test / Real – n/a / HECRZKPR

	visible_dots = 0
	manual = {}
	folds = []

	for line in input_file: 
		split = re.split(' |=|,', line.strip())
		if (len(split) == 2): 
			manual[Vec2(int(split[0]), int(split[1]))] = 1
		elif (len(split) == 4):
			folds.append(Fold(split[2], int(split[3])))
	
	for fold in folds: 
		if fold.axis == 'x': 
			affected_dots = [d for d in manual if d.x > fold.pos]
			for dot in affected_dots: 
				new_pos = Vec2(fold.pos - (dot.x - fold.pos), dot.y)
				manual[new_pos] = manual[new_pos] + 1 if new_pos in manual else 1
				del manual[dot]
		else:
			affected_dots = [d for d in manual if d.y > fold.pos]
			for dot in affected_dots: 
				new_pos = Vec2(dot.x, fold.pos - (dot.y - fold.pos))
				manual[new_pos] = manual[new_pos] + 1 if new_pos in manual else 1
				del manual[dot]

	visible_dots = len(manual)
	visualize()

	print(run_title, "visible_dots:", visible_dots)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
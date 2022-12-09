
# https://adventofcode.com/2022/day/8

import string
import numpy

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

forest = []

for line in input_file:

	line = line.rstrip()
	forest.append([int(c) for c in line])

def get_sight_lines(x, y): 
	column = [row[x] for r in forest]
	left = forest[y][0:x]
	right = forest[y][x + 1:len(forest[y])]
	top = column[0:y]
	bottom = column[y + 1:len(column)]
	return left, right, top, bottom

def get_scenic_score(tree, sight_lines): 
	sight_lines[0].reverse() # Left
	sight_lines[2].reverse() # Top

	scores = [0, 0, 0, 0]

	for i, sight_line in enumerate(sight_lines): 
		for t in sight_line: 
			if t <= tree: 
				scores[i] += 1
			if t >= tree: 
				break

	return numpy.prod(scores)

scenic_scores = []

for y, row in enumerate(forest): 
	scenic_scores.append([])
	for x, tree in enumerate(forest[y]):
		sight_lines = get_sight_lines(x, y)
		score = get_scenic_score(tree, sight_lines)
		scenic_scores[y].append(score)

print("Best Scenic Score:", numpy.max(scenic_scores))
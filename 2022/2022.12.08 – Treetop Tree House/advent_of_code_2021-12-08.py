
# https://adventofcode.com/2022/day/8

import string

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

forest = []

for line in input_file:

	line = line.rstrip()
	forest.append([int(c) for c in line])

def get_sight_lines(x, y): 
	column = [row[x] for row in forest]
	left = forest[y][0:x]
	right = forest[y][x + 1:len(forest[y])]
	top = column[0:y]
	bottom = column[y + 1:len(column)]
	return left, right, top, bottom

visible_trees = 0

for y, row in enumerate(forest): 
	if y == 0 or y == len(forest) - 1: 
		visible_trees += len(forest[y])
		continue
	for x, tree in enumerate(forest[y]): 
		if x == 0 or x == len(forest[y]) - 1: 
			visible_trees += 1
			continue
		sight_lines = get_sight_lines(x, y)
		for s in sight_lines: 
			if max(s) < tree: 
				visible_trees += 1
				break

print("visible_trees:", visible_trees)
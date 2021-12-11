
# https://adventofcode.com/2021/day/9

# import re # Split string with multiple delimiters
from collections import namedtuple

Vec2 = namedtuple("Vec2", ['x', 'y'])

def get_adjacent(x, y, map_size):
	adjacent = {'left':None, 'right':None, 'up':None, 'down':None}
	if (x > 0): 				adjacent['left'] 	= Vec2(x-1, y)
	if (x < map_size.x - 1): 	adjacent['right'] 	= Vec2(x+1, y)
	if (y > 0): 				adjacent['up'] 		= Vec2(x, y-1)
	if (y < map_size.y - 1):  	adjacent['down'] 	= Vec2(x, y+1)
	return adjacent

def is_low_point(cell, adjacent, height_map): 
	for c in adjacent.values():
		if c != None and height_map[c.y][c.x] <= cell: 
			return False
	return True

# def get_basin(basin, cell, height_map, map_size):
# 	if not cell in basin:
# 		basin.append(cell)
# 	adjacent = get_adjacent(height_map, x, y, map_size)
# 	spread = [c for c in ]

# --------------------------------------------------------------------------------

# Test / Real – 15 / 522
# Test / Real – 1134 / ???

def run(run_title, input_file):

	height_map = []
	for line in input_file: 
		height_map.append([int(c) for c in line.strip()])

	risk_level = 0
	map_size = Vec2(len(height_map[0]), len(height_map))

	for y, row in enumerate(height_map): 
		for x, cell in enumerate(row): 
			adjacent = get_adjacent(x, y, map_size)
			if is_low_point(cell, adjacent, height_map):
				risk_level += cell + 1
				# basin = []
				# get_basin(basin, Vec2(x, y), height_map, map_size)
				# print("asd")

	print(run_title, "risk_level:", risk_level)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
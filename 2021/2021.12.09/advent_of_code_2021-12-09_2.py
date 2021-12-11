
# https://adventofcode.com/2021/day/9

# import re # Split string with multiple delimiters
from collections import namedtuple
import math

Vec2 = namedtuple("Vec2", ['x', 'y'])

def run(run_title, input_file):

	def get_adjacent(x, y):
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

	def get_basin(basin, cell_pos, height_map):
		pos = ("{0},{1}").format(cell_pos.x, cell_pos.y)
		if not pos in basin:
			basin.append(pos)
		adjacent = get_adjacent(cell_pos.x, cell_pos.y)
		adjacent_spread = []
		for c in adjacent.values():
			if (c != None):
				pos = ("{0},{1}").format(c.x, c.y)
				height = height_map[c.y][c.x]
				if not pos in basin and height < 9:
					adjacent_spread.append(c)
		for c in adjacent_spread: 
			get_basin(basin, Vec2(c.x, c.y), height_map)

		return basin

	# --------------------------------------------------------------------------------

	# Test / Real – 1134 / 916688

	height_map = []
	for line in input_file: 
		height_map.append([int(c) for c in line.strip()])

	risk_level = 0
	basins = []
	map_size = Vec2(len(height_map[0]), len(height_map))

	for y, row in enumerate(height_map): 
		for x, cell in enumerate(row): 
			adjacent = get_adjacent(x, y)
			if is_low_point(cell, adjacent, height_map):
				risk_level += cell + 1
				basin = get_basin([], Vec2(x, y), height_map)
				basins.append(basin)

	basins = sorted(basins, key=len, reverse=True)
	top3_basin_area_prod = math.prod([len(b) for b in basins[0:3]])

	print(run_title, "risk_level:", risk_level)
	print(run_title, "top3_basin_area_prod:", top3_basin_area_prod)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
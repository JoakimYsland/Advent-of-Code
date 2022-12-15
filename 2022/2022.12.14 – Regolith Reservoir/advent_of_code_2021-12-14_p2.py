
# https://adventofcode.com/2022/day/14

import string
import math
import time
import re
import ast
import copy

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

class Vec2:
	def __init__(self, x, y): 
		self.x = x
		self.y = y
	def __str__(self):
		s = "{0},{1}"
		return s.format(self.x, self.y)
	def __add__(self, v): 
		return Vec2(self.x + v.x, self.y + v.y)

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

bounds_min = Vec2(9999,0)
bounds_max = Vec2(0,0)
w, e, s = "█", ".", "O"

for i, line in enumerate(input_file):

	line = line.rstrip()
	decomposed = re.split(',| -> ', line)

	# Calculate bounds
	for i in range(0, len(decomposed), 2): 
		pos = Vec2(int(decomposed[i]), int(decomposed[i+1]))
		bounds_min.x = min(pos.x, bounds_min.x)
		bounds_max.x = max(pos.x, bounds_max.x)
		bounds_max.y = max(pos.y, bounds_max.y)

# Widen bounds
pad = 160
bounds_min.x -= pad
bounds_max.x += pad

# Construct Cave
width, height = bounds_max.x - bounds_min.x + 1, bounds_max.y + 1
height += 2 # Add room for floor
cave = [[e] * width for i in range(height)]

for i, line in enumerate(input_file):

	line = line.rstrip()
	decomposed = re.split(',| -> ', line)
	prev_pos = None

	for i in range(0, len(decomposed), 2): 
		pos = Vec2(int(decomposed[i]), int(decomposed[i+1]))
		pos.x -= bounds_min.x
		if prev_pos != None: 
			if pos.x != prev_pos.x: 
				from_x = min(pos.x, prev_pos.x)
				to_x = max(pos.x, prev_pos.x)
				for x in range(from_x, to_x+1, 1): 
					cave[pos.y][x] = w
			else: 
				from_y = min(pos.y, prev_pos.y)
				to_y = max(pos.y, prev_pos.y)
				for y in range(from_y, to_y+1, 1): 
					cave[y][pos.x] = w
		prev_pos = pos

# Add floor
for i in range(0, len(cave[-1]), 1): 
	cave[-1][i] = w

start_time_ms = round(time.time() * 1000)

sand_spawn_pos = Vec2(500, 0)
sand_spawn_pos.x -= bounds_min.x
sand_to_rest = 0

movement = [
	Vec2(0,1), 
	Vec2(-1,1), 
	Vec2(1,1), 
]

def update_sand(sand):

	def move(x, y): 
		if x < 0 or x >= len(cave[0]): return None # Out of bounds
		elif y < 0 or y >= len(cave): return None # Out of bounds
		else: return cave[y][x] == e
	
	for m in movement: 
		result = move(sand.x + m.x, sand.y + m.y)
		if result == None: 
			return None # Out of bounds
		elif result == True: 
			return m # Valid movement
	return False # No valid movement

def run(): 
	active_sand = None
	global sand_to_rest

	while True: 
		if not active_sand: 
			active_sand = copy.copy(sand_spawn_pos)
		while active_sand != None: 
			result = update_sand(active_sand)
			if result == None: 
				return # Out of bounds
			elif type(result) == Vec2: 
				active_sand += result
			elif result == False: 
				cave[active_sand.y][active_sand.x] = s
				sand_to_rest += 1
				if active_sand.y == sand_spawn_pos.y: 
					return # No movement from spawn
				active_sand = None

run()

for r in cave: 
	print(''.join(r))

print("sand_to_rest:", sand_to_rest)

end_time_ms = round(time.time() * 1000)
print("Time:", end_time_ms - start_time_ms, "ms")
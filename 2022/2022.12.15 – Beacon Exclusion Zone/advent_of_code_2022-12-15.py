
# https://adventofcode.com/2022/day/15

import string
import math
import time
import re
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

sensors = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	line = re.split(" |, |: ", line)
	values = [int(e.split('=')[1]) for e in line if '=' in e]
	sensors.append(values)

start_time_ms = round(time.time() * 1000)

# Calculate bounds
bounds_min = None
bounds_max = None

for s in sensors: 
	x1, y1, x2, y2 = s
	m_distance = abs(x1 - x2) + abs(y1 - y2) # Manhattan Distance
	x1 -= m_distance # Pad for coverage to nearest Beacon
	y1 -= m_distance # Pad for coverage to nearest Beacon
	x2 += m_distance # Pad for coverage to nearest Beacon
	y2 += m_distance # Pad for coverage to nearest Beacon
	if bounds_min == None: 
		bounds_min = Vec2(x1, y1)
		bounds_max = copy.copy(bounds_min)
	bounds_min.x = min(bounds_min.x, min(x1, x2))
	bounds_min.y = min(bounds_min.y, min(y1, y2))
	bounds_max.x = max(bounds_max.x, max(x1, x2))
	bounds_max.y = max(bounds_max.y, max(y1, y2))

print("Bounds:", bounds_min, bounds_max)

# Offset for bounds correction
for s in sensors: 
	s[0] -= bounds_min.x # Sensor X
	s[2] -= bounds_min.x # Beacon X

grid = ['.'] * (bounds_max.x - bounds_min.x + 1)
# target_row = 10
target_row = 2000000

for s in sensors: 
	x1, y1, x2, y2 = s
	m_distance = abs(x1 - x2) + abs(y1 - y2) # Manhattan Distance
	if abs(target_row - y1) > m_distance: 
		continue # Out of range to affect target row
	else: 
		if y1 == target_row: 
			grid[x1] = 'S'
		if y2 == target_row: 
			grid[x2] = 'B'
		overlap = m_distance - abs(target_row - y1)
		for i in range(x1 - overlap, x1 + overlap + 1, 1): 			
			if i >= 0 and i < len(grid): 
				if grid[i] == '.': 
					grid[i] = '#'

print(len([e for e in grid if e == '#']))

end_time_ms = round(time.time() * 1000)

print("Time:", end_time_ms - start_time_ms, "ms")
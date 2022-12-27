
# https://adventofcode.com/2022/day/22

import string
import math
import time
import datetime
import re
from copy import deepcopy

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def get_time_now(): 
	return datetime.datetime.now().strftime("%H:%M:%S")

class Vec2:
	def __init__(self, x, y): 
		self.x = x
		self.y = y
	def __str__(self):
		s = "{0},{1}"
		return s.format(self.x, self.y)
	def __add__(self, v): 
		return Vec2(self.x + v.x, self.y + v.y)

input_file = open('test_input.txt', 'r').readlines()
# input_file = open('input.txt', 'r').readlines()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

board = []
position = None
facing = 'R' # Right/down/left/up — 0/1/2/3
path_raw = None
trail = []

for i, line in enumerate(input_file):

	line = line.rstrip()

	if len(line) == 0: 
		continue

	# Path
	if line[0].isnumeric(): 
		path_raw = line
		continue

	board.append(list(line))

	# Find start position
	if position == None: 
		for y, c in enumerate(line): 
			if c == '.':
				position = Vec2(y, i)
				break

# Prepare path
path = []
start = 0
for end, c in enumerate(path_raw): 
	if not c.isnumeric(): 
		number = path_raw[start:end]
		start = end + 1
		path.append(int(number))
		path.append(c)

	# Catch the last number
	if end == len(path_raw) - 1: 
		path.append(int(number))

def move_horizontal(dist): 
	step = 1 if dist > 0 else -1
	distance_moved = 0
	temp_pos = Vec2(position.x, position.y)
	valid_pos = Vec2(position.x, position.y)
	row_length = len(board[position.y])
	face = get_face(position.x, position.y)

	while distance_moved < abs(dist): 
		temp_pos.x += step
		if temp_pos.x >= row_length: 
			temp_pos.x = 0
		elif temp_pos.x < 0: 
			temp_pos.x = row_length - 1

		tile = board[temp_pos.y][temp_pos.x]

		if tile == '#': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			return valid_pos
		# else: 
		# 	if tile == '.': 
		# 		trail.append([valid_pos.x, valid_pos.y, facing])
		# 		valid_pos.x = temp_pos.x
		# 		distance_moved += 1
		elif tile == '.': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			valid_pos.x = temp_pos.x
			distance_moved += 1
	return valid_pos

def move_vertical(dist): 
	step = 1 if dist > 0 else -1
	distance_moved = 0
	temp_pos = Vec2(position.x, position.y)
	valid_pos = Vec2(position.x, position.y)

	while distance_moved < abs(dist): 
		temp_pos.y += step
		if temp_pos.y >= len(board): 
			temp_pos.y = 0
		elif temp_pos.y < 0: 
			temp_pos.y = len(board) - 1

		if temp_pos.x >= len(board[temp_pos.y]): 
			continue # Row is not long enough

		tile = board[temp_pos.y][temp_pos.x]

		if tile == '#': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			return valid_pos
		elif tile == '.': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			valid_pos.y = temp_pos.y
			distance_moved += 1
	return valid_pos

while len(path) > 0: 

	cmd = path.pop(0)

	if type(cmd) == int: 
		dist = cmd
		if 	 facing == 'R': position = move_horizontal(dist)
		elif facing == 'D': position = move_vertical(dist)
		elif facing == 'L': position = move_horizontal(-dist)
		elif facing == 'U': position = move_vertical(-dist)
	else: 
		if 	 facing == 'R': facing = 'D' if cmd == 'R' else 'U'
		elif facing == 'D': facing = 'L' if cmd == 'R' else 'R'
		elif facing == 'L': facing = 'U' if cmd == 'R' else 'D'
		elif facing == 'U': facing = 'R' if cmd == 'R' else 'L'

# Draw trail
for t in trail: 
	x, y, f = t
	if f == 'R': f = '>'
	elif f == 'D': f = 'v'
	elif f == 'L': f = '<'
	elif f == 'U': f = '^'
	board[y][x] = f

# Print board
for row in board: 
	print(''.join(row))

# End position and facing
print("End:", position, facing)

# Calculate answer
r = (1000 * (position.y + 1))
c = (4 * (position.x + 1))
f = 0
if facing == 'R': f = 0
elif facing == 'D': f = 1
elif facing == 'L': f = 2
elif facing == 'U': f = 3

password = r+c+f
print("password:", password)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
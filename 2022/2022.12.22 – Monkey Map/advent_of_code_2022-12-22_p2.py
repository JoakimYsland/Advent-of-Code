
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
	x = position.x
	valid_x = x
	row_length = len(board[position.y])

	while distance_moved < abs(dist): 
		x += step
		if x >= row_length: 
			x = 0
		elif x < 0: 
			x = row_length - 1
		tile = board[position.y][x]
		if tile == '#': 
			trail.append([valid_x, position.y, facing])
			return valid_x
		elif tile == '.': 
			trail.append([valid_x, position.y, facing])
			valid_x = x
			distance_moved += 1
	return valid_x

def move_vertical(dist): 
	step = 1 if dist > 0 else -1
	distance_moved = 0
	y = position.y
	valid_y = y

	while distance_moved < abs(dist): 
		y += step
		if y >= len(board): 
			y = 0
		elif y < 0: 
			y = len(board) - 1
		if position.x >= len(board[y]): 
			continue # Row is not long enough
		tile = board[y][position.x]
		if tile == '#': 
			trail.append([position.x, valid_y, facing])
			return valid_y
		elif tile == '.': 
			trail.append([position.x, valid_y, facing])
			valid_y = y
			distance_moved += 1
	return valid_y

while len(path) > 0: 

	cmd = path.pop(0)

	if type(cmd) == int: 
		dist = cmd
		if 	 facing == 'R': position.x = move_horizontal(dist)
		elif facing == 'D': position.y = move_vertical(dist)
		elif facing == 'L': position.x = move_horizontal(-dist)
		elif facing == 'U': position.y = move_vertical(-dist)
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

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

# # ————— Test input —————
# input_file = open('test_input.txt', 'r').readlines()
# face_mapping = {
# 	"B3": [Vec2(8,4), Vec2(11,7)], 
# 	"C3": [Vec2(8,0), Vec2(11,3)], 
# 	"A3": [Vec2(8,8), Vec2(11,11)], 
# 	"A4": [Vec2(12,8), Vec2(15,11)], 
# 	"B2": [Vec2(4,4), Vec2(7,7)], 
# 	"B1": [Vec2(0,4), Vec2(3,7)], 
# }

# # Refer to Blender file for IDs
# # The first list defines what sort of rotation 
# # you need to perform after moving to the new face. 
# # The second list defines the seams between them. 
# transpose_mapping = {
# 	"B3R": [['R'], [Vec2(11,4), Vec2(11,7), Vec2(15,8), Vec2(12,8)]], 
# 	"A4U": [['L'], [Vec2(11,4), Vec2(11,7), Vec2(15,8), Vec2(12,8)]], 

# 	"C3R": [['L', 'L'], [Vec2(11,0), Vec2(11,4), Vec2(15,11), Vec2(15,8)]], 
# 	"A4R": [['R', 'R'], [Vec2(11,0), Vec2(11,4), Vec2(15,11), Vec2(15,8)]], 

# 	"A4D": [['L'], [Vec2(12,11), Vec2(15,11), Vec2(0,7), Vec2(0,4)]], 
# 	"B1L": [['R'], [Vec2(12,11), Vec2(15,11), Vec2(0,7), Vec2(0,4)]], 

# 	"C3L": [['L'], [Vec2(8,0), Vec2(8,3), Vec2(4,4), Vec2(7,4)]], 
# 	"B2U": [['R'], [Vec2(8,0), Vec2(8,3), Vec2(4,4), Vec2(7,4)]], 

# 	"C3U": [['L', 'L'], [Vec2(8,0), Vec2(11,0), Vec2(3,4), Vec2(0,4)]], 
# 	"B1U": [['R', 'R'], [Vec2(8,0), Vec2(11,0), Vec2(3,4), Vec2(0,4)]], 

# 	"A3L": [['R'], [Vec2(8,8), Vec2(8,11), Vec2(7,7), Vec2(4,7)]], 
# 	"B2D": [['L'], [Vec2(8,8), Vec2(8,11), Vec2(7,7), Vec2(4,7)]], 

# 	"A3D": [['L', 'L'], [Vec2(8,11), Vec2(11,11), Vec2(3,7), Vec2(0,7)]], 
# 	"B1D": [['R', 'R'], [Vec2(8,11), Vec2(11,11), Vec2(3,7), Vec2(0,7)]], 
# }


# ————— Real input —————
input_file = open('input.txt', 'r').readlines()
face_mapping = {
	"D2": [Vec2(50,0), Vec2(99,49)], 
	"D3": [Vec2(100,0), Vec2(149,49)], 
	"C2": [Vec2(50,50), Vec2(99,99)], 
	"B1": [Vec2(0,100), Vec2(49,149)], 
	"B2": [Vec2(50,100), Vec2(99,149)], 
	"A1": [Vec2(0,150), Vec2(49,199)], 
}

# Refer to Blender file for IDs
# The first list defines what sort of rotation 
# you need to perform after moving to the new face. 
# The second list defines the seams between them. 
transpose_mapping = {
	"D2U": [['R'], [Vec2(50,0), Vec2(99,0), Vec2(0,150), Vec2(0,199)]], 
	"A1L": [['L'], [Vec2(50,0), Vec2(99,0), Vec2(0,150), Vec2(0,199)]], 

	"D2L": [['R', 'R'], [Vec2(50,0), Vec2(50,49), Vec2(0,149), Vec2(0,100)]], 
	"B1L": [['L', 'L'], [Vec2(50,0), Vec2(50,49), Vec2(0,149), Vec2(0,100)]], 

	"D3U": [[], [Vec2(100,0), Vec2(149,0), Vec2(0,199), Vec2(49,199)]], 
	"A1D": [[], [Vec2(100,0), Vec2(149,0), Vec2(0,199), Vec2(49,199)]], 

	"D3R": [['R', 'R'], [Vec2(149,0), Vec2(149,49), Vec2(99,149), Vec2(99,100)]], 
	"B2R": [['L', 'L'], [Vec2(149,0), Vec2(149,49), Vec2(99,149), Vec2(99,100)]],

	"D3D": [['R'], [Vec2(100,49), Vec2(149,49), Vec2(99,50), Vec2(99,99)]], 
	"C2R": [['L'], [Vec2(100,49), Vec2(149,49), Vec2(99,50), Vec2(99,99)]], 

	"C2L": [['L'], [Vec2(50,50), Vec2(50,99), Vec2(0,100), Vec2(49,100)]], 
	"B1U": [['R'], [Vec2(50,50), Vec2(50,99), Vec2(0,100), Vec2(49,100)]], 

	"B2D": [['R'], [Vec2(50,149), Vec2(99,149), Vec2(49,150), Vec2(49,199)]], 
	"A1R": [['L'], [Vec2(50,149), Vec2(99,149), Vec2(49,150), Vec2(49,199)]], 
}

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
if start < len(path_raw): 
	path.append(int(path_raw[start:]))

def get_face(x, y): 
	for k, v in face_mapping.items(): 
		face_min, face_max = v
		if (x >= face_min.x and 
			x <= face_max.x and
			y >= face_min.y and
			y <= face_max.y): 
			return k
	return None

def transpose(x, y, mapping): 

	from1, to1, from2, to2 = mapping
	prt("transpose: ", x, y, "-", from1, "/", to1, "/", from2, "/", to2)

	# On seam 1
	# if x >= from1.x and x <= to1.x and y >= from1.y and y <= to1.y: 
	if (x >= min(from1.x, to1.x) and 
		x <= max(from1.x, to1.x) and 
		y >= min(from1.y, to1.y) and 
		y <= max(from1.y, to1.y)):
		prt("On seam 1")
		# Get offset on seam 1
		if from1.x == to1.x: # Seam 1 is vertical
			offset = abs(y - from1.y)
		else: # Seam 1 is horizontal
			offset = abs(x - from1.x)

		# transpose to seam 2
		if from2.x == to2.x: # Seam 2 is vertical
			prt("transpose to seam 2 (vertical)")
			if from2.y > to2.y: 
				return Vec2(from2.x, from2.y - offset)
			else: 
				return Vec2(from2.x, from2.y + offset)
		else: # Seam 2 is horizontal
			prt("transpose to seam 2 (horizontal)")
			if from2.x > to2.x: 
				return Vec2(from2.x - offset, from2.y)
			else: 
				return Vec2(from2.x + offset, from2.y)

	# On seam 2
	# elif x >= from2.x and x <= to2.x and y >= from2.y and y <= to2.y: 
	elif (x >= min(from2.x, to2.x) and 
		x <= max(from2.x, to2.x) and 
		y >= min(from2.y, to2.y) and 
		y <= max(from2.y, to2.y)): 
		prt("On seam 2")
		# Get offset on seam 2
		if from2.x == to2.x: # Seam 2 is vertical
			offset = abs(y - from2.y)
		else: # Seam 2 is horizontal
			offset = abs(x - from2.x)

		# Transpose to seam 1
		if from1.x == to1.x: # Seam 1 is vertical
			prt("transpose to seam 1 (vertical)")
			if from1.y > to1.y: 
				return Vec2(from1.x, from1.y - offset)
			else: 
				return Vec2(from1.x, from1.y + offset)
		else: # Seam 1 is horizontal
			prt("transpose to seam 1 (horizontal)")
			if from1.x > to1.x: 
				return Vec2(from1.x - offset, from1.y)
			else: 
				return Vec2(from1.x + offset, from1.y)

	else: 
		prt("Something's fucky")

def move_horizontal(dist): 
	
	step = 1 if dist > 0 else -1
	distance_moved = 0
	temp_pos = Vec2(position.x, position.y)
	valid_pos = Vec2(position.x, position.y)
	row_length = len(board[position.y])
	face = get_face(position.x, position.y)

	while distance_moved < abs(dist): 
		temp_pos.x += step

		# Moved to a new face
		face2 = get_face(temp_pos.x, temp_pos.y)
		if face != face2: 
			movement = face + facing
			if movement in transpose_mapping.keys(): 
				temp_pos = deepcopy(valid_pos)
				trail.append([valid_pos.x, valid_pos.y, facing])
				prt("move_horizontal:", temp_pos, valid_pos, movement)
				# Transpose
				mapping = transpose_mapping[movement][1]
				temp_pos = transpose(valid_pos.x, valid_pos.y, mapping)
				prt("temp_pos:", temp_pos)

				if temp_pos == None: 
					draw_board()

				# Check transposed tile
				tile = board[temp_pos.y][temp_pos.x]
				if tile == '.':
					distance_moved += 1
					rotation = transpose_mapping[movement][0]
					path.insert(0, abs(dist) - distance_moved)
					for r in rotation: 
						path.insert(0, r)
					prt("safe move", path[0:len(rotation) + 1])
					prt("—————")
					return temp_pos
		face = get_face(valid_pos.x, valid_pos.y)

		tile = board[temp_pos.y][temp_pos.x]

		if tile == '#': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			return valid_pos
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
	face = get_face(position.x, position.y)

	while distance_moved < abs(dist): 
		temp_pos.y += step

		# Moved to a new face
		face2 = get_face(temp_pos.x, temp_pos.y)
		if face != face2: 
			movement = face + facing
			if movement in transpose_mapping.keys(): 
				temp_pos = deepcopy(valid_pos)
				trail.append([valid_pos.x, valid_pos.y, facing])
				prt("move_vertical:", temp_pos, valid_pos, movement)
				# Transpose
				mapping = transpose_mapping[movement][1]
				temp_pos = transpose(valid_pos.x, valid_pos.y, mapping)
				prt("temp_pos:", temp_pos)

				if temp_pos == None: 
					draw_board()

				# Check transposed tile
				tile = board[temp_pos.y][temp_pos.x]
				if tile == '.':
					distance_moved += 1
					rotation = transpose_mapping[movement][0]
					path.insert(0, abs(dist) - distance_moved)
					for r in rotation: 
						path.insert(0, r)
					prt("safe move", path[0:len(rotation) + 1])
					prt("—————")
					return temp_pos
		face = get_face(valid_pos.x, valid_pos.y)

		tile = board[temp_pos.y][temp_pos.x]

		if tile == '#': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			return valid_pos
		elif tile == '.': 
			trail.append([valid_pos.x, valid_pos.y, facing])
			valid_pos.y = temp_pos.y
			distance_moved += 1
	return valid_pos

def draw_board(): 
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

draw_board()

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
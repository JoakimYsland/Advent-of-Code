
# https://adventofcode.com/2022/day/23

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

class Elf: 
	def __init__(self, x, y): 
		self.x = x
		self.y = y

def print_scan(): 
	for row in scan: 
		r = ""
		for c in row: 
			r += '#' if type(c) == Elf else '.'
		print(r)

def pad(): 
	# Pad scan
	for row in scan: 
		row.insert(0, '.')
		row.insert(len(scan[0]), '.')
	scan.insert(0, ['.' for i in range(len(scan[0]))])
	scan.insert(len(scan), ['.' for i in range(len(scan[0]))])

	# Update elf positions
	for elf in elves: 
		elf.x += 1
		elf.y += 1

def scan_for_elves(elf, pattern): 
	num_elves = 0
	for n in pattern: 
		x, y = n
		tile = scan[elf.y+y][elf.x+x]
		if type(tile) == Elf: 
			num_elves += 1
	return num_elves

def move_elf(elf, x, y): 
	scan[elf.y][elf.x] = '.'
	scan[y][x] = elf
	elf.x = x
	elf.y = y

# Scan pattern
neighbors = [
	[ 0,-1], # N
	[ 1,-1], # NE
	[ 1, 0], # E
	[ 1, 1], # SE
	[ 0, 1], # S
	[-1, 1], # SW
	[-1, 0], # W
	[-1,-1], # NW
]

# Scan pattern
arcs = [
	[[0,-1], [1,-1],  [-1,-1]], # N, NE, NW
	[[0,1],  [1,1],   [-1,1]], # S, SE, SW
	[[-1,0], [-1,-1], [-1,1]], # W, NW, SW
	[[1,0],  [1,-1],  [1,1]], # E, NE, SE
]

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

scan = []
elves = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	# scan.append(list(line))
	scan.append(['.' for i in range(len(line))])
	for x, c in enumerate(line): 
		if c == '#': 
			new_elf = Elf(x, i)
			elves.append(new_elf)
			scan[i][x] = new_elf

# Rounds
for r in range(10): 

	pad()

	proposed_movement = {}

	# First half of the round
	for elf in elves: 
		num_neighbors = scan_for_elves(elf, neighbors)
		if num_neighbors == 0: 
			continue
		for arc in arcs: 
			num_elves = scan_for_elves(elf, arc)
			if num_elves == 0: # No other elves in the arc
				x, y = arc[0] # Cardinal center direction of arc (N,S,E,W)
				k = "{0},{1}".format(elf.x+x, elf.y+y)
				if not k in proposed_movement: 
					proposed_movement[k] = []
				proposed_movement[k].append(elf)
				break # No need to check more arcs
	
	# Second half of the round
	for k, v in proposed_movement.items(): 
		if len(v) > 1: # More than 1 elf wants to move to the position
			continue
		x, y = (int(i) for i in k.split(','))
		elf = v[0]
		move_elf(elf, x, y)

	# Move first arc to the back of the queue
	arcs.insert(len(arcs), arcs.pop(0))

print_scan()

# Calculate bounding box empty tiles
min_x, min_y, max_x, max_y = math.inf, math.inf, 0, 0

for elf in elves: 
	min_x = min(min_x, elf.x)
	min_y = min(min_y, elf.y)
	max_x = max(max_x, elf.x)
	max_y = max(max_y, elf.y)

width = (max_x - min_x) + 1
height = (max_y - min_y) + 1
empty_tiles = (width * height) - len(elves)
print("empty_tiles:", empty_tiles)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
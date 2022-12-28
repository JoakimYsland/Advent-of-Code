
# https://adventofcode.com/2022/day/24

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

class Blizzard: 
	directions = {
		'^': ( 0,-1), 
		'>': ( 1, 0), 
		'v': ( 0, 1), 
		'<': (-1, 0), 
	}

	def __init__(self, x, y, c): 
		self.x = x
		self.y = y
		self.direction = Blizzard.directions[c]
		self.icon = c

	def __str__(self): 
		return self.icon

def print_valley(valley): 
	for row in valley: 
		r = ""
		for c in row: 
			if type(c) == Blizzard: 
				r += str(c)
			else: 
				r += c
		print(r)

def update_blizzards(): 
	for b in blizzards: 

		if valley[b.y][b.x] == b: 
			valley[b.y][b.x] = '.' 

		b.x += b.direction[0]
		b.y += b.direction[1]

		w = len(valley[0])
		h = len(valley)

		# Wrap position
		if b.x > w-2: 	b.x = 1
		if b.x < 1: 	b.x = w-2
		if b.y > h-2: 	b.y = 1
		if b.y < 1: 	b.y = h-2

		valley[b.y][b.x] = b

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

valley = []
blizzards = []
start = None
last_line = None

for i, line in enumerate(input_file):

	line = line.rstrip()
	last_line = line

	row = ['.' for i in range(len(line))]
	valley.append(row)

	for x, c in enumerate(line): 
		if c == '#': 
			valley[i][x] = '#'
		elif c == '.': 
			if i == 0: 
				start = (x, i) # Capture start position
			else: 
				continue
		else: 
			new_blizzard = Blizzard(x, i, c)
			valley[i][x] = new_blizzard
			blizzards.append(new_blizzard)

# Find goal
for i, c in enumerate(last_line): 
	if c == '.': 
		goal = (i, len(valley)-1)

# print_valley(valley)

def get_neighbors(pos): 
	
	x, y = pos
	neighbors = []
	w = len(valley[0])
	h = len(valley)

	if x > 0: 	neighbors.append((x-1, y)) # Left
	if x < w-1: neighbors.append((x+1, y)) # Right
	if y > 0: 	neighbors.append((x, y-1)) # Up
	if y < h-1: neighbors.append((x, y+1)) # Down

	return neighbors

max_idle = 10
max_distance = 20
frontier_x, frontier_y = 0, 0
goals = [goal, start, goal]
progress_string = "[{0}] {1} ({2},{3})"
rounds = 0

def run(start, goal): 

	global frontier_x, frontier_y
	global rounds

	paths = [[deepcopy(start)]]

	while True: 

		update_blizzards()
		rounds += 1

		temp = []
		for path in list(paths): 
			path_id = str(path[-1])
			if path_id in temp: 
				paths.remove(path)
			else: 
				temp.append(path_id)

		# Update paths
		for path in list(paths): 

			if len(path) >= max_idle: 
				# Remove path if it has been stationary for too long
				if len(set(path[len(path)-max_idle:])) == 1: 
					paths.remove(path)
					continue

			# Cull by Manhattan Distance to max
			x, y = path[-1]

			if goal[1] == 0: # Goal is start
				frontier_x = min(frontier_x, x)
				frontier_y = min(frontier_y, y)
			else: 
				frontier_x = max(frontier_x, x)
				frontier_y = max(frontier_y, y)

			if (abs(frontier_x - x) > max_distance or 
				abs(frontier_y - y) > max_distance):
				paths.remove(path)
				continue

			# Create branches for cardinal directions
			for n in get_neighbors(path[-1]): 

				x, y = n

				# The neighbor is occupied
				if valley[y][x] != '.': 
					continue

				if n == goal: 
					print("Goal reached in", len(path), "steps", n)
					return

				# Create branch
				branch = deepcopy(path)
				branch.append((x, y))
				paths.append(branch)

			# Process the root path
			x, y = path[-1]

			if valley[y][x] == '.': 
				path.append(path[-1]) # Continue path by remaining stationary
			else: 
				paths.remove(path) # The stationary position was hit by a blizzard

		print(progress_string.format(len(paths[0]), len(paths), frontier_x, frontier_y))

run(start, goal)
run(goal, start)
run(start, goal)

print("rounds:", rounds)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
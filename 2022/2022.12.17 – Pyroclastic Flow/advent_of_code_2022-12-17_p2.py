
# https://adventofcode.com/2022/day/17

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
	# return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	return datetime.datetime.now().strftime("%H:%M:%S")

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

width, height = 7, 3
cave = []
jet_pattern = []
rocks = [
	["..####."], 

	["...#...", 
	 "..###..", 
	 "...#..."], 

	["....#..", 
	 "....#..", 
	 "..###.."], 

	["..#....", 
	 "..#....", 
	 "..#....",
	 "..#...."], 

	["..##...", 
	 "..##..."], 
]

for i, line in enumerate(input_file):

	line = line.rstrip()
	for char in line: 
		jet_pattern.append(-1 if char == "<" else 1)

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

# Code here
spawned_rocks = 0
tower_height = 0
rock_height = 0
rock_indices = []
jet = True

def spawn_rock(index): 
	global spawned_rocks
	global tower_height
	global rock_height
	global rock_indices
	rock_indices = []
	for i, row in enumerate(rocks[index]): 
		cave.insert(i, row)
		row_indices = []
		for i, c in enumerate(row): 
			if c == '#': 
				row_indices.append(i)
		rock_indices.insert(i, row_indices)
	rock_height = len(rocks[index])
	spawned_rocks += 1
	tower_height += rock_height

def print_cave(cave): 
	for row in cave: 
		print("|", ''.join(row), "|")
	print("+ ––––––– +")

def pad_cave(): 
	existing_padding = 0
	for row in cave: 
		if row == ".......": 
			existing_padding += 1
		else: 
			break
	
	if existing_padding == 3: 
		return
	elif existing_padding < 3:
		extra_padding = 3 - existing_padding
		for i in range(0, extra_padding, 1): 
			cave.insert(0, ".......")
	elif existing_padding > 3: 
		extra_padding = existing_padding - 3
		for i in range(0, extra_padding, 1): 
			cave.pop(0)

def get_jet_collision(jet_right):
	global rock_indices
	for row in rock_indices: 
		if jet_right and 6 in row: # Want to jet right but cannot
			return True
		elif not jet_right and 0 in row: # Want to jet left but cannot
			return True
	return False

jet_index = 0
culled_height = 0
rock_at_rest = False
run = True
# total_rocks = 1000000000000
total_rocks = 1000000
progress = "{0}% ({1})"

pad_cave()
spawn_rock(0)

while run: 

	if rock_at_rest:

		if spawned_rocks < total_rocks: 

			# OPTIMISATION: If the tower has a full line, 
			# we can safely remove that line and everything below
			for y, row in enumerate(cave): 
				if row == "#######": 
					culled_height += len(cave) - y
					cave = cave[0:y]
					break 

			pad_cave()
			spawn_rock(spawned_rocks % len(rocks))
			rock_at_rest = False

			if spawned_rocks % (total_rocks / 100) == 0: 
				p = (spawned_rocks / total_rocks) * 100
				print(progress.format(int(p), len(cave)))

		else: 
			run = False
			break

	if jet: 

		jet_right = jet_pattern[jet_index] == 1

		if not get_jet_collision(jet_right): 

			temp_cave = cave[0:len(rock_indices)] # Temp cave from rows relevant for collision
			pebbles_before = ''.join(temp_cave).count('#')

			# Remove rock
			for y, row in enumerate(rock_indices): 
				for x in row: 
					temp_cave[y] = temp_cave[y][:x] + '.' + temp_cave[y][x+1:]

			displacement = 1 if jet_right else -1
			# Recreate rock with displacement
			for y, row in enumerate(rock_indices): 
				for x in row: 
					temp_cave[y] = temp_cave[y][:x+displacement] + '#' + temp_cave[y][x+displacement+1:]

			pebbles_after = ''.join(temp_cave).count('#')

			# No collision
			if pebbles_after == pebbles_before: 
				# Apply displacement for cave
				for y, row in enumerate(temp_cave): 
					cave[y] = row
				# Apply displacement for rock_indices
				for row in rock_indices: 
					for i in range(0, len(row), 1):
						row[i] += displacement

		jet_index = (jet_index + 1) % len(jet_pattern)

	else: 

		rock_bottom = len(rock_indices) # Index of row below active rock

		if rock_bottom > len(cave) - 1: 
			rock_at_rest = True # Hit bottom
			
		elif cave[rock_bottom] == ".......": 
			# Row below rock is empty. Pop n' drop
			cave.pop(rock_bottom) 
			
		else: 
			temp_cave = cave[0:len(rock_indices) + 1] # Temp cave from rows relevant for collision
			pebbles_before = ''.join(temp_cave).count('#')

			# Remove rock
			for y, row in enumerate(rock_indices): 
				for x in row: 
					temp_cave[y] = temp_cave[y][:x] + '.' + temp_cave[y][x+1:]

			# Recreate rock one step down
			for y, row in enumerate(rock_indices): 
				for x in row: 
					temp_cave[y+1] = temp_cave[y+1][:x] + '#' + temp_cave[y+1][x+1:]
			
			pebbles_after = ''.join(temp_cave).count('#')
			
			if pebbles_after < pebbles_before: 
				# Collision
				rock_at_rest = True
			else: 
				# Apply drop
				for y, new_row in enumerate(temp_cave): 
					cave[y] = new_row
				# Offset rock_indices to compensate for drop
				rock_indices.insert(0, [])

	jet = not jet

pad_cave()
# print_cave(cave)

print("tower_height:", len(cave) + culled_height - 3) # Subtract padding
print("spawned_rocks:", spawned_rocks)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
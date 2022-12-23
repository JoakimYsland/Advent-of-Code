
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

def cull_cave():
	global cave
	global culled_height
	# OPTIMISATION: If the tower has a full line, 
	# we can safely remove that line and everything below
	for y, row in enumerate(cave): 
		if row == "#######": 
			culled_height += len(cave) - y
			cave = cave[0:y]
			return 

jet_index = 0
culled_height = 0
rock_at_rest = False
run = True
total_rocks = 1000000000000
# 1799999999990
# 1514285714288
# total_rocks = 1000000 # => 59587 ms
# total_rocks = 100000 # => 152838 / 5997 ms
# total_rocks = 10000 # => 15282 / 647 ms
# total_rocks = 2022
progress = "{0}% ({1})"

pad_cave()
spawn_rock(0)

jet_cycles = 0

# 1739 rocks in initial cycle
# 1730 rocks per whole cycle (10090 jets)
# 1381 rocks in the final cycle

# 2342 rows in the initial cycle
# 2644 new rows per cycle
# 29 rows in the final cycle

# test = 0
cycle0_rocks = 0
cycle0_height = 0

cycle1_rocks = 0
cycle1_height = 0
num_mid_cycles = 0

cycle_last_rocks = 0
calculated_height = 0

test = 0

while run: 

	# if jet_index == 0 and spawned_rocks > 1: 
	# 	if jet_cycles == 4: # 13253
	# 		pad_cave()
	# 		print(len(cave)-3)
	# 	jet_cycles += 1

	if jet_index == 0 and spawned_rocks > 1: 

		pad_cave()

		if jet_cycles == 0: 
			cycle0_rocks = spawned_rocks
			cycle0_height = len(cave) - 3
		elif jet_cycles == 1: 
			cycle1_rocks = spawned_rocks
			cycle1_height = len(cave) - 3
			
			cycle1_rocks_delta = cycle1_rocks - cycle0_rocks
			cycle1_height_delta = cycle1_height - cycle0_height

			num_mid_cycles = int((total_rocks - cycle0_rocks) / cycle1_rocks_delta)
			cycle_last_rocks = total_rocks - cycle0_rocks - (num_mid_cycles * cycle1_rocks_delta)
			
			print("—————")
			print("cycle0_rocks:", cycle0_rocks)
			print("cycle0_height:", cycle0_height)
			print("cycle1_rocks:", cycle1_rocks)
			print("cycle1_height:", cycle1_height)
			print("cycle1_rocks_delta:", cycle1_rocks_delta)
			print("cycle1_height_delta:", cycle1_height_delta)
			print("num_mid_cycles:", num_mid_cycles, ((total_rocks - cycle0_rocks) / cycle1_rocks_delta))
			print("cycle_last_rocks:", cycle_last_rocks)
			print("—————")

			# Jump forward in time
			spawned_rocks = cycle0_rocks + (num_mid_cycles * cycle1_rocks_delta)

		jet_cycles += 1

	if rock_at_rest:

		# if test == spawned_rocks: 
		# 	print(rock_indices)
		# 	print(spawned_rocks)
		# 	print_cave(cave[0:10])

		if spawned_rocks < total_rocks: 

			# cull_cave()

			pad_cave()
			spawn_rock(spawned_rocks % len(rocks))
			rock_at_rest = False

			# if spawned_rocks % (total_rocks / 100) == 0: 
			# 	p = (spawned_rocks / total_rocks) * 100
			# 	print(progress.format(int(p), len(cave)))

		else: 
			run = False
			break

	# ===== JET =====

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

	# ===== DROP =====

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

pad_cave()
# print_cave(cave)

# print(num_mid_cycles)
# print((cycle1_height - cycle0_height))
cycles_mid_height = num_mid_cycles * (cycle1_height - cycle0_height)
cycles_last_height = (len(cave) - 3) - cycle1_height
calculated_height = cycle0_height + cycles_mid_height + cycles_last_height
# 15282

print("tower_height:", len(cave) + culled_height - 3) # Subtract padding
print("calculated_height:", calculated_height)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
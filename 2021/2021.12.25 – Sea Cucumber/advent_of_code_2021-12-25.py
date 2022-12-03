
# https://adventofcode.com/2021/day/25

import time
import math
import re
from copy import deepcopy

def run(run_title, input_file):

	def visualize_cucumbers(): 
		print('-----')
		for row in cucumbers: 
			print(str(row).replace('\'', '').replace(',', ''))

	def update_cucumbers(): 
		nonlocal cucumbers

		def move_herd(c_type): 
			moved = False
			c_copy = deepcopy(cucumbers)
			rows = len(c_copy)
			columns = len(c_copy[0])
			for y in range(0, rows): 
				for x in range(0, columns): 
					if c_copy[y][x] != c_type: 
						continue

					if c_type == '>': 
						a_x, a_y = (x + 1) % columns, y
					else: 
						a_x, a_y = x, (y + 1) % rows
					
					if c_copy[a_y][a_x] == '.': 
						cucumbers[y][x] = '.'
						cucumbers[a_y][a_x] = c_type
						moved = True
			
			return moved

		moved_h = move_herd('>')
		moved_v = move_herd('v')

		return moved_h or moved_v

	# --------------------------------------------------------------------------------

	# Test / Real – 58 / 329

	start_time_ms = round(time.time() * 1000)
	steps = 0
	cucumbers = []
	
	for line in input_file: 
		cucumbers.append([])
		for c in [c for c in line.strip()]: 
			cucumbers[-1].append(c)

	moved = True
	while moved: 
		moved = update_cucumbers()
		steps += 1
		if steps % 10 == 0: 
			print('step', steps)

	# visualize_cucumbers()

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "steps:", steps, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
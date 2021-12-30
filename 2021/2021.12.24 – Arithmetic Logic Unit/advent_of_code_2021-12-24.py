
# https://adventofcode.com/2021/day/24

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def inp(split): 
		a = split[1]
		loc = get_write_location(a)
		ALU[loc] = inps.pop(0)

	def add(): 
		print('add')

	def mul(): 
		print('mul')

	def div(): 
		print('div')

	def mod(): 
		print('mod')

	def eql(): 
		print('eql')
	
	def get_write_location(location): 
		if location == 'x': return 0
		if location == 'y': return 1
		if location == 'z': return 2
		if location == 'w': return 3
	
	def get_b(b) : 
		if b.isdigit(): 
			return int(b)
		else: 
			loc_b = get_write_location(b)
			return ALU[loc_b]

	# --------------------------------------------------------------------------------

	# Test / Real – 44169 / !47191

	start_time_ms = round(time.time() * 1000)

	# ALU = { 'x': 0, 'y': 0, 'z': 0, 'w': 0 }
	ALU = [0,0,0,0]
	instructions = {
		'inp': inp, 
		'add': add, 
		'mul': mul, 
		'div': div, 
		'mod': mod, 
		'eql': eql, 
	}
	inps = [7]

	for line in input_file: 
		split = line.strip().split()
		instruction = split[0]

		if instruction == 'inp': 
			# a = split[1]
			# loc = get_write_location(a)
			# ALU[loc] = inps.pop(0)
			instructions[instruction](split)

		elif instruction == 'add': 
			a, b = split[1], get_b(split[2])
			loc_a = get_write_location(a)
			ALU[loc_a] = b + ALU[loc_a]

		elif instruction == 'mul': 
			a, b = split[1], get_b(split[2])
			loc = get_write_location(a)
			ALU[loc] *= b

		elif instruction == 'div': 
			a, b = split[1], get_b(split[2])
			loc_a = get_write_location(a)
			ALU[loc_a] = int(ALU[loc_a] / b)

		elif instruction == 'mod': 
			a, b = split[1], get_b(split[2])
			loc_a = get_write_location(a)
			ALU[loc_a] = ALU[loc_a] % b

		elif instruction == 'eql': 
			a, b = split[1], get_b(split[2])
			loc_a = get_write_location(a)
			is_equal = ALU[loc_a] == b
			ALU[loc_a] = 1 if is_equal else 0

	# burrow_init = [['', '', '', '', '', '', '', '', '', '', '']] # Hallway (0 - left, 10 - right)
	# # movement_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
	# # total_cost = 0

	# # -1-3-5-7-9-
	# #   C B D D  => A B C D
	# #   D C B A  => A B C D
	# #   D B A C  => A B C D
	# #   B C A A  => A B C D
	# burrow_init.append(['C', 'D', 'D', 'B']) # Room 1 (0 - top, 1 - bottom)
	# burrow_init.append(['B', 'C', 'B', 'C']) # Room 1 (0 - top, 1 - bottom)
	# burrow_init.append(['D', 'B', 'A', 'A']) # Room 1 (0 - top, 1 - bottom)
	# burrow_init.append(['D', 'A', 'C', 'A']) # Room 1 (0 - top, 1 - bottom)

	# lowest_score = 999999
	# valid_hallway = [0,1,3,5,7,9,10]

	# def try_stuff(burr, score): 

	# 	nonlocal lowest_score
	# 	if score >= lowest_score: 
	# 		return

	# 	# Enter
	# 	for i in valid_hallway: 
	# 		if burr[0][i] == '': 
	# 				continue
	# 		for j in range(1, 5): 
	# 			b = deepcopy(burr)
	# 			success, cost = enter(i,j, b)
	# 			if success == True: 
	# 				new_score = score + cost
	# 				if new_score < lowest_score: 
	# 					is_complete = len(''.join(b[0])) == 0
	# 					if is_complete: 
	# 						lowest_score = new_score
	# 						print('lowest_score', lowest_score)
	# 					else: 
	# 						try_stuff(b, new_score)
				
	# 	# Leave
	# 	for j in valid_hallway: 
	# 		if burr[0][j] != '': 
	# 				continue
	# 		for i in range(1, 5): 
	# 			b = deepcopy(burr)
	# 			success, cost = leave(i,j, b)
	# 			if success == True: 
	# 				new_score = score + cost
	# 				if new_score < lowest_score: 
	# 					try_stuff(b, new_score)
	
	# try_stuff(burrow_init, 0)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "ALU:", ALU, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
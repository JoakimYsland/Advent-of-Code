
# https://adventofcode.com/2021/day/24

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

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

	def inp(split): 
		a = split[1]
		loc_a = get_write_location(a)
		ALU[loc_a] = inps.pop(0)

	def add(split): 
		a, b = split[1], get_b(split[2])
		loc_a = get_write_location(a)
		ALU[loc_a] = b + ALU[loc_a]

	def mul(split): 
		a, b = split[1], get_b(split[2])
		loc = get_write_location(a)
		ALU[loc] *= b

	def div(split): 
		a, b = split[1], get_b(split[2])
		loc_a = get_write_location(a)
		ALU[loc_a] = int(ALU[loc_a] / b)

	def mod(split): 
		a, b = split[1], get_b(split[2])
		loc_a = get_write_location(a)
		ALU[loc_a] = ALU[loc_a] % b

	def eql(split): 
		a, b = split[1], get_b(split[2])
		loc_a = get_write_location(a)
		is_equal = ALU[loc_a] == b
		ALU[loc_a] = 1 if is_equal else 0

	# --------------------------------------------------------------------------------

	# Test / Real – ??? / ???

	start_time_ms = round(time.time() * 1000)

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

		instructions[instruction](split)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "ALU:", ALU, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
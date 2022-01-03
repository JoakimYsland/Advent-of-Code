
# https://adventofcode.com/2021/day/24

import time
import math
import re
from copy import deepcopy

def run(run_title, input_file):

	def get_write_location(location): 
		if location == 'x': return 0
		if location == 'y': return 1
		if location == 'z': return 2
		if location == 'w': return 3
	
	def get_b(b) : 
		if b.isdigit() or b.startswith('-'): 
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
		loc_a = get_write_location(a)
		ALU[loc_a] *= b

	def div(split): 
		a, b = split[1], get_b(split[2])
		loc_a = get_write_location(a)
		ALU[loc_a] = ALU[loc_a] // b

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
	
	valid_model_number = False
	ALU = [0,0,0,0]
	instructions = {
		'inp': inp, 
		'add': add, 
		'mul': mul, 
		'div': div, 
		'mod': mod, 
		'eql': eql, 
	}
	inps = []

	numbers = [
		# XX964696999889
		# 964696999889
		92997999999999
	]

	def my_print(*args, **kwargs):
		# print(' '.join(map(str,args)), **kwargs)
		return

	temp = []
	connecting_numbers = []

	c_nums = [0]

	def run_instructions(number, z=0): 
		nonlocal inps
		nonlocal ALU
		inps = [int(d) for d in str(number)]
		ALU = [0,0,z,0]

		for i, line in enumerate(input_file): 
			if line.startswith('#'): 
				continue
			if len(line) <= 1: 
				# my_print('---')
				continue
			split = line.strip().split()
			instruction = split[0]
			instructions[instruction](split)

	# ==================================================
	# NEW TEST 2022.01.02 – 2
	# ==================================================

	# Manually check each cycle, starting with the last. 

	# For the last cycle (14) c_nums_15.txt contains '0', 
	# meaning that we want cycle 14 to output a Z value of '0'
	# Then we try all combinations of 'inp w' numbers 1-9 and 
	# existing Z-values 0-2000000 (coming into the cycle as 
	# output from the previous one) and record which combinations 
	# produce the desired output Z-value. 

	# Then we move on to cycle 13 but instead of wanting an 
	# output Z-value of '0', we want an output Z-value that 
	# was found when checking cycle 14, meaning any combination of 
	# 'inp w' number and existing Z-values 0-2000000 that will produce 
	# an output Z-value of '0' in the 14th cycle. 

	f = open('c_nums_15.txt', 'r').readlines()
	c_nums = [int(n) for n in f[0].strip().split(', ')]

	for n in range(1, 10): 
		print(n)
		for j in range(0, 2000000): 
			run_instructions(n, j)
			valid_model_number = True if ALU[2] in c_nums else False
			if valid_model_number: 
				# print(run_title, "ALU:", ALU, n, j, '----- VALID -----')
				if not j in temp: 
					temp.append(j)

	f = open('c_nums_1.txt', 'a')
	f.write(str(temp).replace('[', '').replace(']', ''))
	f.close()

	# ==================================================
	# CONTINUATION 2022.01.03
	# ==================================================

	# Manually check each cycle, starting with the first. 

	# For cycle 1, we have an input Z-value of '0', as recorded in 
	# 'c_nums_1.txt'. We run all numbers in this file (only '0' for cycle 1)
	# in combination with all desired Z-values in 'c_nums_2.txt' and see 
	# which number 1-9 produces a desired output Z-value. 
	# There is only 1 valid number, '9', which produces an output Z-value of
	# '12' so the first digit in the valid model number is '9'

	# 92967699949891

	run_instructions(92967699949891)
	print(ALU)
	return

	f_in  = open('c_nums_14.txt', 'r').readlines() # 1
	f_out = open('c_nums_15.txt', 'r').readlines() # 2
	c_nums_in  = [int(n) for n in f_in[0].strip().split(', ')]
	c_nums_out = [int(n) for n in f_out[0].strip().split(', ')]

	for n in range(9, 0, -1): 
		for c_num_in in c_nums_in: 
			run_instructions(n, c_num_in)
			if ALU[2] in c_nums_out: 
				print(n, ALU[2])

	# end_time_ms = round(time.time() * 1000)
	# total_time = end_time_ms - start_time_ms

	# print(run_title, "ALU:", ALU, ('(' + str(total_time) + "ms)"))
	# print(run_title, "valid_model_number:", valid_model_number, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
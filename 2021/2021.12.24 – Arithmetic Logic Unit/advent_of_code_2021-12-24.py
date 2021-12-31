
# https://adventofcode.com/2021/day/24

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

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
	# inps = [7] # [1, 1, 1, 0]
	# inps = [1,3,5,7,9,2,4,6,8,9,9,9,9,9]
	# number = 99999999999999
	# number = 11111111111111
	# number = 13579246899999
	numbers = [
		11111111111111, 
		22222222222222, 
		33333333333333, 
		44444444444444, 
		55555555555555, 
		66666666666666, 
		77777777777777, 
		88888888888888, 
		99999999999999, 
		13579246899999, 
		76687718179891, 
		73826491827356, 
		91287892173649, 
		82376487676572, 
		67347847676857, 
		86921367984678, 
		91423789614327, 
		86959782713487, 
		59817236487265, 
		81723647826358, 
		19354917864586, 
		48716934914941, 
		94196154914865, 
		98461759678496, 
		78542139867946, 
		81379817234917, 
		36917846917451, 
		92746579149696, 
		84948617369186, 
		41285468971494, 
	]

	# 15 => add y 3 [1, 12, 0, 9]
	# 16 => mul y x [1, 4, 0, 1]
	# 17 => add z y [1, 4, 4, 1]

	irrelevant_instructions = []

	def run_instructions(number): 
		nonlocal inps
		nonlocal ALU
		inps = [int(d) for d in str(number)]
		ALU = [0,0,0,0]

		irrelevant_instructions.append([])

		for i, line in enumerate(input_file): 
			if line.startswith('#'): 
				continue
			split = line.strip().split()
			instruction = split[0]
			init = ALU[2]
			instructions[instruction](split)
			if ALU[2] == init and instruction != 'inp': 
				# irrelevant_instructions[-1].append(str(i) + ': ' + line.strip())
				irrelevant_instructions[-1].append('# ' + line.strip())
			else: 
				irrelevant_instructions[-1].append(line.strip())
			# my_print(i, '=>', line.strip(), ALU)

		# valid_model_number = True if ALU[2] == 0 else False
		
		# end_time_ms = round(time.time() * 1000)
		# total_time = end_time_ms - start_time_ms

		# print(run_title, "ALU:", ALU, ('(' + str(total_time) + "ms)"))
		# print(run_title, "valid_model_number:", valid_model_number, ('(' + str(total_time) + "ms)"))

	for n in numbers: 
		run_instructions(n)

	for e in irrelevant_instructions[0]: 
		print(e)

	# while number > 10000000000000: 
	# 	# my_print(number)
	# 	inps = [int(d) for d in str(number)]
	# 	for i, line in enumerate(input_file): 
	# 		# my_print(i, '=>', line.strip())
	# 		split = line.strip().split()
	# 		instruction = split[0]
	# 		instructions[instruction](split)
		
	# 	valid_model_number = True if ALU[2] == 0 else False
	# 	if valid_model_number == True: 
	# 		break

	# 	number -= 1
	# 	while '0' in str(number) or number in blacklist: 
	# 		number -= 1

	# end_time_ms = round(time.time() * 1000)
	# total_time = end_time_ms - start_time_ms

	# print(run_title, "ALU:", ALU, ('(' + str(total_time) + "ms)"))
	# print(run_title, "valid_model_number:", valid_model_number, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
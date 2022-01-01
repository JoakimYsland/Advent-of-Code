
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
		# 11111111111111, 
		# 22222222222222, 
		# 33333333333333, 
		# 44444444444444, 
		# 55555555555555, 
		# 66666666666666, 
		# 77777777777777, 
		# 88888888888888, 
		# 99999999999999, 
		# 13579246899999, 
		# 76687718179891, 
		# 73826491827356, 
		# 91287892173649, 
		# 82376487676572, 
		# 67347847676857, 
		# 86921367984678, 
		# 91423789614327, 
		# 86959782713487, 
		# 59817236487265, 
		# 81723647826358, 
		# 19354917864586, 
		# 48716934914941, 
		# 94196154914865, 
		# 98461759678496, 
		# 78542139867946, 
		# 81379817234917, 
		# 36917846917451, 
		# 92746579149696, 
		# 84948617369186, 
		# 41285468971494, 

		# 19999999999999, 
		# 91999999999999, 
		# 99199999999999, 
		# 99919999999999, 
		# 99991999999999, 
		# 99999199999999, 
		# 99999919999999, 
		# 99999991999999, 
		# 99999999199999, 
		# 99999999919999, 
		# 99999999991999, 
		# 99999999999199, 
		# 99999999999919, 
		# 99999999999991, 

		# # 99999999999119, 
		# # 99999999999123, 
		# 11223344556677, 
		# 11221122112211, 
		# 99119911991199, 
		# 11991199119911, 
		# 12345678912345, 
		# 12121212121212, 
		# 13131313131313, 
		# 14141414141414, 
		# 15151515151515, 
		# 16161616161616, 
		# 17171717171717, 
		# 18181818181818, 
		# 19191919191919, 
		
		# 12345678912345, 
		# 12345678912349, 
		# 12345678912399, 
		# 12345678912999, 
		# 12345678919999, 
		# 12345678999999, 
		# 12345679999999, 
		# 12345699999999, 
		# 12345999999999, 
		# 12349999999999, 
		# 12399999999999, 
		# 12999999999999, 
		# 19999999999999, 
		# 99999999999999, 

		# 11111111111189, 
		# 22222222222289, 
		# 33333333333389, 
		# 44444444444489, 
		# 55555555555589, 
		# 66666666666689, 
		# 77777777777789, 
		# 88888888888889, 
		99999999999989, 
		# 89898989898989, 
		# 98989898989889, 
		# 26262626262689, 
		
		# 11, 
		# 1, 2, 3, 4, 5, 6, 7, 8, 9, 
		# 11, 22, 33, 44, 55, 66, 77, 88, 99, 
		# 12, 13, 14, 15, 16, 17, 18, 19, 
		# 21, 31, 41, 51, 61, 71, 81, 91, 
		# 12, 24, 36, 48, 21, 42, 63, 84, 
		# 1221, 2112, 1289
	]

	# x Has to be 0 because: 
	# mul y x
	# add z y
	# XXXXXXXXXXXX-89-
	# X 0 is the key

	# inp w      [0, 0, 0, 1]
	# ...
	# mul z y    [1, 26, 104, 1]
	# mul y 0    [1, 0, 104, 1]
	# add y w    [1, 1, 104, 1]
	# add y 3    [1, 4, 104, 1]
	# mul y x    [1, 4, 104, 1]
	# add z y    [1, 4, 108, 1]

	def run_instructions(number): 
		nonlocal inps
		nonlocal ALU
		inps = [int(d) for d in str(number)]
		ALU = [0,0,0,0]

		for i, line in enumerate(input_file): 
			if line.startswith('#'): 
				continue
			if len(line) <= 1: 
				my_print('---')
				continue
			split = line.strip().split()
			instruction = split[0]
			instructions[instruction](split)
			# my_print(i, '=>', line.strip(), ALU)
			# my_print(line.strip(), ALU)
			my_print(line.strip().ljust(10, ' '), ALU)

		# valid_model_number = True if ALU[2] == 0 else False
		
		
		# print(run_title, "valid_model_number:", valid_model_number, ('(' + str(total_time) + "ms)"))

	for i, n in enumerate(numbers): 
		run_instructions(n)

		end_time_ms = round(time.time() * 1000)
		total_time = end_time_ms - start_time_ms
		total_time_str = '(' + str(total_time) + 'ms)'

		print(run_title, "ALU:", ALU, total_time_str, n)

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
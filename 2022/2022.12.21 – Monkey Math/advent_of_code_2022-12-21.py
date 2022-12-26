
# https://adventofcode.com/2022/day/21

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

class Monkey: 
	def __init__(self, name): 
		self.name = name
		self.base_value = None
		self.ref_monkey_1 = None
		self.ref_monkey_2 = None
		self.get_math_operation = None
	def get_value(self): 
		if self.base_value != None: 
			return self.base_value
		else: 
			return int(self.get_math_operation())
	def get_ref_values(self): 
		v1 = monkeys[self.ref_monkey_1].get_value()
		v2 = monkeys[self.ref_monkey_2].get_value()
		return v1, v2
	def get_math_plus(self): 
		v1, v2 = self.get_ref_values()
		return v1 + v2
	def get_math_minus(self): 
		v1, v2 = self.get_ref_values()
		return v1 - v2
	def get_math_mult(self): 
		v1, v2 = self.get_ref_values()
		return v1 * v2
	def get_math_div(self): 
		v1, v2 = self.get_ref_values()
		return v1 / v2

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

monkeys = {}

for i, line in enumerate(input_file):

	line = line.rstrip()
	line = re.split(" |: ", line)

	name = line[0]
	new_monkey = Monkey(name)
	monkeys[name] = new_monkey

	# Monkey with base number
	if len(line) == 2: 
		new_monkey.base_value = int(line[1])

	# Monkey references other monkeys
	elif len(line) == 4: 
		new_monkey.ref_monkey_1 = line[1]
		new_monkey.ref_monkey_2 = line[3]

		if line[2] == '+': 
			new_monkey.get_math_operation = new_monkey.get_math_plus
		elif line[2] == '-': 
			new_monkey.get_math_operation = new_monkey.get_math_minus
		elif line[2] == '*': 
			new_monkey.get_math_operation = new_monkey.get_math_mult
		elif line[2] == '/': 
			new_monkey.get_math_operation = new_monkey.get_math_div

riddle_answer = monkeys["root"].get_value()
print("riddle_answer:", riddle_answer)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
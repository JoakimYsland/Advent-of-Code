
# https://adventofcode.com/2022/day/11

import string
import math
import re

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

monkeys = []

class Monkey: 
	items = None
	operator = None
	operator_value = None
	test = None
	true = None
	false = None
	inspections = 0

	def op_multiply(self, worry_level): 
		return worry_level * self.operator_value
	
	def op_old_multiply(self, worry_level): 
		return worry_level * worry_level
	
	def op_add(self, worry_level): 
		return worry_level + self.operator_value

def play_round(): 
	for m in monkeys: 
		for item in m.items: 
			item = m.operator(item)
			item = int(item / 3) # Relief
			if item % m.test == 0: 
				monkeys[m.true].items.append(item)
			else: 
				monkeys[m.false].items.append(item)
			m.inspections += 1
		m.items.clear()

for line in input_file:

	line = line.rstrip()
	line = line.lstrip()

	if line.startswith("Monkey"): 
		new_monkey = Monkey()
		monkeys.append(new_monkey)

	elif line.startswith("Starting items"): 
		temp = re.split(' |,', line)
		monkeys[-1].items = [int(i) for i in temp if i.isnumeric()]

	elif line.startswith("Operation"): 
		temp = re.split(' ', line)
		sign = temp[-2]
		value = temp[-1]

		if sign == "*": 
			monkeys[-1].operator = monkeys[-1].op_multiply
		elif sign == "+": 
			monkeys[-1].operator = monkeys[-1].op_add

		if value.isnumeric(): 
			monkeys[-1].operator_value = int(value)
		elif value == "old": 
			monkeys[-1].operator = monkeys[-1].op_old_multiply

	elif line.startswith("Test"): 
		temp = re.split(' ', line)
		monkeys[-1].test = int(temp[-1])

	elif line.startswith("If true"): 
		temp = re.split(' ', line)
		monkeys[-1].true = int(temp[-1])

	elif line.startswith("If false"): 
		temp = re.split(' ', line)
		monkeys[-1].false = int(temp[-1])

for i in range(0, 20, 1): 
	play_round()

num_inspections_list = [m.inspections for m in monkeys]
num_inspections_list.sort(reverse=True)
monkey_business = num_inspections_list[0] * num_inspections_list[1]
print("monkey_business:", monkey_business)
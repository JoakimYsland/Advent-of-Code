
# https://adventofcode.com/2022/day/13

import string
import math
import time
import re
import ast

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

packet_data = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	if len(line) > 0:
		packet_data.append(ast.literal_eval(line))

def asd(left, right): 
	i = 0
	while i < len(left) and i < len(right): 

		prt("Compare", left[i], "vs", right[i])

		# If both values are ints, the lower int should come first
		if type(left[i]) == int and type(right[i]) == int: 
			if left[i] < right[i]: 
				return True
			elif left[i] > right[i]: 
				return False

		# If both values are lists, compare each pair of ints
		elif type(left[i]) == list and type(right[i]) == list: 
			result = asd(left[i], right[i])
			if result != None: 
				return result

		# If only one value is an int, convert it to a list
		else: 
			prt(" – Mixed types; convert to list")
			if type(left[i]) == int: 
				result = asd([left[i]], right[i])
				if result != None: 
					return result
			elif type(right[i]) == int: 
				result = asd(left[i], [right[i]])
				if result != None: 
					return result

		i += 1

	# If the left list runs out of items first, 
	# the inputs are in the right order
	if len(left) < len(right): 
		prt(" – Left side ran out of items")
		return True
	elif len(left) > len(right): 
		prt(" – Right side ran out of items")
		return False
	else: 
		return None

start_time_ms = round(time.time() * 1000)

right_order_pair_indices = []

for p in range(0, len(packet_data), 2): 
	left = packet_data[p]
	right = packet_data[p+1]
	pair_index = int((p / 2) + 0.5) + 1

	right_order = asd(left, right)
	prt("Pair", pair_index, "in the right order:", right_order, "\n")
	
	if right_order: 
		right_order_pair_indices.append(pair_index)

sum_right_order_pair_indices = sum(right_order_pair_indices)
print("sum_right_order_pair_indices:", sum_right_order_pair_indices)

end_time_ms = round(time.time() * 1000)

print("Time:", end_time_ms - start_time_ms, "ms")
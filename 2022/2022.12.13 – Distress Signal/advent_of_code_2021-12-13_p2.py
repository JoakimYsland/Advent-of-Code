
# https://adventofcode.com/2022/day/13

import string
import math
import time
import re
import ast
import functools

def prt(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

packet_data = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	if len(line) > 0:
		packet_data.append(ast.literal_eval(line))

div_packet_1 = [[2]]
div_packet_2 = [[6]]

packet_data.append(div_packet_1)
packet_data.append(div_packet_2)

def compare_packets(left, right): 
	i = 0
	while i < len(left) and i < len(right): 

		prt("Compare", left[i], "vs", right[i])

		# If both values are ints, the lower int should come first
		if type(left[i]) == int and type(right[i]) == int: 
			if left[i] < right[i]: 
				return 1 #True
			elif left[i] > right[i]: 
				return -1 #False

		# If both values are lists, compare each pair of ints
		elif type(left[i]) == list and type(right[i]) == list: 
			result = compare_packets(left[i], right[i])
			if result != None: 
				return result

		# If only one value is an int, convert it to a list
		else: 
			prt(" – Mixed types; convert to list")
			if type(left[i]) == int: 
				result = compare_packets([left[i]], right[i])
				if result != None: 
					return result
			elif type(right[i]) == int: 
				result = compare_packets(left[i], [right[i]])
				if result != None: 
					return result

		i += 1

	# If the left list runs out of items first, 
	# the inputs are in the right order
	if len(left) < len(right): 
		prt(" – Left side ran out of items")
		return 1 #True
	elif len(left) > len(right): 
		prt(" – Right side ran out of items")
		return -1 #False
	else: 
		return None

start_time_ms = round(time.time() * 1000)
			
packet_data.sort(key=functools.cmp_to_key(compare_packets), reverse=True)

index_div_packet_1 = None
index_div_packet_2 = None

for i, p in enumerate(packet_data): 
	if p == div_packet_1: 
		index_div_packet_1 = i + 1
	if p == div_packet_2: 
		index_div_packet_2 = i + 1

decoder_key = index_div_packet_1 * index_div_packet_2
print("decoder_key:", decoder_key)

end_time_ms = round(time.time() * 1000)

print("Time:", end_time_ms - start_time_ms, "ms")
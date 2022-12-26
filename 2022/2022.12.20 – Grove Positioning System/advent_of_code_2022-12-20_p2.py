
# https://adventofcode.com/2022/day/20

import string
import math
import time
import datetime
import re
from copy import deepcopy
from collections import namedtuple

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def get_time_now(): 
	return datetime.datetime.now().strftime("%H:%M:%S")

class Number: 
	def __init__(self, index, value, mixed): 
		self.initial_index = index
		self.value = value
		self.mixed = mixed
	def __str__(self): 
		s = "[{0}] {1}, {2}"
		return s.format(self.initial_index, self.value, self.mixed)

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

device_file = []

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

for i, line in enumerate(input_file):

	line = line.rstrip()
	device_file.append(Number(i, int(line), False))

def print_sequence(): 
	numbers = []
	for n in device_file: 
		numbers.append(str(n.value))
	print(', '.join(numbers))

def get_nth(i): 
	i %= len(device_file)
	return device_file[i]

def mix():
	num_mixes = 0
	target_index = 0
	while num_mixes < len(device_file): 
		for i, number in enumerate(device_file): 

			# Only mix each number once
			if number.mixed == True: 
				continue

			if number.initial_index != target_index: 
				continue
			
			target_index += 1
			num_mixes += 1

			# No need to do mixing if the number is 0
			if number.value == 0: 
				number.mixed = True
				continue

			# Do the mixing
			n = device_file.pop(i)
			n.mixed = True
			new_index = (i + number.value) % len(device_file)
			device_file.insert(new_index, n)

			# Debug text
			# s = "{0} moves between {1} and {2} ({3})"
			# left = device_file[(new_index-1) % len(device_file)].value
			# right = device_file[(new_index+1) % len(device_file)].value
			# print(s.format(n.value, left, right, new_index))
			# print_sequence()

			# Only mix 1 number at a time
			break

	# Reset mixing status
	for n in device_file: 
		n.mixed = False

# Apply decryption key
for n in device_file: 
	n.value *= 811589153 # Decryption key

for i in range(0, 10, 1): 
	mix()
	# print_sequence()

# Get index of '0' value
zero_index = None
for i, n in enumerate(device_file): 
	if n.value == 0: 
		zero_index = i
		break

# Find answer
key_numbers = [1000, 2000, 3000]
for i, n in enumerate(key_numbers): 
	key_numbers[i] = get_nth(n + zero_index).value
answer = sum(key_numbers)

print("key_numbers:", key_numbers)
print("answer:", answer)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
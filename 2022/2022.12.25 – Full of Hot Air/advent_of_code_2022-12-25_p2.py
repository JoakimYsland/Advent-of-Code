
# https://adventofcode.com/2022/day/25

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

decimal_table = []
for i in range(30):
	decimal_table.append(pow(5, i))
snafu_table = {
	'2': 2, 
	'1': 1, 
	'0': 0, 
	'-': -1, 
	'=': -2, 
}

def to_decimal(snafu): 
	decimal = 0
	elements = list(snafu)
	elements.reverse()
	for i, e in enumerate(elements): 
		decimal += decimal_table[i] * snafu_table[e]
	return decimal

# [1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125, 9765625, 48828125, 244140625]
def to_snafu(decimal): 

	# Convert decimal to base 5
	base5 = []
	while decimal > 0:
		base5.append(int(decimal % 5))
		decimal = int(decimal / 5)
	
	# If value is > 2, carry over 1 and subtract 5. 
	# Example: 0,3 (0,15) becomes 0,-2,1 (0,-10,25)
	for i in range(0, len(base5), 1): 
		if base5[i] >= 3: 
			if i >= len(base5) - 1: 
				base5.append(0) # Pad if necessary
			base5[i+1] += 1
			base5[i] -= 5

	base5.reverse()

	# Convert adjusted base5 to snafu
	for i in range(0, len(base5)): 
		if base5[i] == -2: 
			base5[i] = '='
		elif base5[i] == -1: 
			base5[i] = '-'
		else: 
			base5[i] = str(base5[i])
	
	return ''.join(base5)

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

decimals = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	decimals.append(to_decimal(line))

sum_decimals = sum(decimals)
sum_snafu = to_snafu(sum_decimals)

print("sum:", sum_decimals)
print("sum_snafu:", sum_snafu)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
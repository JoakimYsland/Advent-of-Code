
# https://adventofcode.com/2022/day/6

import string

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

buffer = ""
marker_length = 4

for line in input_file:

	line = line.rstrip()

	for i in range(marker_length - 1, len(line), 1): 
		seq = line[i-(marker_length - 1):i+1]
		is_marker = len(set(seq)) == len(seq)
		if is_marker:
			print(seq, i + 1)
			break
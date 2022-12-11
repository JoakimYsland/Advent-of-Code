
# https://adventofcode.com/2022/day/10

import string
import math

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

x = 1
cycle = 1
interesting_signal_strengths = []
previous_ISS_cycle = -20
interval = 40
CRT = [['.'] * 40 for i in range(6)] # 40x6 pixels

def update_CTR(cycle, x): 
	crt_x = (cycle - 1) % 40
	crt_y = int((cycle - 1) / 40)
	if x >= (crt_x - 1) and x <= (crt_x + 1): 
		CRT[crt_y][crt_x] = '█'

for line in input_file:

	line = line.rstrip()

	if line == "noop": 
		update_CTR(cycle, x)
		cycle += 1
	else: 
		for i in range(0, 2, 1): 
			update_CTR(cycle, x)
			cycle += 1
		init_x = x
		x += int(line.split(' ')[1])

		if cycle > previous_ISS_cycle + interval: 
			rounded_cycle = int(cycle / 10) * 10
			signal_strength = rounded_cycle * init_x # x before add
			interesting_signal_strengths.append(signal_strength)
			previous_ISS_cycle = rounded_cycle
		elif cycle == previous_ISS_cycle + interval: 
			signal_strength = cycle * x
			interesting_signal_strengths.append(signal_strength)
			previous_ISS_cycle = cycle

for row in CRT: 
	print(''.join(row))
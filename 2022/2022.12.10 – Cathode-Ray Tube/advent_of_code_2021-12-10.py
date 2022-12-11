
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

for line in input_file:

	line = line.rstrip()

	if line == "noop": 
		cycle += 1
	else: 
		cycle += 2
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

print("interesting_signal_strengths:", interesting_signal_strengths)
print("sum:", sum(interesting_signal_strengths))
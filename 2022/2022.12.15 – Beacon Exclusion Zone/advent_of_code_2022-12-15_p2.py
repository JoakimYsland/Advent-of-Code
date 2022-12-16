
# https://adventofcode.com/2022/day/15

import string
import math
import time
import re
import copy

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

# input_file, boundary = open('test_input.txt', 'r').readlines(), 20
input_file, boundary = open('input.txt', 'r').readlines(), 4000000

sensors = []

for i, line in enumerate(input_file):

	line = line.rstrip()
	line = re.split(" |, |: ", line)
	values = [int(e.split('=')[1]) for e in line if '=' in e]
	sensors.append(values)

start_time_ms = round(time.time() * 1000)

for y in range(0, boundary, 1): 

	coverage = []

	# Collect coverages
	for s in sensors: 
		x1, y1, x2, y2 = s
		m_distance = abs(x1 - x2) + abs(y1 - y2) # Manhattan Distance to beacon
		if abs(y - y1) > m_distance: 
			continue # Out of range to affect current row
		else: 
			# Calculate number of cells where the 
			# current row intersects the sensor coverage
			overlap = m_distance - abs(y - y1) 
			from_x = x1 - overlap
			to_x = x1 + overlap + 1
			coverage.append(max(from_x, 0)) # Crop to possible Distress Beacon range
			coverage.append(min(to_x, boundary)) # Crop to possible Distress Beacon range

	# Merge coverages so that they do not overlap
	found_overlap = True
	while found_overlap: 
		found_overlap = False
		for a in range(0, len(coverage), 2): 
			from_a, to_a = coverage[a], coverage[a+1]
			for b in range(0, len(coverage), 2): 
				if a == b: 
					continue # Don't check against self
				from_b, to_b = coverage[b], coverage[b+1]
				if from_a <= to_b and from_b <= to_a: # Overlap check
					found_overlap = True
					coverage[a] = min(from_a, from_b) # Expand coverage A
					coverage[a+1] = max(to_a, to_b) # Expand coverage A
					del coverage[b:b+2] # Delete coverage B
					break
			if found_overlap == True: 
				break

	# Sum coverage
	total_coverage = 0
	for i in range(0, len(coverage), 2): 
		f, t = coverage[i], coverage[i+1]
		total_coverage += t-f
	
	# Find Distress Beacon
	if total_coverage < boundary: 
		for i in range(0, len(coverage), 2): 
			f, t = coverage[i], coverage[i+1]
			if t != 0: # We assume that the first valid coverage is the left-most
				tuning_frequency = (t * 4000000) + y
				print("Distress Beacon at:", t, y)
				print("tuning_frequency:", tuning_frequency)
				break
		break # Break main loop

end_time_ms = round(time.time() * 1000)

print("Time:", end_time_ms - start_time_ms, "ms")

# https://adventofcode.com/2021/day/22

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def get_cuboid_volume(cuboid): 
		if None in cuboid[1] or None in cuboid[2]: 
			return 0
		volume = (cuboid[2][0] - cuboid[1][0] + 1) * \
				 (cuboid[2][1] - cuboid[1][1] + 1) * \
				 (cuboid[2][2] - cuboid[1][2] + 1)
		return volume if volume > 0 else 0

	def get_intersection(cuboid_a, cuboid_b): 
		a_min, a_max = cuboid_a[1], cuboid_a[2]
		b_min, b_max = cuboid_b[1], cuboid_b[2]
		i_min = [None, None, None]
		i_max = [None, None, None]

		for i in range(0, 3):
			if a_max[i] >= b_min[i] and a_min[i] <= b_min[i]: 
				i_max[i] = min(a_max[i], b_max[i])
				i_min[i] = max(a_min[i], b_min[i])
			elif a_max[i] >= b_max[i] and a_min[i] >= b_min[i]: 
				i_max[i] = min(a_max[i], b_max[i])
				i_min[i] = max(a_min[i], b_min[i])
			elif a_max[i] <= b_max[i] and a_min[i] >= b_min[i]: 
				i_max[i] = min(a_max[i], b_max[i])
				i_min[i] = max(a_min[i], b_min[i])
			elif a_max[i] >= b_max[i] and a_min[i] <= b_min[i]: 
				i_max[i] = min(a_max[i], b_max[i])
				i_min[i] = max(a_min[i], b_min[i])

		return i_min, i_max

	# --------------------------------------------------------------------------------

	# Test / Real – 2758514936282235 / ???
	# 				2913162407580289

	start_time_ms = round(time.time() * 1000)
	
	cuboids = []
	cuboids_dict = {}
	# init_procedure_area = ['init_procedure_area', [-50, -50, -50], [50, 50, 50]]

	for line in input_file: 
		if line.startswith('#'): 
			continue
		split = [x for x in line.strip().replace('x=', '').replace(',y=', ' ').replace(',z=', ' ').replace('..', ' ').split(' ')]
		for i in range(1, len(split)): 
			split[i] = int(split[i])
		c_min = [split[1], split[3], split[5]]
		c_max = [split[2], split[4], split[6]]
		new_cuboid = [split[0], c_min, c_max]
		cuboids.append(new_cuboid)

	while len(cuboids) > 0: 
		next_cuboid = cuboids.pop(0)
		for cuboid in deepcopy(cuboids_dict).values(): 
			i_min, i_max = get_intersection(next_cuboid, cuboid[0])
			new_cuboid_name = 'on' if cuboid[0][0] == 'off' else 'off'
			new_cuboid = [new_cuboid_name, i_min, i_max]
			new_cuboid_key = str(new_cuboid)
			if new_cuboid_key in cuboids_dict.keys(): 
				cuboids_dict[new_cuboid_key][1] += cuboid[1]
			else: 
				i_volume = get_cuboid_volume(new_cuboid)
				if i_volume > 0: 
					cuboids_dict[new_cuboid_key] = [new_cuboid, cuboid[1]]
		if next_cuboid[0] != 'off': 
			next_cuboid_key = str(next_cuboid)
			cuboids_dict.setdefault(next_cuboid_key, [next_cuboid, 0])
			cuboids_dict[next_cuboid_key][1] += 1

	# for k,v in cuboids_dict.items(): 
	# 	print(v)
	# print(len(cuboids_dict))

	cubes_on = 0
	for cuboid in cuboids_dict.values(): 
		instruction, c_min, c_max = cuboid[0]
		if instruction == 'on': 
			cubes_on += get_cuboid_volume(cuboid[0]) * cuboid[1]
		elif instruction == 'off': 
			cubes_on -= get_cuboid_volume(cuboid[0]) * cuboid[1]

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "cubes_on:", cubes_on, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
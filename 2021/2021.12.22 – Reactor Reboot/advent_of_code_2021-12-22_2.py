
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
			if a_max[i] < b_min[i] or a_min[i] > b_max[i]: 
				return None, None
			else: 
				i_max[i] = min(a_max[i], b_max[i])
				i_min[i] = max(a_min[i], b_min[i])

		return i_min, i_max

	# --------------------------------------------------------------------------------

	# Test / Real – 2758514936282235 / 1285677377848549

	start_time_ms = round(time.time() * 1000)
	
	cuboids = []

	for line in input_file: 
		split = [x for x in line.strip().replace('x=', '').replace(',y=', ' ').replace(',z=', ' ').replace('..', ' ').split(' ')]
		for i in range(1, len(split)): 
			split[i] = int(split[i])
		c_min = [split[1], split[3], split[5]]
		c_max = [split[2], split[4], split[6]]
		new_cuboid = [split[0], c_min, c_max]
		cuboids.append(new_cuboid)

	cuboids_dict = {}
	while len(cuboids) > 0: 
		print(len(cuboids))
		next_cuboid = cuboids.pop(0)

		for cuboid in deepcopy(cuboids_dict).values(): 
			i_min, i_max = get_intersection(next_cuboid, cuboid[0])
			if i_min == None or i_max == None: 
				continue
			mod = 1 if cuboid[0][0] == 'off' else -1
			new_cuboid = ['intersection', i_min, i_max]
			new_cuboid_key = str(new_cuboid)
			cuboids_dict.setdefault(new_cuboid_key, [new_cuboid, 0])
			cuboids_dict[new_cuboid_key][1] += cuboid[1] * mod

		cuboids_dict = { k:v for k, v in cuboids_dict.items() if v[1] != 0 }
					
		if next_cuboid[0] != 'off': 
			next_cuboid_key = str(next_cuboid)
			cuboids_dict.setdefault(next_cuboid_key, [next_cuboid, 0])
			cuboids_dict[next_cuboid_key][1] += 1

	print('len(cuboids_dict):', len(cuboids_dict))

	cubes_on = 0
	for cuboid in cuboids_dict.values(): 
		cubes_on += get_cuboid_volume(cuboid[0]) * cuboid[1]

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "cubes_on:", cubes_on, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
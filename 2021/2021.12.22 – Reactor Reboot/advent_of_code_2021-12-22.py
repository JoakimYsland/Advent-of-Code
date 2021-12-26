
# https://adventofcode.com/2021/day/22

import time
import math
import re
from copy import deepcopy
# from collections import deque

# class Vec3: 
# 	def __init__(self, x, y, z): 
# 		self.x = x
# 		self.y = y
# 		self.z = z

# 	def __repr__(self): 
# 		return "({0},{1},{2})".format(str(self.x), str(self.y), str(self.z))

# 	# def __add__(self, other):
# 	# 	return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

# 	def __sub__(self, other):
# 		return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def get_cube_list(cuboid): 
		cube_list = []
		c_min, c_max = cuboid[1], cuboid[2]
		for x in range(c_min[0], c_max[0] + 1): 
			for y in range(c_min[1], c_max[1] + 1): 
				for z in range(c_min[2], c_max[2] + 1): 
					cube_list.append((x,y,z))
		return cube_list

	def get_cuboid_volume(cuboid): 
		c_min, c_max = cuboid[1], cuboid[2]
		for i in range(0, 3):
			if (c_min[i] == None) or \
			   (c_max[i] == None): 
				return 0
		volume = (c_max[0] - c_min[0] + 1) * \
				 (c_max[1] - c_min[1] + 1) * \
				 (c_max[2] - c_min[2] + 1)
		return volume if volume > 0 else 0

	def get_intersection(cuboid_a, cuboid_b): 
		a_min, a_max = cuboid_a[1], cuboid_a[2]
		b_min, b_max = cuboid_b[1], cuboid_b[2]
		i_min = [None, None, None]
		i_max = [None, None, None]

		for i in range(0, 3):
			if a_max[i] > b_min[i] and a_min[i] < b_min[i]: 
				i_max[i] = a_max[i]
				i_min[i] = b_min[i]
			elif a_max[i] > b_max[i] and a_min[i] > b_min[i]: 
				i_max[i] = b_max[i]
				i_min[i] = a_min[i]
			elif a_max[i] < b_max[i] and a_min[i] > b_min[i]: 
				i_max[i] = a_max[i]
				i_min[i] = a_min[i]
			elif a_max[i] > b_max[i] and a_min[i] < b_min[i]: 
				i_max[i] = b_max[i]
				i_min[i] = b_min[i]

		return i_min, i_max

	# --------------------------------------------------------------------------------

	# Test / Real – 590784 / ???

	start_time_ms = round(time.time() * 1000)
	
	cuboids = []
	reactor = {}
	init_procedure_area = ['init_procedure_area', [-50, -50, -50], [50, 50, 50]]

	for line in input_file: 
		split = [x for x in line.strip().replace('x=', '').replace(',y=', ' ').replace(',z=', ' ').replace('..', ' ').split(' ')]
		for i in range(1, len(split)): 
			split[i] = int(split[i])
		c_min = [split[1], split[3], split[5]]
		c_max = [split[2], split[4], split[6]]
		new_cuboid = [split[0], c_min, c_max]

		i_min, i_max = get_intersection(new_cuboid, init_procedure_area)
		i_volume = get_cuboid_volume(['intersection', i_min, i_max])
		if i_volume > 0: 
			cuboids.append(new_cuboid)

	for cuboid in cuboids: 
		instruction, c_min, c_max = cuboid
		cube_list = get_cube_list(cuboid)
		if instruction == 'on': 
			for cube in cube_list: 
				reactor[cube] = 1
		elif instruction == 'off': 
			for cube in cube_list: 
				if cube in reactor: 
					reactor[cube] = 0

	cubes_on = len([c for c in reactor.values() if c == 1])

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "cubes_on:", cubes_on, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
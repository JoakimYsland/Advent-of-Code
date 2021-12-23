
# https://adventofcode.com/2021/day/18

# import re
import time
import math
from copy import deepcopy
# from collections import namedtuple

# Vec3 = namedtuple("Vec3", ['x', 'y', 'z'])

class Vec3: 
	def __init__(self, x, y, z): 
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self): 
		return "({0},{1},{2})".format(str(self.x), str(self.y), str(self.z))

	def __sub__(self, other):
		return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

	def __abs__(self):
		return Vec3(abs(self.x), abs(self.y), abs(self.z))

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def get_axis_permutations(vec3): 
		x, y, z = vec3.x, vec3.y, vec3.z
		return [
			# Foward, Right, Up
			Vec3( x,-z, y), 
			Vec3(-z,-x, y), 
			Vec3(-x, z, y), 
			Vec3( z, x, y), 

			Vec3(-y,-z, x), 
			Vec3(-z, y, x), 
			Vec3( y, z, x), 
			Vec3( z,-y, x), 

			Vec3( x, y, z), 
			Vec3( y,-x, z), 
			Vec3(-x,-y, z), 
			Vec3(-y, x, z), 

			Vec3( x, z,-y), 
			Vec3( z,-x,-y), 
			Vec3(-x,-z,-y), 
			Vec3(-z, x,-y), 

			Vec3( z, y,-x), 
			Vec3( y,-z,-x), 
			Vec3(-z,-y,-x), 
			Vec3(-y, z,-x), 

			Vec3( x,-y,-z), 
			Vec3(-y,-x,-z), 
			Vec3(-x, y,-z), 
			Vec3( y, x,-z), 
		]

	def intersect_scanners(a, b): 
		offsets = {}
		for beacon_a in a:
			permutations = get_axis_permutations(beacon_a)
			for beacon_b in b: 
				for beacon_perm in permutations: 
					offset = str(beacon_perm - beacon_b)
					offsets.setdefault(offset, 0)
					offsets[offset] += 1

		for offset, count in offsets.items(): 
			if count >= 12: 
				print(offset, count)
				return offset
		return None

	# --------------------------------------------------------------------------------

	# Test / Real – 3993 / 4837

	start_time_ms = round(time.time() * 1000)
	
	scanners = []

	for line in input_file: 
		if len(line) < 2: 
			continue
		if line.startswith('---'): 
			scanners.append([])
		else: 
			x,y,z = (int(c) for c in line.strip().split(','))
			scanners[-1].append(Vec3(x,y,z))

	beacons = {}

	for i in range(0, len(scanners)): 
		for j in range(i, len(scanners)):
			if i == j: 
				continue

			print('Comparing', i, 'and', j)
			offset = intersect_scanners(scanners[i], scanners[j])


			# for b1 in scanners[i]:
			# 	permutations = get_axis_permutations(b1)
			# 	for b2 in scanners[j]: 
			# 		for b in permutations: 
			# 			offset = str(b - b2)
			# 			offsets.setdefault(offset, 0)
			# 			offsets[offset] += 1

			# for offset, count in offsets.items(): 
			# 	if count > 2: 
			# 		print(offset, count)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	# print('––––––––––')
	# print(run_title, "highest_magnitude:", highest_magnitude, ('(' + str(total_time) + "ms)"))
	# print('––––––––––')

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
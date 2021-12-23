
# https://adventofcode.com/2021/day/19

import time
import math
import re
from copy import deepcopy

class Vec3: 
	def __init__(self, x, y, z): 
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self): 
		return "({0},{1},{2})".format(str(self.x), str(self.y), str(self.z))

	def __add__(self, other):
		return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

	def __sub__(self, other):
		return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

	def __abs__(self):
		return Vec3(abs(self.x), abs(self.y), abs(self.z))

	# def __neg__(self):
	# 	return Vec3(-self.x, -self.y, -self.z)

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def get_axis_permutations(vec3): 
		x,y,z = vec3.x, vec3.y, vec3.z
		return [
			# Foward, Right, Up
			Vec3( x,-z, y), # 0
			Vec3(-z,-x, y), 
			Vec3(-x, z, y), 
			Vec3( z, x, y), 
			Vec3(-y,-z, x), # 4
			Vec3(-z, y, x), 
			Vec3( y, z, x), 
			Vec3( z,-y, x), 
			Vec3( x, y, z), # 8
			Vec3( y,-x, z), 
			Vec3(-x,-y, z), 
			Vec3(-y, x, z), 
			Vec3( x, z,-y), # 12
			Vec3( z,-x,-y), 
			Vec3(-x,-z,-y), 
			Vec3(-z, x,-y), 
			Vec3( z, y,-x), # 16
			Vec3( y,-z,-x), 
			Vec3(-z,-y,-x), 
			Vec3(-y, z,-x), 
			Vec3( x,-y,-z), # 20
			Vec3(-y,-x,-z), 
			Vec3(-x, y,-z), 
			Vec3( y, x,-z), 
		]

	def intersect_scanners(a, b): 
		offsets = {}
		# for beacon_a in a:
		for beacon_b in b:
			permutations = get_axis_permutations(beacon_b)
			# for beacon_b in b: 
			for beacon_a in a: 
				for i, beacon_perm in enumerate(permutations): 
					# offset = str(beacon_perm - beacon_b)
					# offset = str(beacon_a - beacon_perm)
					offset = beacon_a - beacon_perm
					k = str(offset)
					offsets.setdefault(k, 0)
					offsets[k] += 1
					if offsets[k] >= 12: 
						print(i)
						return offset

		return None

	def map_scanner_graph(): 

		def traverse(scanner_id, total_offset): 
			visited.append(scanner_id)
			offsets[scanner_id] = total_offset

			for s in scanner_graph[scanner_id]: 
				if not s[0] in visited: 
					traverse(s[0], deepcopy(total_offset) + s[1])

		total_offset = Vec3(0,0,0)
		visited = []
		traverse('0', total_offset)

	# --------------------------------------------------------------------------------

	# Test / Real – ??? / ???

	start_time_ms = round(time.time() * 1000)
	
	scanners = []
	beacons = {}
	offsets = {}
	scanner_graph = {}

	for line in input_file: 
		if len(line) < 2: 
			continue
		if line.startswith('---'): 
			scanners.append([])
		else: 
			x,y,z = (int(c) for c in line.strip().split(','))
			scanners[-1].append(Vec3(x,y,z))

	for i in range(0, len(scanners)): 
		# for j in range(i, len(scanners)): 
		for j in range(0, len(scanners)): 
			if i == j: 
				continue

			offset = intersect_scanners(scanners[i], scanners[j])
			if offset != None: 
				print("Offset from Scanner {0} to Scanner {1} is {2}".format(i, j, offset))
				scanner_graph.setdefault(str(i), [])
				# scanner_graph.setdefault(str(j), [])
				scanner_graph[str(i)].append((str(j), offset))
				# scanner_graph[str(j)].append((str(i), -offset))

	map_scanner_graph()

	for i, scanner in enumerate(scanners): 
		for beacon in scanner: 
			p = beacon + offsets[str(i)]
			beacons.setdefault(str(p), 1)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	print(run_title, "beacons:", len(beacons), ('(' + str(total_time) + "ms)"))
	print('––––––––––')

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
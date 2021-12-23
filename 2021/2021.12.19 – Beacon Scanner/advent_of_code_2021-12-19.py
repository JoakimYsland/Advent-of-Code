
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

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def get_axis_permutation(v, i): 
		if i == 0:  return Vec3( v.x,-v.z, v.y) # 0
		if i == 1:  return Vec3(-v.z,-v.x, v.y) 
		if i == 2:  return Vec3(-v.x, v.z, v.y) 
		if i == 3:  return Vec3( v.z, v.x, v.y) 
		if i == 4:  return Vec3(-v.y,-v.z, v.x) # 4
		if i == 5:  return Vec3(-v.z, v.y, v.x) 
		if i == 6:  return Vec3( v.y, v.z, v.x) 
		if i == 7:  return Vec3( v.z,-v.y, v.x) 
		if i == 8:  return Vec3( v.x, v.y, v.z) # 8
		if i == 9:  return Vec3( v.y,-v.x, v.z) 
		if i == 10: return Vec3(-v.x,-v.y, v.z) 
		if i == 11: return Vec3(-v.y, v.x, v.z) 
		if i == 12: return Vec3( v.x, v.z,-v.y) # 12
		if i == 13: return Vec3( v.z,-v.x,-v.y) 
		if i == 14: return Vec3(-v.x,-v.z,-v.y) 
		if i == 15: return Vec3(-v.z, v.x,-v.y) 
		if i == 16: return Vec3( v.z, v.y,-v.x) # 16
		if i == 17: return Vec3( v.y,-v.z,-v.x) 
		if i == 18: return Vec3(-v.z,-v.y,-v.x) 
		if i == 19: return Vec3(-v.y, v.z,-v.x) 
		if i == 20: return Vec3( v.x,-v.y,-v.z) # 20
		if i == 21: return Vec3(-v.y,-v.x,-v.z) 
		if i == 22: return Vec3(-v.x, v.y,-v.z) 
		if i == 23: return Vec3( v.y, v.x,-v.z) 
		return None

	def get_axis_permutations(v): 
		permutations = []
		for i in range(0, 24):
			permutations.append(get_axis_permutation(v, i))
		return permutations

	def intersect_scanners(a, b): 
		offsets = {}
		for beacon_b in b:
			permutations = get_axis_permutations(beacon_b)
			for beacon_a in a: 
				for i, beacon_perm in enumerate(permutations): 
					offset = beacon_a - beacon_perm
					k = str(offset)
					offsets.setdefault(k, 0)
					offsets[k] += 1
					if offsets[k] >= 12: 
						return offset, i

		return None

	def map_scanner_offsets(): 
		
		def traverse(scanner_id, offset): 
			visited.append(scanner_id)
			offsets[scanner_id] = offset

			if scanner_id in scanner_graph: 
				for s in scanner_graph[scanner_id]: 
					if not s[0] in visited: 
						traverse(s[0], offset + s[1])

		visited = []
		traverse('0', Vec3(0,0,0))

	def correct_scanner_rotations(): 
		
		def traverse(i):
			corrected.append(str(i))
			for j in range(0, len(scanners)): 
				if i == j or str(j) in corrected: 
					continue

				result = intersect_scanners(scanners[i], scanners[j])
				if result != None: 
					print("Correcting from {0} onto {1}".format(i, j))
					offset, permutation = result
					intersecting_scanners.append((i, j))
					for k in range(0, len(scanners[j])): 
						scanners[j][k] = get_axis_permutation(scanners[j][k], permutation)
					traverse(j)

		corrected = []
		traverse(0)

	# --------------------------------------------------------------------------------

	# Test / Real – 79 / ???

	start_time_ms = round(time.time() * 1000)
	
	scanners = []
	offsets = {}
	scanner_graph = {}
	intersecting_scanners = []

	for line in input_file: 
		if len(line) < 2: 
			continue
		if line.startswith('---'): 
			scanners.append([])
		else: 
			x,y,z = (int(c) for c in line.strip().split(','))
			scanners[-1].append(Vec3(x,y,z))

	correct_scanner_rotations()

	for s1, s2 in intersecting_scanners: 
		result = intersect_scanners(scanners[s1], scanners[s2])
		if result != None: 
			offset, permutation = result
			text = "Offset from Scanner {0} to Scanner {1} is {2} (permutation {3})"
			print(text.format(s1, s2, offset, permutation))
			scanner_graph.setdefault(str(s1), [])
			scanner_graph[str(s1)].append((str(s2), offset))
	
	map_scanner_offsets()

	beacons = {}
	for i, scanner in enumerate(scanners): 
		for beacon in scanner: 
			p = beacon + offsets[str(i)]
			beacons.setdefault(str(p), 1)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	print(run_title, "beacons:", len(beacons), ('(' + str(total_time) + "ms)"))
	print('––––––––––')

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
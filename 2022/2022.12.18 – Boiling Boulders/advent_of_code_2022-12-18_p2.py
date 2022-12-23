
# https://adventofcode.com/2022/day/18

import string
import math
import time
import datetime
import re
from copy import deepcopy

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def get_time_now(): 
	# return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	return datetime.datetime.now().strftime("%H:%M:%S")

class Vec3:
	def __init__(self, x, y, z): 
		self.x = x
		self.y = y
		self.z = z
	def __str__(self):
		s = "{0},{1},{2}"
		return s.format(self.x, self.y, self.z)
	def __add__(self, v): 
		return Vec2(self.x + v.x, self.y + v.y, self.z + v.z)

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

adjacent = [
	[ 1, 0, 0], 
	[-1, 0, 0], 
	[ 0, 1, 0], 
	[ 0,-1, 0], 
	[ 0, 0, 1], 
	[ 0, 0,-1], 
]
s = "{0},{1},{2}"
droplets = {}

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

bounds_min = Vec3(9999,9999,9999)
bounds_max = Vec3(0,0,0)

# Get bounds
padding = 1
for i, line in enumerate(input_file):

	line = line.rstrip()
	x, y, z = (int(i) for i in line.split(','))
	bounds_min.x = min(bounds_min.x, x - padding)
	bounds_min.y = min(bounds_min.y, y - padding)
	bounds_min.z = min(bounds_min.z, z - padding)
	bounds_max.x = max(bounds_max.x, x + padding)
	bounds_max.y = max(bounds_max.y, y + padding)
	bounds_max.z = max(bounds_max.z, z + padding)

print("Bounds:", bounds_min, "—", bounds_max)

for i, line in enumerate(input_file):

	line = line.rstrip()
	x, y, z = (int(i) for i in line.split(','))
	new_cube = Vec3(x, y, z)
	droplets[str(new_cube)] = 6
	
	for i in range(0, 6, 1): 
		temp = [new_cube.x, new_cube.y, new_cube.z]
		for j in range(0, 3, 1): 
			temp[j] += adjacent[i][j]
		neighbor = s.format(temp[0], temp[1], temp[2])
		if neighbor in droplets.keys(): 
			droplets[neighbor] -= 1
			droplets[str(new_cube)] -= 1

traverse_sides = 0

def Traverse():

	global traverse_sides
	queue = [bounds_min]
	visited = []

	while len(queue) > 0: 

		vec = queue.pop(0)

		if str(vec) in visited: 
			continue

		visited.append(str(vec))

		for i in range(0, 6, 1): 
			neighbor = [vec.x, vec.y, vec.z]
			for j in range(0, 3, 1): 
				neighbor[j] += adjacent[i][j]
			
			neighbor = Vec3(neighbor[0], neighbor[1], neighbor[2])

			if str(neighbor) in visited: 
				continue # Already visited
			
			if (neighbor.x < bounds_min.x or 
				neighbor.y < bounds_min.y or
				neighbor.z < bounds_min.z or
				neighbor.x > bounds_max.x or
				neighbor.y > bounds_max.y or
				neighbor.z > bounds_max.z): 
				visited.append(str(neighbor))
				continue # Out of bounds
			
			if str(neighbor) in droplets.keys(): 
				traverse_sides += 1
			else: 
				queue.append(neighbor)

	print("visited:", len(visited))

Traverse()

sum_sides = sum(droplets.values())
print("sum_sides:", sum_sides)
print("traverse_sides:", traverse_sides)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
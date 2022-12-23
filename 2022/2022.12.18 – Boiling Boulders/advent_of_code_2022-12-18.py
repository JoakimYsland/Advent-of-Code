
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

sum_sides = sum(droplets.values())
print("sum_sides:", sum_sides)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
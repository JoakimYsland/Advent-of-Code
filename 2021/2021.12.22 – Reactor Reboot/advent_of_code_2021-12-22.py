
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

	def get_cuboid_volume(cuboid): 
		c_min, c_max = cuboid[1], cuboid[2]
		for i in range(0, 3):
			if (c_min[i] == None) or \
			   (c_max[i] == None): 
				return 0
		return (c_max[0] - c_min[0] + 1) * \
			   (c_max[1] - c_min[1] + 1) * \
			   (c_max[2] - c_min[2] + 1)

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

		print(i_min, i_max)
		return get_cuboid_volume(['intersection', i_min, i_max])

	# --------------------------------------------------------------------------------

	# Test / Real – 444356092776315 / 133029050096658

	start_time_ms = round(time.time() * 1000)
	
	cuboids = []

	for line in input_file: 
		split = [x for x in line.strip().replace('x=', '').replace(',y=', ' ').replace(',z=', ' ').replace('..', ' ').split(' ')]
		for i in range(1, len(split)): 
			split[i] = int(split[i])
		# c_min = Vec3(split[1], split[3], split[5])
		c_min = [split[1], split[3], split[5]]
		# c_max = Vec3(split[2], split[4], split[6])
		c_max = [split[2], split[4], split[6]]
		cuboids.append([split[0], c_min, c_max])

	# print(cuboids[0][2] - cuboids[0][1])
	print(get_intersection(cuboids[0], cuboids[1]))
	
	# scoreboard = [0, 0]
	# # games = { (4, 0, 8, 0): 1 }
	# games = { (2, 0, 7, 0): 1 }
	# p1_turn = True

	# while len(games) > 0: 
		
	# 	games_turn_start = games.copy()
	# 	for game_state, count in games_turn_start.items(): 

	# 		if p1_turn: p1, s1, p2, s2 = game_state
	# 		else: 		p2, s2, p1, s1 = game_state

	# 		for q_sum_rolls, q_count in quantum_distribution.items(): 

	# 			new_pos = p1 + q_sum_rolls
	# 			while new_pos > 10: 
	# 				new_pos -= 10
				
	# 			new_score = s1 + new_pos
	# 			new_count = count * q_count

	# 			if new_score >= 21: 
	# 				if p1_turn: scoreboard[0] += new_count
	# 				else: 		scoreboard[1] += new_count
	# 			else: 
	# 				if p1_turn: new_game_state = (new_pos, new_score, p2, s2)
	# 				else: 		new_game_state = (p2, s2, new_pos, new_score)
	# 				games.setdefault(new_game_state, 0)
	# 				games[new_game_state] += new_count
			
	# 		games[game_state] -= count

	# 		if games[game_state] == 0: 
	# 			del games[game_state]

	# 	p1_turn = not p1_turn

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	# print(run_title, "scoreboard:", scoreboard, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
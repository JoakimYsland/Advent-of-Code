
# https://adventofcode.com/2022/day/12 / https://adventofcode.com/2021/day/15

import string
import math
import re

import time
from copy import deepcopy
from collections import namedtuple
from queue import PriorityQueue

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

start = None
end = None
input_map = []

Vec2 = namedtuple("Vec2", ['x', 'y'])

for y, line in enumerate(input_file):

	input_map.append([])
	line = line.rstrip()
	for x, c in enumerate(line): 
		if c == 'S': 
			start = Vec2(x, y)
			c = 'a'
		elif c == 'E': 
			end = Vec2(x, y)
			c = 'z'
		c = string.ascii_lowercase.index(c.lower())
		input_map[-1].append(c)

class Node: 
	def __init__(self, x, y, parent=None, cost=0, heuristic=0): 
		self.x = x
		self.y = y
		self.parent = parent
		self.cost = cost
		self.heuristic = heuristic
		self.total_cost = cost + heuristic

def visualize():
	path = []
	current = end
	while current != None: 
		path.append(current)
		current = closed[current].parent

	visualization = [['.' for x in range(map_size.x)] for y in range(map_size.y)]

	for pos in path: 
		# visualization[pos.x][pos.y] = str(input_map[pos.x][pos.y])
		visualization[pos.y][pos.x] = string.ascii_lowercase[input_map[pos.y][pos.x]]
	
	for line in visualization: 
		print(''.join(line))

def a_star_search(start, goal): 
	
	def get_adjacent(pos):
		adjacent = []
		if (pos.x > 0): 			adjacent.append(Vec2(pos.x-1, pos.y))
		if (pos.x < map_size.x-1): 	adjacent.append(Vec2(pos.x+1, pos.y))
		if (pos.y > 0): 			adjacent.append(Vec2(pos.x, pos.y-1))
		if (pos.y < map_size.y-1): 	adjacent.append(Vec2(pos.x, pos.y+1))
		return adjacent

	frontier_pqueue = PriorityQueue()
	frontier_pqueue.put((0, start))
	frontier = { start: Node(0, 0, None) }
	closed = {}

	while len(frontier) > 0: 
		_, current = frontier_pqueue.get()
		current_node = frontier[current]
		closed[current] = current_node
		del frontier[current]

		if current == goal: 
			break

		for child in get_adjacent(current): 
			rm_current = input_map[current_node.y][current_node.x]
			rm_child = input_map[child.y][child.x]

			# Continue if the height different is invalid
			if rm_child > rm_current + 1: 
				continue

			if child in closed: 
				continue

			heuristic = ((map_size.x-1) - child.x) + ((map_size.y-1) - child.y)

			# In this situation, Height does not represent cost. 
			# Cost is number of steps and therefore increments by 1. 
			child_cost = current_node.cost + 1 # input_map[child.y][child.x]
			child_total_cost = child_cost + heuristic

			if child in frontier: 
				if frontier[child].total_cost < child_total_cost:
					continue
			
			child_node = Node(child.x, child.y, current, child_cost, heuristic)
			if not child in frontier: 
				frontier_pqueue.put((child_total_cost, child))
			frontier[child] = child_node

	return closed

map_size = Vec2(len(input_map[0]), len(input_map))
closed = a_star_search(start, end)

visualize()

# Retrace path to count steps
path = []
current = end
while current != None: 
	path.append(current)
	current = closed[current].parent

print("Steps to E:", len(path) - 1)
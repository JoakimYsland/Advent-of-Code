
# https://adventofcode.com/2021/day/15

import re
import time
from copy import deepcopy
from collections import namedtuple
from queue import PriorityQueue

Vec2 = namedtuple("Vec2", ['x', 'y'])

class Node: 
	def __init__(self, x, y, parent=None, cost=0, heuristic=0): 
		self.x = x
		self.y = y
		self.pos = Vec2(x, y)
		self.parent = parent
		self.cost = cost
		self.heuristic = heuristic
		self.total_cost = cost + heuristic

	def __eq__(self, other):
		if isinstance(other, Node):
			return self.total_cost == other.total_cost
		return False

def run(run_title, input_file):

	def visualize(goal, closed):
		def reconstruct_path(current, closed): 
			path = []
			print(closed[current].parent)
			while current != None: 
				path.append(current)
				current = closed[current].parent
			return path

		visualization = [['.' for x in range(map_size.x)] for y in range(map_size.y)]

		for pos in reconstruct_path(goal, closed): 
			visualization[pos.x][pos.y] = str(risk_map[pos.x][pos.y])
		
		for line in visualization: 
			print(''.join(line))

	def expand_risk_map(expansions): 
		def expand(risk):
			r = risk % 9
			return r if r != 0 else 9

		map_copy = deepcopy(risk_map)
		for i in range(0, expansions): 
			for j, line in enumerate(map_copy): 
				risk_map[j] += [expand(r+1+i) for r in line] # Horizontal

		map_copy = deepcopy(risk_map)
		for i in range(0, expansions): 
			for j, line in enumerate(map_copy): 
				risk_map.append([expand(r+1+i) for r in line]) # Vertical

	def a_star_search(start, goal): 
		def get_adjacent(pos):
			adjacent = []
			if (pos.x > 0): 			adjacent.append(Vec2(pos.x-1, pos.y))
			if (pos.x < map_size.x-1): 	adjacent.append(Vec2(pos.x+1, pos.y))
			if (pos.y > 0): 			adjacent.append(Vec2(pos.x, pos.y-1))
			if (pos.y < map_size.y-1): 	adjacent.append(Vec2(pos.x, pos.y+1))
			return adjacent

		def get_heuristic(pos): 
			if pos in frontier: 
				return frontier[pos].heuristic
			else: 
				return ((map_size.x-1) - pos.x) + ((map_size.y-1) - pos.y)

		frontier = { start: Node(0, 0, None) }
		frontier_prioq = PriorityQueue()
		frontier_prioq.put((0, Node(0, 0, None)))
		closed = {}

		while not frontier_prioq.empty(): 
			_, current = frontier_prioq.get()
			current_pos = Vec2(current.x, current.y)
			closed[current_pos] = current

			if current_pos in frontier: 
				del frontier[current_pos]
			# del frontier[current_pos]

			if current_pos == goal: 
				break

			for child in get_adjacent(current): 
				if child in closed: 
					continue

				heuristic = get_heuristic(child)
				child_cost = current.cost + risk_map[child.x][child.y]
				child_total_cost = child_cost + heuristic

				if child in frontier: 
					if frontier[child].total_cost < child_total_cost:
						continue
				
				child_node = Node(child.x, child.y, current, child_cost, heuristic)
				frontier[child] = child_node
				frontier_prioq.put((child_total_cost, child_node))

		return closed

	# --------------------------------------------------------------------------------

	# Test / Real – 315 / 2925 (3838ms)

	risk_map = []
	start_time_ms = round(time.time() * 1000)

	for line in input_file: 
		risk_map.append([int(c) for c in line.strip()])

	expand_risk_map(4)
	map_size = Vec2(len(risk_map[0]), len(risk_map))

	start = Vec2(0,0)
	end = Vec2(map_size.x-1, map_size.y-1)
	closed = a_star_search(start, end)

	# goal = closed[end]
	# visualize(closed[end].pos, closed)
	visualize(end, closed)
	print(run_title, "closed[end]:", closed[end].cost)

	end_time_ms = round(time.time() * 1000)
	print("time:", end_time_ms - start_time_ms)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
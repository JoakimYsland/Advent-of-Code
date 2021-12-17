
# https://adventofcode.com/2021/day/15

import re
from copy import deepcopy
from collections import namedtuple

Vec2 = namedtuple("Vec2", ['x', 'y'])
Node = namedtuple("Node", ['parent', 'cost', 'total_cost'])

def run(run_title, input_file):

	def visualize():
		def reconstruct_path(current, closed): 
			path = []
			while current != None: 
				path.append(current)
				current = closed[current].parent
			path.reverse()
			return path

		path = reconstruct_path(goal, closed)

		visualization = [['.' for x in range(map_size.x)] for y in range(map_size.y)]
		# visualization = [[str(risk_map[y][x]) for x in range(map_size.x)] for y in range(map_size.y)]
		for pos in path: 
			visualization[pos.x][pos.y] = str(risk_map[pos.x][pos.y])
		
		for line in visualization: 
			print(''.join(line))

	def expand_risk_map(): 

		def expand(risk):
			risk += 1
			if risk > 9:
				risk -= 9
			return risk

		exp = 4

		# Horizontal
		map_copy = deepcopy(risk_map)
		for i in range(0, exp): 
			for j, line in enumerate(map_copy): 
				risk_map[j] += [expand(r+i) for r in line]

		# Vertical
		map_copy = deepcopy(risk_map)
		for i in range(0, exp): 
			for j, line in enumerate(map_copy): 
				risk_map.append([expand(r+i) for r in line])

	def a_star_search(start, goal): 

		def get_adjacent(node):
			adjacent = []
			if (node.x > 0): 			adjacent.append(Vec2(node.x-1, node.y))
			if (node.x < map_size.x-1): adjacent.append(Vec2(node.x+1, node.y))
			if (node.y > 0): 			adjacent.append(Vec2(node.x, node.y-1))
			if (node.y < map_size.y-1): adjacent.append(Vec2(node.x, node.y+1))
			return adjacent

		def get_frontier_best(): 
			best = list(frontier.keys())[0]
			for pos, node in frontier.items():
				if node.total_cost < frontier[best].total_cost:
					best = pos
			return best, frontier[best]

		frontier = { start: Node(None, 0,0) }
		closed = {}

		while len(frontier) > 0: 
			current, current_node = get_frontier_best()
			closed[current] = current_node
			del frontier[current]

			if current == goal: 
				break

			for child in get_adjacent(current): 
				if child in closed: 
					continue

				heuristic = ((map_size.x-1) - child.x) + ((map_size.y-1) - child.y)
				child_cost = current_node.cost + risk_map[child.x][child.y]
				child_total_cost = child_cost + heuristic

				if child in frontier: 
					if frontier[child].total_cost < child_total_cost:
						continue
				
				frontier[child] = Node(current, child_cost, child_total_cost)

		return closed

	# --------------------------------------------------------------------------------

	# Test / Real – 315 / ???

	risk_map = []

	for line in input_file: 
		risk_map.append([int(c) for c in line.strip()])

	expand_risk_map()
	map_size = Vec2(len(risk_map[0]), len(risk_map))

	start = Vec2(0,0)
	goal = Vec2(map_size.x-1, map_size.y-1)
	closed = a_star_search(start, goal)

	# for node in closed: 
	# 	print(node, closed[node])

	visualize()	
	print(closed[goal])

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
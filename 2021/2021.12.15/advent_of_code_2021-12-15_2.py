
# https://adventofcode.com/2021/day/15

import re
from copy import deepcopy
from collections import namedtuple
from collections import OrderedDict

Vec2 = namedtuple("Vec2", ['x', 'y'])
Node = namedtuple("Node", ['parent', 'cost', 'total_cost'])

def run(run_title, input_file):

	def visualize():
		def reconstruct_path(current, closed): 
			path = []
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
		def get_adjacent(node):
			adjacent = []
			if (node.x > 0): 			adjacent.append(Vec2(node.x-1, node.y))
			if (node.x < map_size.x-1): adjacent.append(Vec2(node.x+1, node.y))
			if (node.y > 0): 			adjacent.append(Vec2(node.x, node.y-1))
			if (node.y < map_size.y-1): adjacent.append(Vec2(node.x, node.y+1))
			return adjacent

		def get_frontier_best(): 
			return min(frontier.items(), key=lambda x: x[1].total_cost) 

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

	expand_risk_map(4)
	map_size = Vec2(len(risk_map[0]), len(risk_map))

	start = Vec2(0,0)
	goal = Vec2(map_size.x-1, map_size.y-1)
	closed = a_star_search(start, goal)

	# visualize()	
	print(closed[goal])

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
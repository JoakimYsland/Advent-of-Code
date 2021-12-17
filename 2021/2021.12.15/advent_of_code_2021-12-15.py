
# https://adventofcode.com/2021/day/15

import re
from collections import namedtuple

Vec2 = namedtuple("Vec2", ['x', 'y'])
Node = namedtuple("Node", ['cost', 'total_cost'])

def run(run_title, input_file):

	def a_star_search(start, goal): 

		def get_adjacent(node):
			adjacent = []
			if (node.x > 0): 				adjacent.append(Vec2(node.x-1, node.y))
			if (node.x < map_size.x-1): 	adjacent.append(Vec2(node.x+1, node.y))
			if (node.y > 0): 				adjacent.append(Vec2(node.x, node.y-1))
			if (node.y < map_size.y-1):  	adjacent.append(Vec2(node.x, node.y+1))
			return adjacent

		def get_frontier_best(): 
			best = list(frontier.keys())[0]
			for pos, node in frontier.items():
				if node.total_cost < frontier[best].total_cost:
					best = pos
			return best

		frontier = { start: Node(0,0) }
		closed = {}

		while len(frontier) > 0: 
			
			# current = node in open with best value
			current = get_frontier_best()

			# Add current to closed
			closed[current] = frontier[current]

			# Remove current from open
			del frontier[current]

			# if current is the goal, break
			if current == goal: 
				break

			# for each child in children
			for child in get_adjacent(current): 

				# if the child in in closed: 
				if child in closed: 
					continue

				# distance_from_start = current.distance_from_start + distance between child and current
				distance_from_start = closed[current].cost + risk_map[child.x][child.y]
				# heuristic = distance from child to goal
				pyth_a = (map_size.x-1) - child.x
				pyth_b = (map_size.y-1) - child.y
				heuristic = pyth_a + pyth_b
				# child_total_cost = distance_from_start + heuristic
				child_total_cost = distance_from_start + heuristic

				# if child is in open: 
				if child in frontier: 
					# if child is already in open with a lower distance_from_start: 
					if frontier[child].total_cost < child_total_cost:
						continue
				
				# Add child to open
				frontier[child] = Node(distance_from_start, child_total_cost)

		return closed

	# --------------------------------------------------------------------------------

	# Test / Real – 40 / 609

	risk_map = []

	for line in input_file: 
		risk_map.append([int(c) for c in line.strip()])

	risk_map = [list(x) for x in zip(*risk_map)] # Transpose
	map_size = Vec2(len(risk_map[0]), len(risk_map))
	start = Vec2(0,0)
	goal = Vec2(map_size.x-1, map_size.y-1)

	closed = a_star_search(start, goal)

	# print(closed)
	for node in closed: 
		print(node, closed[node])

	# viz = [['-' for x in range(map_size.x)] for y in range(map_size.y)]
	# for node in closed.keys():
	# 	viz[node.x][node.y] = "#"
	
	# for line in viz: 
	# 	print(''.join(line))

	# for i, line in enumerate(risk_map): 
	# 	line = '-' * len(line)
	# 	for n in (n for n in closed.keys() if n.y == i): 
	# 		print("klasjd")
	# 		line[n.x] == '#'
	# 	print(line)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
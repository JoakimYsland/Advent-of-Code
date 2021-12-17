
# https://adventofcode.com/2021/day/15

import re
from collections import namedtuple

Vec2 = namedtuple("Vec2", ['x', 'y'])
Node = namedtuple("Node", ['cost', 'total_cost'])

def run(run_title, input_file):

	# def add_pair(pair, count):
	# 	polymer_pairs.setdefault(pair, 0)
	# 	polymer_pairs[pair] += count

	# def remove_pair(pair, count):
	# 	if pair in polymer_pairs:
	# 		polymer_pairs[pair] -= count
	# 		if (polymer_pairs[pair] < 1): 
	# 			del polymer_pairs[pair]

	# def count_element(element, count): 
	# 	element_count.setdefault(element, 0)
	# 	element_count[element] += count

	# def heuristic(a: GridLocation, b: GridLocation) -> float:
	# 	(x1, y1) = a
	# 	(x2, y2) = b
	# 	return abs(x1 - x2) + abs(y1 - y2)

	def get_adjacent(node):
		adjacent = []
		if (node.x > 0): 				adjacent.append(Vec2(node.x-1, node.y))
		if (node.x < map_size.x-1): 	adjacent.append(Vec2(node.x+1, node.y))
		if (node.y > 0): 				adjacent.append(Vec2(node.x, node.y-1))
		if (node.y < map_size.y-1):  	adjacent.append(Vec2(node.x, node.y+1))
		return adjacent

		# adjacent = {'left':None, 'right':None, 'up':None, 'down':None}
		# if (x > 0): 				adjacent['left'] 	= Vec2(x-1, y)
		# if (x < map_size.x - 1): 	adjacent['right'] 	= Vec2(x+1, y)
		# if (y > 0): 				adjacent['up'] 		= Vec2(x, y-1)
		# if (y < map_size.y - 1):  	adjacent['down'] 	= Vec2(x, y+1)
		# return adjacent

	# def a_star_search(start, goal)
	def a_star_search(): 
		open = {}
		closed = {}

		start = Vec2(0,0)
		goal = Vec2(len(risk_map) - 1, len(risk_map[0]) - 1)
		
		open[start] = Node(0,0)

		while len(open) > 0: 
			
			# current = node in open with best value
			current = list(open.keys())[0]
			for node in open: 
				if open[node].total_cost < open[current].total_cost: 
					current = node

			# Add current to closed
			closed[current] = open[current]

			# Remove current from open
			del open[current]

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
				pyth_a = pow((map_size.x-1) - child.x, 2)
				pyth_b = pow((map_size.y-1) - child.y, 2)
				heuristic = pyth_a + pyth_b
				# child_total_cost = distance_from_start + heuristic
				child_total_cost = distance_from_start + heuristic

				# if child is in open: 
				if child in open: 
					# if child is already in open with a lower distance_from_start: 
					if open[child].total_cost < child_total_cost:
						continue
				
				# Add child to open
				open[child] = Node(distance_from_start, child_total_cost)


			# best = sorted([(Vec2(pos.x, pos.y), val), for (pos,val) in open.items()])[0]
			# current_node = 

		return closed


		# frontier = PriorityQueue()
		# frontier.put(start, 0)

		# total_cost = (position, cost)

		# while not frontier.empty(): 
		# 	current = frontier.get()
			
		# 	if current == goal: 
		# 		break

		# 		for next in graph.neighbors(current_location):
		# 			new_cost = total_cost + next.cost
		# 			if next not in total_cost or new_cost < total_cost: 
		# 				total_cost[next] = new_cost

		# return came_from, total_cost


	# --------------------------------------------------------------------------------

	# Test / Real – 40 / 4441317262452

	# polymer_pairs = {}
	# element_count = {}
	# pair_insertion_rules = {}
	risk_map = []

	for line in input_file: 
		risk_map.append([int(c) for c in line.strip()])

	risk_map = [list(x) for x in zip(*risk_map)] # Transpose
	map_size = Vec2(len(risk_map[0]), len(risk_map))

	closed = a_star_search()

	# print(closed)
	for node in closed: 
		print(node, closed[node])

	# total_risk = 0
	# for node in closed: 
		# total_risk += closed[node].
	
	# start, goal = Vec2(0, 0) Vec2(len(risk_map), len(risk_map[0]))

	# came_from, cost_so_far = a_star_search(diagram4, start, goal)
	# draw_grid(diagram4, point_to=came_from, start=start, goal=goal)
	# draw_grid(diagram4, path=reconstruct_path(came_from, start=start, goal=goal))

	# for step in range(0, 40): 
	# 	for pair, count in polymer_pairs.copy().items(): 
	# 		new_element = pair_insertion_rules[pair]
	# 		count_element(new_element, count)
	# 		remove_pair(pair, count)
	# 		add_pair(pair[0] + new_element, count)
	# 		add_pair(new_element + pair[1], count)

	# print(risk_map)

	# element_count_range = max(element_count.values()) - min(element_count.values())
	# print(run_title, "element_count_range:", element_count_range)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
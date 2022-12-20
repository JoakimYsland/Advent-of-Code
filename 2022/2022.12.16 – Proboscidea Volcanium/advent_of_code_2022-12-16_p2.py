
# https://adventofcode.com/2022/day/16

import string
import math
import time
import re
from copy import deepcopy

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

input_file = open('test_input.txt', 'r').readlines()
# input_file = open('input.txt', 'r').readlines()

class Valve:
	tunnels = None
	def __init__(self, name, flow_rate): 
		self.name = name
		self.flow_rate = flow_rate

valves = {}
start_valve = None
best_path = None
paths = 1

for i, line in enumerate(input_file):

	line = line.rstrip()
	line = re.split(" |=|; |, ", line)
	name = line[1]
	flow_rate = int(line[5])
	tunnels = line[10:len(line)]
	valve = Valve(name, flow_rate)
	valve.tunnels = tunnels
	valves[valve.name] = valve

	if name == "AA":
		start_valve = valve

# https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/dijkstras-algorithm/

from queue import PriorityQueue

class Graph:
	def __init__(self, num_of_vertices):
		self.v = num_of_vertices
		self.visited = []

def dijkstra(graph, start_vertex):
	D = {}
	for k, v in valves.items(): 
		D[k] = float('inf')
	D[start_vertex.name] = 0

	pq = PriorityQueue()
	pq.put((0, start_vertex.name))

	while not pq.empty():
		(dist, current_vertex) = pq.get()
		graph.visited.append(current_vertex)

		for neighbor in valves[current_vertex].tunnels: 
			distance = 1
			if neighbor not in graph.visited:
				old_cost = D[neighbor]
				new_cost = D[current_vertex] + distance
				if new_cost < old_cost:
					pq.put((new_cost, neighbor))
					D[neighbor] = new_cost
	return D

##########

class Path: 

	def __init__(self, target_valves): 
		self.time1 = 26
		self.time2 = 26
		self.score = 0
		self.target_valves = target_valves
		self.current1 = None
		self.current2 = None
		self.history = {}

	def open_valve(self, time, valve): 
		score = time * valve.flow_rate
		self.score += score
		self.target_valves.pop(valve.name)
		self.history[valve.name] = score

	def get_potential(self): 
		potential = self.score
		max_time = max(self.time1, self.time2)
		for valve in self.target_valves.values(): 
			potential += valve.flow_rate * max_time
		return potential

def Traverse(path): 
	graph1 = Graph(len(valves))
	graph2 = Graph(len(valves))
	D1 = dijkstra(graph1, path.current1)
	D2 = dijkstra(graph2, path.current2)
	new_paths = []
	global best_path
	global paths

	# Check if the path can possibly get a better pressure
	path_potential = path.get_potential()
	if best_path != None and path_potential < best_path.score: 
		return

	for x in range(0, len(path.target_valves), 1): 
		for y in range(0, len(path.target_valves), 1): 

			if x == y: 
				continue

			temp = list(path.target_valves.values())
			name1, valve1 = temp[x].name, temp[x]
			name2, valve2 = temp[y].name, temp[y]
			new_path = deepcopy(path)

			travel_time1 = D1[name1]
			if path.time1 >= travel_time1 + 1: 
				new_path.time1 -= travel_time1 + 1
				new_path.current1 = valve1
				new_path.open_valve(new_path.time1, valve1)

			travel_time2 = D2[name2]
			if path.time2 >= travel_time2 + 1: 
				new_path.time2 -= travel_time2 + 1
				new_path.current2 = valve2
				new_path.open_valve(new_path.time2, valve2)

			# We spent time. Therefore, we did something
			if path.time1 != new_path.time1 or path.time2 != new_path.time2: 
				new_paths.append(new_path)
				paths += 1
	
	if len(new_paths) == 0: 
		if best_path == None: 
			best_path = path
		else: 
			if path.score > best_path.score: 
				best_path = path

	for p in new_paths: 
		Traverse(p)

import datetime
start_time = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
start_time_ms = round(time.time() * 1000)
print("Start time:", start_time)

valves_with_flow_rate = { k:v for (k,v) in valves.items() if v.flow_rate > 0 }
start_path = Path(valves_with_flow_rate)

start_path.current1 = start_valve
start_path.current2 = start_valve

Traverse(start_path)

# valves_with_flow_rate: 6
# best_path: 1651
# {'DD': 560, 'BB': 325, 'JJ': 441, 'HH': 286, 'EE': 27, 'CC': 12}
# Time: 54 ms
# 1707
print("best_path:", best_path.score)
print("History:", best_path.history, " => ", len(best_path.history))
print("Remaining time:", best_path.time1, "/", best_path.time2)
print("paths:", paths)

end_time_ms = round(time.time() * 1000)
print("Time:", end_time_ms - start_time_ms, "ms")
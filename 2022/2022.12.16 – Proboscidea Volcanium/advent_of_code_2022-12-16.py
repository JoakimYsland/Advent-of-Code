
# https://adventofcode.com/2022/day/16

import string
import math
import time
import re
from copy import deepcopy

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

class Valve:
	tunnels = None
	def __init__(self, name, flow_rate): 
		self.name = name
		self.flow_rate = flow_rate

valves = {}
start_valve = None
most_pressure = 0

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
		self.time = 30
		self.score = 0
		self.target_valves = target_valves
		self.history = []

	def open_valve(self, valve): 
		self.time -= 1
		self.score += self.time * valve.flow_rate
		self.target_valves.pop(valve.name)
		self.history.append(valve)

	def get_potential(self): 
		potential = self.score
		for valve in self.target_valves.values(): 
			potential += valve.flow_rate * self.time
		return potential

def Traverse(path): 
	graph = Graph(len(valves))
	D = dijkstra(graph, path.history[-1])
	new_paths = []
	global most_pressure

	# Check if the path can possibly get a better pressure
	path_potential = path.get_potential()
	if path_potential < most_pressure: 
		return

	for name, valve, in path.target_valves.items(): 
		travel_time = D[name]
		if travel_time + 1 > path.time: 
			continue # Not enough time to open
		new_path = deepcopy(path)		
		new_path.time -= travel_time
		new_path.open_valve(valve)
		new_paths.append(new_path)
	
	if len(new_paths) == 0: 
		most_pressure = max(most_pressure, path.score)

	for p in new_paths: 
		Traverse(p)

start_time_ms = round(time.time() * 1000)

valves_with_flow_rate = { k:v for (k,v) in valves.items() if v.flow_rate > 0 }
print("valves_with_flow_rate:", len(valves_with_flow_rate))

start_path = Path(valves_with_flow_rate)
start_path.history.append(start_valve)

Traverse(start_path)

print("most_pressure:", most_pressure)

end_time_ms = round(time.time() * 1000)

print("Time:", end_time_ms - start_time_ms, "ms")
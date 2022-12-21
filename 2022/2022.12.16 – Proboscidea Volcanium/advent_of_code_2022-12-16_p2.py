
# https://adventofcode.com/2022/day/16

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

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

class Valve:
	tunnels = None
	def __init__(self, name, flow_rate): 
		self.name = name
		self.flow_rate = flow_rate

valves = {}
start_valve = None

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
		start_time = 26
		self.time1 = start_time
		self.time2 = start_time
		self.score = 0
		self.target_valves = target_valves
		self.current1 = None
		self.current2 = None
		self.history = {}
		
		self.potential = 0
		for valve in self.target_valves.values(): 
			self.potential += valve.flow_rate * (start_time - 1) # 1 minute to open

	def open_valve(self, time, valve): 
		score = time * valve.flow_rate
		self.score += score
		self.target_valves.pop(valve.name)
		self.history[valve.name] = score

	def update_potential(self, D1, D2): 
		potential = self.score
		for valve in self.target_valves.values(): 
			max_time = max(self.time1 - D1[valve.name], self.time2 - D2[valve.name])
			max_time -= 1 # 1 minute to open
			if max_time > 0:
				potential += valve.flow_rate * max_time
		self.potential = potential

best_path = None
num_paths = 1
valve_cycles = 0

def Traverse(path): 
	graph1 = Graph(len(valves))
	graph2 = Graph(len(valves))
	D1 = dijkstra(graph1, path.current1)
	D2 = dijkstra(graph2, path.current2)
	new_paths = []
	global best_path
	global num_paths
	global valve_cycles

	if len(path.history) > valve_cycles: 
		valve_cycles = len(path.history)
		print("Valve Cycle", valve_cycles, get_time_now())

	# Prune valves no one have time to open
	for v in list(path.target_valves.keys()): 
		if path.time1 < D1[v] + 1 and path.time2 < D2[v] + 1: 
			path.target_valves.pop(v)
	
	path.update_potential(D1, D2)

	# The score has to be higher than this
	if path.potential <= 2314: # 2314 => Too low
		return

	# Check if the path can possibly get a better pressure
	if path.potential < best_path.score: 
		return

	for x in range(0, len(path.target_valves), 1): 
		for y in range(0, len(path.target_valves), 1): 

			if valve_cycles  == 0 and y <= x: 
				# If we are on the first cycle, we do not need to check 
				# flipped positions. They would result in identical paths. 
				continue

			if x == y: 
				# Don't travel to the same valve
				continue

			temp = list(path.target_valves.values())
			name1, valve1 = temp[x].name, temp[x]
			name2, valve2 = temp[y].name, temp[y]
			new_path = deepcopy(path)
			opened_valve = False

			cost1 = D1[name1] + 1 # Travel time + open valve
			if path.time1 >= cost1: 
				new_path.time1 -= cost1
				new_path.current1 = valve1
				new_path.open_valve(new_path.time1, valve1)
				opened_valve = True

			cost2 = D2[name2] + 1 # Travel time + open valve
			if path.time2 >= cost2: 
				new_path.time2 -= cost2
				new_path.current2 = valve2
				new_path.open_valve(new_path.time2, valve2)
				opened_valve = True

			if opened_valve == True: 
				new_paths.append(new_path)
				num_paths += 1

	if len(new_paths) == 0: 
		if path.score > best_path.score: 
			best_path = path

	for p in new_paths: 
		Traverse(p)

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

# Valves with flow_rate > 0, sorted low => high
valves_with_flow_rate = { k:v for (k,v) in sorted(valves.items(), key=lambda item: item[1].flow_rate) if v.flow_rate > 0 }
print("valves_with_flow_rate:", len(valves_with_flow_rate))

start_path = Path(valves_with_flow_rate)
start_path.current1 = start_valve
start_path.current2 = start_valve
best_path = start_path
print("start_path.potential:", start_path.potential)

Traverse(start_path)

print("——————————")
print("best_path:", best_path.score)
print("History:", best_path.history, " => ", len(best_path.history))
print("Remaining time:", best_path.time1, "/", best_path.time2)
print("——————————")
print("num_paths:", num_paths)

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
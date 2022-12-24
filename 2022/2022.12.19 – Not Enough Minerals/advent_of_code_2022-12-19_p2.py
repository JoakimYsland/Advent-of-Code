
# https://adventofcode.com/2022/day/19

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
	return datetime.datetime.now().strftime("%H:%M:%S")

class Blueprint: 
	def __init__(self, bp_id, robots): 
		self.bp_id = bp_id
		self.robots = robots
		self.max_cost = [0,0,0]
		for robot in robots: 
			for i in range(0, 3, 1): 
				self.max_cost[i] = max(self.max_cost[i], robot[i])
		self.max_cost.append(9999) # This will make sure geodes always have value

def print_blueprint(bp): 
	s = "Blueprint {0}: Ore Robot {1} / Clay Robot {2} / Obsidian Robot {3} / Geode Robot {4}"
	print(s.format(i, bp.robots[0], bp.robots[1], bp.robots[2], bp.robots[3]))

def can_build(robot, inventory): 
	for i, cost in enumerate(robot): 
		if robot[i] > inventory[i]: 
			return False
	return True

def build(robot_id, robot, fleet, inventory): 
	for i, cost in enumerate(robot): 
		inventory[i] -= robot[i]
	fleet[robot_id] += 1

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

blueprints = []
most_geodes = 0
robot_build_priority = [0,1,2,3]
# robot_build_priority = [3,2,1,0]

for i, line in enumerate(input_file):

	line = line.rstrip()
	line = re.split(" |: ", line)
	values = [int(e) for e in line if e.isnumeric()]

	ore_robot = [values[1], 0, 0]
	clay_robot = [values[2], 0, 0]
	obsidian_robot = [values[3], values[4], 0]
	geode_robot = [values[5], 0, values[6]]

	# Blueprint IDs start at 1, not 0
	new_blueprint = Blueprint(i + 1, [ore_robot, clay_robot, obsidian_robot, geode_robot])
	blueprints.append(new_blueprint)

def run_branch(bp, fleet, inventory, remaining_time, robot_id): 

	def end_branch(): 
		global most_geodes
		most_geodes = max(most_geodes, inventory[3])
		# print(remaining_time, fleet, inventory)

	global num_branches

	robot_cost = bp.robots[robot_id]

	# Return if the current fleet will 
	# never be able to build the target robot
	for i, cost in enumerate(robot_cost): 
		if cost > 0 and fleet[i] == 0: 
			end_branch()
			return

	while remaining_time > 0: 

		init_fleet = fleet.copy()
		built_robot = False
	
		if can_build(robot_cost, inventory): 

			# There is no point in producing more of a resource 
			# than what can be spent in 1 round to build a new robot
			# https://www.reddit.com/r/adventofcode/comments/zpy5rm/2022_day_19_what_are_your_insights_and/

			if fleet[robot_id] >= bp.max_cost[robot_id]: 
				end_branch()
				return

			# Compare max amount of resources against how much 
			# we could possibly use within the remaining time
			# https://www.reddit.com/r/adventofcode/comments/zpy5rm/2022_day_19_what_are_your_insights_and/

			if (fleet[robot_id] * remaining_time) + inventory[robot_id] >= remaining_time * bp.max_cost[robot_id]: 
				end_branch()
				return

			# Build the robot
			build(robot_id, robot_cost, fleet, inventory)
			built_robot = True

		# Collect resources
		for i in range(0, 4, 1): 
			inventory[i] += init_fleet[i]

		# Reduce time
		remaining_time -= 1

		if remaining_time == 0: 
			end_branch()
			return

		# If we've built a robot, end the branch and 
		# create 4 new ones, targeting each of the robots
		if built_robot: 
			run_branch(bp, fleet.copy(), inventory.copy(), remaining_time, 0)
			run_branch(bp, fleet.copy(), inventory.copy(), remaining_time, 1)
			run_branch(bp, fleet.copy(), inventory.copy(), remaining_time, 2)
			run_branch(bp, fleet.copy(), inventory.copy(), remaining_time, 3)
			num_branches += 3 # Technically, we are continuing this branch and adding 3 more
			end_branch()
			return

	# Ran out of time
	end_branch()

num_branches = 4
quality_levels = []

def simulate_blueprint(i): 
	global most_geodes
	global quality_levels
	most_geodes = 0
	remaining_time = 24
	# print_blueprint(blueprints[i])
	run_branch(blueprints[i], [1,0,0,0], [0,0,0,0], remaining_time, 0)
	run_branch(blueprints[i], [1,0,0,0], [0,0,0,0], remaining_time, 1)
	run_branch(blueprints[i], [1,0,0,0], [0,0,0,0], remaining_time, 2)
	run_branch(blueprints[i], [1,0,0,0], [0,0,0,0], remaining_time, 3)
	quality_level = blueprints[i].bp_id * most_geodes
	quality_levels.append(quality_level)

for i in range(0, len(blueprints)): 
	simulate_blueprint(i)

print("most_geodes:", most_geodes) # 9
print("quality_levels:", sum(quality_levels))
print("num_branches:", num_branches) # 72419

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
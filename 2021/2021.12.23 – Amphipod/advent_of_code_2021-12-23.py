
# https://adventofcode.com/2021/day/22

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def leave(room_index, hallway_index): 
		nonlocal total_cost
		room_first = burrow[room_index][0]
		room_second = burrow[room_index][1]

		if room_first != '': 
			amphipod = room_first
			cost_exit_room = 1
			burrow[room_index][0] = ''
		else: 
			amphipod = room_second
			cost_exit_room = 2
			burrow[room_index][1] = ''

		room_entrance_index = room_index * 2
		cost_hallway_move = abs(hallway_index - room_entrance_index)
		cost_final = (cost_exit_room + cost_hallway_move) * movement_cost[amphipod]
		burrow[0][hallway_index] = amphipod
		print('leave', amphipod, 'to', hallway_index)
		total_cost += cost_final
	
	def enter(hallway_index, room_index): 
		nonlocal total_cost
		room_first = burrow[room_index][0]
		room_second = burrow[room_index][1]
		amphipod = burrow[0][hallway_index]

		if room_second == '': 
			cost_enter_room = 2
			burrow[room_index][1] = amphipod
		else: 
			cost_enter_room = 1
			burrow[room_index][0] = amphipod

		room_entrance_index = room_index * 2
		cost_hallway_move = abs(hallway_index - room_entrance_index)
		cost_final = (cost_hallway_move + cost_enter_room) * movement_cost[amphipod]
		burrow[0][hallway_index] = ''
		print('enter', amphipod, 'from', hallway_index)
		total_cost += cost_final

	def transfer(from_room_index, hallway_index, to_room_index): 
		leave(from_room_index, hallway_index)
		enter(hallway_index, to_room_index)

	# --------------------------------------------------------------------------------

	# Test / Real – 12521 / 10321

	start_time_ms = round(time.time() * 1000)
	
	burrow = [['', '', '', '', '', '', '', '', '', '', '']] # Hallway (0 - left, 10 - right)
	movement_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
	total_cost = 0

	# Example (12521)
	# BCBD => ABCD
	# ADCA => ABCD
	# burrow.append(['B', 'A']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['C', 'D']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['B', 'C']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['D', 'A']) # Room 1 (0 - top, 1 - bottom)
	
	# print(burrow)
	# leave(3,3)
	# transfer(2,5,3)
	# leave(2,5)
	# enter(3,2)
	# transfer(1,3,2)
	# leave(4,7)
	# leave(4,9)
	# enter(7,4)
	# enter(5,4)
	# enter(9,1)
	# print(burrow)

	# 1 3 5 7 9
	#  C B D D  => A B C D
	#  B C A A  => A B C D
	burrow.append(['C', 'B']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['B', 'C']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['D', 'A']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['D', 'A']) # Room 1 (0 - top, 1 - bottom)

	print(burrow)
	leave(4,7) 		# D
	leave(4,9) 		# A
	enter(7,4) 		# D *
	transfer(3,7,4) # D **
	leave(3,1) 		# A
	leave(2,3) 		# B
	transfer(2,5,3) # C *
	enter(3,2) 		# B *
	transfer(1,5,3) # C **
	transfer(1,3,2) # B **
	enter(1,1) 		# A *
	enter(9,1) 		# A **

	print(burrow)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "total_cost:", total_cost, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
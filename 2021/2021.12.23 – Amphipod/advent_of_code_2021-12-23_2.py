
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
		
		for i, a in enumerate(burrow[room_index]): 
			if a != '': 
				amphipod = a
				cost_exit_room = i + 1
				burrow[room_index][i] = ''
				break

		room_entrance_index = room_index * 2
		cost_hallway_move = abs(hallway_index - room_entrance_index)
		cost_final = (cost_exit_room + cost_hallway_move) * movement_cost[amphipod]
		burrow[0][hallway_index] = amphipod
		total_cost += cost_final
	
	def enter(hallway_index, room_index): 
		nonlocal total_cost
		room_first = burrow[room_index][0]
		room_second = burrow[room_index][1]
		amphipod = burrow[0][hallway_index]
		cost_enter_room = None

		empty_slot = len([s for s in burrow[room_index] if s == ''])
		cost_enter_room = empty_slot
		burrow[room_index][empty_slot - 1] = amphipod

		room_entrance_index = room_index * 2
		cost_hallway_move = abs(hallway_index - room_entrance_index)
		cost_final = (cost_hallway_move + cost_enter_room) * movement_cost[amphipod]
		burrow[0][hallway_index] = ''
		print('enter', amphipod, 'from', hallway_index)
		total_cost += cost_final

	def transfer(from_room_index, to_room_index): 
		nonlocal total_cost
		room_first = burrow[from_room_index][0]
		room_second = burrow[from_room_index][1]
		amphipod = None
		cost_exit_room = None

		for i, a in enumerate(burrow[from_room_index]): 
			if a != '': 
				amphipod = a
				cost_exit_room = i + 1
				burrow[from_room_index][i] = ''
				break

		empty_slot = len([s for s in burrow[to_room_index] if s == ''])
		cost_enter_room = empty_slot
		burrow[to_room_index][empty_slot - 1] = amphipod

		from_room_entrance_index = from_room_index * 2
		to_room_entrance_index = to_room_index * 2

		# room_entrance_index = room_index * 2
		cost_hallway_move = abs(from_room_entrance_index - to_room_entrance_index)
		cost_final = (cost_exit_room + cost_hallway_move + cost_enter_room) * movement_cost[amphipod]
		total_cost += cost_final

	# --------------------------------------------------------------------------------

	# Test / Real – 44169 / ???

	start_time_ms = round(time.time() * 1000)
	
	burrow = [['', '', '', '', '', '', '', '', '', '', '']] # Hallway (0 - left, 10 - right)
	movement_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
	total_cost = 0

	# Example (44169)
	burrow.append(['B', 'D', 'D', 'A']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['C', 'C', 'B', 'D']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['B', 'B', 'A', 'C']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['D', 'A', 'C', 'A']) # Room 1 (0 - top, 1 - bottom)
	
	print(burrow)
	leave(4,10) 	# D
	leave(4,0) 		# A
	leave(3,9) 		# B
	leave(3,7) 		# B
	leave(3,1) 		# A
	transfer(2,3) 	# C **
	transfer(2,3) 	# C ***
	leave(2,5) 		# B
	leave(2,3) 		# D
	enter(5,2) 		# B *
	enter(7,2) 		# B **
	enter(9,2) 		# B ***
	transfer(4,3) 	# C ****
	leave(4,9) 		# A
	enter(3,4) 		# D *
	transfer(1,2) 	# B ****
	transfer(1,4) 	# D **
	transfer(1,4) 	# D ***
	enter(1,1) 		# A **
	enter(0,1) 		# A ***
	enter(9,1) 		# A ****
	enter(10,4) 	# D ****
	print(burrow)

	# 1 3 5 7 9
	#  C B D D  => A B C D
	#  D C B A  => A B C D
	#  D B A C  => A B C D
	#  B C A A  => A B C D
	# burrow.append(['C', 'D', 'D', 'B']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['B', 'C', 'B', 'C']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['D', 'B', 'A', 'A']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['D', 'A', 'C', 'A']) # Room 1 (0 - top, 1 - bottom)

	# print(burrow)
	# leave(4,7) 		# D
	# leave(4,9) 		# A
	# enter(7,4) 		# D *
	# transfer(3,7,4) # D **
	# leave(3,1) 		# A
	# leave(2,3) 		# B
	# transfer(2,5,3) # C *
	# enter(3,2) 		# B *
	# transfer(1,5,3) # C **
	# transfer(1,3,2) # B **
	# enter(1,1) 		# A *
	# enter(9,1) 		# A **
	# print(burrow)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "total_cost:", total_cost, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
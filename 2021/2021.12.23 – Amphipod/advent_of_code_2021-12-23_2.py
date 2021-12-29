
# https://adventofcode.com/2021/day/22

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def is_hallway_clear(from_index, to_index): 
		a = min(from_index, to_index)
		b = max(from_index, to_index)
		occupied_slots = [e for e in burrow[0][a:b] if e != '']
		return len(occupied_slots) == 0

	def leave(from_room_index, hallway_index): 
		nonlocal total_cost
		num_vacant = len([s for s in burrow[from_room_index] if s == ''])
		amphipod = burrow[from_room_index][num_vacant]
		burrow[from_room_index][num_vacant] = ''
		cost_exit_room = num_vacant + 1

		from_room_entrance_index = from_room_index * 2
		cost_hallway_move = abs(hallway_index - from_room_entrance_index)
		cost_final = (cost_exit_room + cost_hallway_move) * movement_cost[amphipod]
		total_cost += cost_final
		s = "Move {0} from R{1} to H{2}"
		result = s.format(amphipod, from_room_index, hallway_index)

		if not is_hallway_clear(from_room_entrance_index, hallway_index): 
			s = " – ERROR: Hallway {0} to {1} is blocked!"
			result += s.format(from_room_entrance_index, hallway_index)

		burrow[0][hallway_index] = amphipod

		my_print(result)
	
	def enter(hallway_index, to_room_index): 
		nonlocal total_cost
		amphipod = burrow[0][hallway_index]

		num_vacant = len([s for s in burrow[to_room_index] if s == ''])
		cost_enter_room = num_vacant
		burrow[to_room_index][num_vacant - 1] = amphipod

		to_room_entrance_index = to_room_index * 2
		cost_hallway_move = abs(hallway_index - to_room_entrance_index)
		cost_final = (cost_hallway_move + cost_enter_room) * movement_cost[amphipod]
		burrow[0][hallway_index] = ''
		total_cost += cost_final
		s = "Move {0} from H{1} to R{2}"
		result = s.format(amphipod, hallway_index, to_room_index)

		if not is_hallway_clear(hallway_index, to_room_entrance_index): 
			s = " – ERROR: Hallway {0} to {1} is blocked!"
			result += s.format(hallway_index, to_room_entrance_index)

		my_print(result)

	def transfer(from_room_index, to_room_index): 
		nonlocal total_cost
		num_vacant = len([s for s in burrow[from_room_index] if s == ''])
		amphipod = burrow[from_room_index][num_vacant]
		burrow[from_room_index][num_vacant] = ''
		cost_exit_room = num_vacant + 1

		num_vacant = len([s for s in burrow[to_room_index] if s == ''])
		cost_enter_room = num_vacant
		burrow[to_room_index][num_vacant - 1] = amphipod

		from_room_entrance_index = from_room_index * 2
		to_room_entrance_index = to_room_index * 2
		cost_hallway_move = abs(from_room_entrance_index - to_room_entrance_index)
		cost_final = (cost_exit_room + cost_hallway_move + cost_enter_room) * movement_cost[amphipod]
		total_cost += cost_final
		s = "Transfer {0} from R{1} to R{2}"
		result = s.format(amphipod, from_room_index, to_room_index)

		if not is_hallway_clear(from_room_entrance_index, to_room_entrance_index): 
			s = " – ERROR: Hallway {0} to {1} is blocked!"
			result += s.format(from_room_entrance_index, to_room_entrance_index)

		my_print(result)

	def visualize_burrow(): 
		print(str(burrow[0]).replace('\'\'', '-').replace('\'', '').replace(',', ''))
		for r in [list(x) for x in zip(*burrow[1:5])]: 
			print("    " + str(r).replace('\'\'', '\'-\'').replace('\'', '').replace(',', '  '))

	# --------------------------------------------------------------------------------

	# Test / Real – 44169 / ???

	start_time_ms = round(time.time() * 1000)
	
	burrow = [['', '', '', '', '', '', '', '', '', '', '']] # Hallway (0 - left, 10 - right)
	movement_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
	total_cost = 0

	# # Example (44169)
	# burrow.append(['B', 'D', 'D', 'A']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['C', 'C', 'B', 'D']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['B', 'B', 'A', 'C']) # Room 1 (0 - top, 1 - bottom)
	# burrow.append(['D', 'A', 'C', 'A']) # Room 1 (0 - top, 1 - bottom)

	# print(burrow)
	# leave(4,10) 	# D
	# leave(4,0) 		# A
	# leave(3,9) 		# B
	# leave(3,7) 		# B
	# leave(3,1) 		# A
	# transfer(2,3) 	# C **
	# transfer(2,3) 	# C ***
	# leave(2,5) 		# B
	# leave(2,3) 		# D
	# enter(5,2) 		# B *
	# enter(7,2) 		# B **
	# enter(9,2) 		# B ***
	# transfer(4,3) 	# C ****
	# leave(4,9) 		# A
	# enter(3,4) 		# D *
	# transfer(1,2) 	# B ****
	# transfer(1,4) 	# D **
	# transfer(1,4) 	# D ***
	# enter(1,1) 		# A **
	# enter(0,1) 		# A ***
	# enter(9,1) 		# A ****
	# enter(10,4) 	# D ****
	# print(burrow)

	# -1-3-5-7-9-
	#   C B D D  => A B C D
	#   D C B A  => A B C D
	#   D B A C  => A B C D
	#   B C A A  => A B C D
	burrow.append(['C', 'D', 'D', 'B']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['B', 'C', 'B', 'C']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['D', 'B', 'A', 'A']) # Room 1 (0 - top, 1 - bottom)
	burrow.append(['D', 'A', 'C', 'A']) # Room 1 (0 - top, 1 - bottom)

	leave(3,10)
	leave(3,9)
	leave(3,0)
	leave(3,1)

	transfer(1,3)
	leave(2,3)
	transfer(2,3)
	leave(2,7)
	transfer(2,3)
	enter(3,2)
	enter(7,2)
	enter(9,2)

	visualize_burrow()

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "total_cost:", total_cost, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
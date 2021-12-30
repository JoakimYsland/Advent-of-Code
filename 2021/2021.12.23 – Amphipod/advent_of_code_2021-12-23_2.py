
# https://adventofcode.com/2021/day/23

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def is_hallway_clear(from_index, to_index, burrow): 
		a = min(from_index, to_index)
		b = max(from_index, to_index)
		occupied_slots = [e for e in burrow[0][a:b] if e != '']
		return len(occupied_slots) == 0

	def leave(from_room_index, hallway_index, burrow): 
		num_vacant = len([s for s in burrow[from_room_index] if s == ''])

		if num_vacant == len(burrow[from_room_index]): 
			return False, 0

		amphipod = burrow[from_room_index][num_vacant]
		if amphipod != 'A' and amphipod != 'B' and amphipod != 'C' and amphipod != 'D': 
			return False, 0

		burrow[from_room_index][num_vacant] = ''
		cost_exit_room = num_vacant + 1

		from_room_entrance_index = from_room_index * 2
		cost_hallway_move = abs(hallway_index - from_room_entrance_index)
		cost_final = (cost_exit_room + cost_hallway_move) * movement_cost[amphipod]
		# s = "Move {0} from R{1} to H{2}"
		# result = s.format(amphipod, from_room_index, hallway_index)

		if not is_hallway_clear(from_room_entrance_index, hallway_index, burrow): 
			# s = " – ERROR: Hallway {0} to {1} is blocked!"
			# result += s.format(from_room_entrance_index, hallway_index)
			return False, 0

		burrow[0][hallway_index] = amphipod

		return True, cost_final
	
	def enter(hallway_index, to_room_index, burrow): 
		amphipod = burrow[0][hallway_index]
		num_vacant = len([s for s in burrow[to_room_index] if s == ''])
		
		if num_vacant == 0: 
			return False, 0
		if amphipod == '': 
			return False, 0
		if to_room_index == 1 and amphipod != 'A': 
			return False, 0
		if to_room_index == 2 and amphipod != 'B': 
			return False, 0
		if to_room_index == 3 and amphipod != 'C': 
			return False, 0
		if to_room_index == 4 and amphipod != 'D': 
			return False, 0
		for a in burrow[to_room_index]: 
			if a != '' and a.upper() != amphipod: 
				return False, 0

		cost_enter_room = num_vacant

		to_room_entrance_index = to_room_index * 2
		cost_hallway_move = abs(hallway_index - to_room_entrance_index)
		cost_final = (cost_hallway_move + cost_enter_room) * movement_cost[amphipod]
		burrow[0][hallway_index] = ''
		# s = "Move {0} from H{1} to R{2}"
		# result = s.format(amphipod, hallway_index, to_room_index)

		burrow[to_room_index][num_vacant - 1] = amphipod.lower()

		if not is_hallway_clear(hallway_index, to_room_entrance_index, burrow): 
			# s = " – ERROR: Hallway {0} to {1} is blocked!"
			# result += s.format(hallway_index, to_room_entrance_index)
			return False, 0

		return True, cost_final

	def visualize_burrow(burrow): 
		print(str(burrow[0]).replace('\'\'', '-').replace('\'', '').replace(',', ''))
		for r in [list(x) for x in zip(*burrow[1:5])]: 
			print("    " + str(r).replace('\'\'', '\'-\'').replace('\'', '').replace(',', '  '))

	# --------------------------------------------------------------------------------

	# Test / Real – 44169 / !47191

	start_time_ms = round(time.time() * 1000)
	
	burrow_init = [['', '', '', '', '', '', '', '', '', '', '']] # Hallway (0 - left, 10 - right)
	movement_cost = { 'A': 1, 'B': 10, 'C': 100, 'D': 1000 }
	total_cost = 0

	# -1-3-5-7-9-
	#   C B D D  => A B C D
	#   D C B A  => A B C D
	#   D B A C  => A B C D
	#   B C A A  => A B C D
	burrow_init.append(['C', 'D', 'D', 'B']) # Room 1 (0 - top, 1 - bottom)
	burrow_init.append(['B', 'C', 'B', 'C']) # Room 1 (0 - top, 1 - bottom)
	burrow_init.append(['D', 'B', 'A', 'A']) # Room 1 (0 - top, 1 - bottom)
	burrow_init.append(['D', 'A', 'C', 'A']) # Room 1 (0 - top, 1 - bottom)

	lowest_score = 999999
	valid_hallway = [0,1,3,5,7,9,10]

	def try_stuff(burr, score): 

		nonlocal lowest_score
		if score >= lowest_score: 
			return

		# Enter
		for i in valid_hallway: 
			if burr[0][i] == '': 
					continue
			for j in range(1, 5): 
				b = deepcopy(burr)
				success, cost = enter(i,j, b)
				if success == True: 
					new_score = score + cost
					if new_score < lowest_score: 
						is_complete = len(''.join(b[0])) == 0
						if is_complete: 
							lowest_score = new_score
							print('lowest_score', lowest_score)
						else: 
							try_stuff(b, new_score)
				
		# Leave
		for j in valid_hallway: 
			if burr[0][j] != '': 
					continue
			for i in range(1, 5): 
				b = deepcopy(burr)
				success, cost = leave(i,j, b)
				if success == True: 
					new_score = score + cost
					if new_score < lowest_score: 
						try_stuff(b, new_score)
	
	try_stuff(burrow_init, 0)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "total_cost:", total_cost, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
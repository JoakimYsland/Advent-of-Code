
# https://adventofcode.com/2021/day/21

import time
import math
import re
from copy import deepcopy
from collections import deque

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	quantum_distribution = {
		3: 1, # 111
		4: 3, # 112, 121, 211
		5: 6, # 113, 131, 311, 122, 221, 212
		6: 7, # 123, 132, 213, 231, 321, 312, 222
		7: 6, # 133, 331, 313, 223, 232, 322
		8: 3, # 332, 323, 233
		9: 1, # 333
		}

	# --------------------------------------------------------------------------------

	# Test / Real – 444356092776315 / 133029050096658

	start_time_ms = round(time.time() * 1000)
	
	scoreboard = [0, 0]
	# games = { (4, 0, 8, 0): 1 }
	games = { (2, 0, 7, 0): 1 }
	p1_turn = True

	while len(games) > 0: 
		
		games_turn_start = games.copy()
		for game_state, count in games_turn_start.items(): 

			if p1_turn: p1, s1, p2, s2 = game_state
			else: 		p2, s2, p1, s1 = game_state

			for q_sum_rolls, q_count in quantum_distribution.items(): 

				new_pos = p1 + q_sum_rolls
				while new_pos > 10: 
					new_pos -= 10
				
				new_score = s1 + new_pos
				new_count = count * q_count

				if new_score >= 21: 
					if p1_turn: scoreboard[0] += new_count
					else: 		scoreboard[1] += new_count
				else: 
					if p1_turn: new_game_state = (new_pos, new_score, p2, s2)
					else: 		new_game_state = (p2, s2, new_pos, new_score)
					games.setdefault(new_game_state, 0)
					games[new_game_state] += new_count
			
			games[game_state] -= count

			if games[game_state] < 1: 
				del games[game_state]

		p1_turn = not p1_turn

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "scoreboard:", scoreboard, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
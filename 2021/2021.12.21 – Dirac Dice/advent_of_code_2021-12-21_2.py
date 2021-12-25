
# https://adventofcode.com/2021/day/20

import time
import math
import re
from copy import deepcopy
from collections import deque

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	# --------------------------------------------------------------------------------

	# Test / Real – 444356092776315 / ???

	start_time_ms = round(time.time() * 1000)
	
	# players = deque([
	# 	('Player 1', 4, 0), 
	# 	('Player 2', 8, 0), 
	# 	# ('Player 1', 2, 0), 
	# 	# ('Player 2', 7, 0), 
	# 	])
	scoreboard = { 'Player 1': 0, 'Player 2': 0 }

	quantum_distribution = {
		3: 1, # 111
		4: 3, # 112, 121, 211
		5: 6, # 113, 131, 311, 122, 221, 212
		6: 7, # 123, 132, 213, 231, 321, 312, 222
		7: 6, # 133, 331, 313, 223, 232, 322
		8: 3, # 332, 323, 233
		9: 1, # 333
		}
	
	games = { (4, 0, 8, 0): 1 }
	playing = True
	player = 1

	while playing: 
		playing = False
		for game_state, count in games.copy().items(): 
			if player == 1: p1, s1, p2, s2 = game_state
			else: 			p2, s2, p1, s1 = game_state

			my_print('game:', game_state, count)
			
			if count > 0: 
				for q_sum_rolls, q_count in quantum_distribution.items(): 

					new_pos = p1 + q_sum_rolls
					while new_pos > 10: 
						new_pos -= 10

					new_score = s1 + new_pos
					new_count = count * q_count

					if player == 1: new_game_state = (new_pos, new_score, p2, s2)
					else: 			new_game_state = (p2, s2, new_pos, new_score)

					games.setdefault(new_game_state, 0)
					my_print('new_game_state: ', new_game_state, new_count)
					
					if new_score >= 21: 
						if player == 1: scoreboard['Player 1'] += new_count
						else: 			scoreboard['Player 2'] += new_count
						games[new_game_state] = 0
					else: 
						games[new_game_state] += new_count
						playing = True

				games[game_state] = 0

		player = 1 if player == 2 else 2

	print(len(games))
	print(scoreboard)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	# print(run_title, "loser_value:", loser_value, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
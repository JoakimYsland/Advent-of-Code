
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

	# def dirac_dice(roll, rolls, players): 
	# 	players = deepcopy(players)
	# 	name, position, score = players[0]
	# 	position += roll

	# 	if rolls == 3: 
	# 		while position > 10: 
	# 			position -= 10
	# 		score += position
	# 		if score >= 21: 
	# 			scoreboard[name] += 1
	# 		else: 
	# 			players[0] = (name, position, score)
	# 			players.rotate(1)
	# 			dirac_dice(1, 1, players)
	# 			dirac_dice(2, 1, players)
	# 			dirac_dice(3, 1, players)
	# 	else: 
	# 		players[0] = (name, position, score)
	# 		rolls += 1
	# 		dirac_dice(1, rolls, players)
	# 		dirac_dice(2, rolls, players)
	# 		dirac_dice(3, rolls, players)

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

	# dirac_dice(1, 1, players)
	# dirac_dice(2, 1, players)
	# dirac_dice(3, 1, players)

	# print(scoreboard)

	quantum_distribution = {
		3: 1, # 3 = 111
		4: 3, # 4 = 112, 121, 211
		5: 6, # 5 = 113, 131, 311, 122, 221, 212
		6: 7, # 6 = 123, 132, 213, 231, 321, 312, 222
		7: 6, # 7 = 133, 331, 313, 223, 232, 322
		8: 3, # 8 = 332, 323, 233
		9: 1, # 9 = 333
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
				for k2,v2 in quantum_distribution.items(): 
					position = p1 + k2
					while position > 10: 
						position -= 10
					score = s1 + position
					if player == 1: new_key = (position, score, p2, s2)
					else: 			new_key = (p2, s2, position, score)
					games.setdefault(new_key, 0)

					my_print('new_key: ', new_key, v2 * count)
					
					if score >= 21: 
						if player == 1: scoreboard['Player 1'] += v2 * count
						else: 			scoreboard['Player 2'] += v2 * count
						games[new_key] = 0
					else: 
						games[new_key] += v2 * count
						playing = True

			games[game_state] = 0

		player = 1 if player == 2 else 2

	# print(games)
	print(scoreboard)

	# while not winner: 
	# 	for i in range(1, 1,101, 3): 
	# 		rolls = get_dice_roll() + get_dice_roll() + get_dice_roll()
	# 		name, position, score = players[0]

	# 		new_position = (position + rolls) % 10
	# 		if new_position == 0: 
	# 			new_position = 10

	# 		score += new_position
	# 		if score >= 21: 
	# 			print(name, 'wins! Score:', score)
	# 			winner = True
	# 			break
	# 		else: 
	# 			players[0] = (name, new_position, score)
	# 			players.rotate(1)

	# loser_value = players[1][2] * dice_rolls
	# print('loser_score:', players[1][2])
	# print('dice_rolls:', dice_rolls)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	# print(run_title, "loser_value:", loser_value, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
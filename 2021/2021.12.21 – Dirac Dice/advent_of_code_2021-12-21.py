
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

	def get_dice_roll(): 
		nonlocal dice
		nonlocal dice_rolls
		dice += 1
		dice_rolls += 1
		while dice > 100: 
			dice -= 100
		return dice

	# --------------------------------------------------------------------------------

	# Test / Real – ??? / ???

	start_time_ms = round(time.time() * 1000)
	
	winner = False
	dice_rolls = 0
	players = deque([
		('Player 1', 2, 0), 
		('Player 2', 7, 0)
		])
	dice = 0

	while not winner: 
		for i in range(1,101, 3): 
			rolls = get_dice_roll() + get_dice_roll() + get_dice_roll()
			name, position, score = players[0]

			new_position = (position + rolls) % 10
			if new_position == 0: 
				new_position = 10

			score += new_position
			if score >= 1000: 
				print(name, 'wins! Score:', score)
				winner = True
				break
			else: 
				players[0] = (name, new_position, score)
				players.rotate(1)

	loser_value = players[1][2] * dice_rolls
	print('loser_score:', players[1][2])
	print('dice_rolls:', dice_rolls)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "loser_value:", loser_value, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
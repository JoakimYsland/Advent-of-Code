
# https://adventofcode.com/2021/day/10

import statistics
from collections import deque
from collections import namedtuple

BracketScore = namedtuple("BracketScore", ['repair', 'error'])

def run(run_title, input_file):

	def get_repair_score(repairs): 
		repair_score = 0
		for bracket in repairs:
			repair_score *= 5
			repair_score += bracket_score[bracket].repair
		return repair_score
	
	# --------------------------------------------------------------------------------

	# Test / Real – 288957 / 3654963618

	opening_brackets = ['(', '[', '{', '<']
	corresponding_brackets = {
		'(':')', ')':'(', 
		'[':']', ']':'[', 
		'{':'}', '}':'{', 
		'<':'>', '>':'<', 
		}
	bracket_score = {
		')': BracketScore(1, 3), 
		']': BracketScore(2, 57), 
		'}': BracketScore(3, 1197), 
		'>': BracketScore(4, 25137), 
	}
	syntax_error_score = 0
	repair_scores = []

	for line in input_file: 
		chunks = deque()
		is_corrupted = False
		for bracket in [b for b in line.strip()]:
			if bracket in opening_brackets: 
				chunks.append(bracket)
			else: 
				if bracket == corresponding_brackets[chunks[-1]]:
					chunks.pop()
				else: 
					syntax_error_score += bracket_score[bracket].error
					is_corrupted = True
					break
		if not is_corrupted: 
			repairs = []
			chunks.reverse()
			for bracket in chunks:
				repairs.append(corresponding_brackets[bracket])
			repair_score = get_repair_score(repairs)
			repair_scores.append(repair_score)

	print(run_title, "syntax_error_score:", syntax_error_score)
	print(run_title, "repair_score:", statistics.median(repair_scores))

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
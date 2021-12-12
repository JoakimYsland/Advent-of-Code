
# https://adventofcode.com/2021/day/11

# import statistics
# from collections import deque
# from collections import namedtuple

# BracketScore = namedtuple("BracketScore", ['repair', 'error'])

def run(run_title, input_file):

	# def get_repair_score(repairs): 
	# 	repair_score = 0
	# 	for bracket in repairs:
	# 		repair_score *= 5
	# 		repair_score += bracket_score[bracket].repair
	# 	return repair_score
	
	# --------------------------------------------------------------------------------

	# Test / Real – 1656 / ???

	# opening_brackets = ['(', '[', '{', '<']
	# corresponding_brackets = {
	# 	'(':')', ')':'(', 
	# 	'[':']', ']':'[', 
	# 	'{':'}', '}':'{', 
	# 	'<':'>', '>':'<', 
	# 	}
	# bracket_score = {
	# 	')': BracketScore(1, 3), 
	# 	']': BracketScore(2, 57), 
	# 	'}': BracketScore(3, 1197), 
	# 	'>': BracketScore(4, 25137), 
	# }
	# syntax_error_score = 0
	# repair_scores = []
	steps = 100
	flashes = 0
	octopi = []

	for line in input_file: 
		octopi.append([int(o) for o in line.strip()])


	print(run_title, "flashes:", flashes)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
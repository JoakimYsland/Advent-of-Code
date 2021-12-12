
# https://adventofcode.com/2021/day/10

import re # Split string with multiple delimiters
import math
from collections import deque
from collections import namedtuple

# Vec2 = namedtuple("Vec2", ['x', 'y'])

def run(run_title, input_file):

	def is_matching_bracket(open, close): 
		if open == '(' and close == ')': return True
		if open == '[' and close == ']': return True
		if open == '{' and close == '}': return True
		if open == '<' and close == '>': return True
		return False

	def get_syntax_error_score(illegal_bracket): 
		if (illegal_bracket == ')'): return 3
		if (illegal_bracket == ']'): return 57
		if (illegal_bracket == '}'): return 1197
		if (illegal_bracket == '>'): return 25137
		return 0

	# --------------------------------------------------------------------------------

	# Test / Real – 26397 / 299793

	opening_brackets = ['(', '[', '{', '<']
	syntax_error_score = 0

	for line in input_file: 
		chunks = deque()
		for char in [c for c in line]:
			if char in opening_brackets: 
				chunks.append(char)
			else: 
				if is_matching_bracket(chunks[-1], char):
					chunks.pop()
				else: 
					syntax_error_score += get_syntax_error_score(char)
					break

	print(run_title, "syntax_error_score:", syntax_error_score)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())

# https://adventofcode.com/2021/day/18

# import re
import time
import math

class SFNum: 
	def __init__(self, depth, value): 
		self.depth = depth
		self.value = value

	def __repr__(self): 
		return "({0},{1})".format(str(self.depth), str(self.value))

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def add_sequences(sequence_1, sequence_2): 
		new_sequence = sequence_1 + sequence_2
		for sfnum in new_sequence: 
			sfnum.depth += 1
		return new_sequence

	def get_sequence_from_line(line): 
		sequence = []
		depth = 0
		for i, c in enumerate(line): 
			if 	 c == '[': depth += 1
			elif c == ']': depth -= 1
			elif c == ',': continue
			else: 
				sequence.append(SFNum(depth, int(c)))
		return sequence

	def reduce_sequence(sequence):
		
		my_print('REDUCE =>', sequence)
		my_print('––––––––––')

		reduced = False
		while not reduced: 
			state = 'IDLE'
			for i, sfnum in enumerate(sequence): 
				if sfnum.depth > 4: 
					state = 'EXPLODE'
					if i > 0: 
						sequence[i-1].value += sequence[i].value
					if i + 2 < len(sequence): 
						sequence[i+2].value += sequence[i+1].value
					sfnum.depth -=1
					sfnum.value = 0
					sequence.pop(i+1)
					break
			if state == 'IDLE': 
				for i, sfnum in enumerate(sequence): 
					if sfnum.value > 9: 
						state = 'SPLIT'
						v1 = int(sfnum.value / 2)
						v2 = int((sfnum.value / 2) + 0.5)
						sfnum.depth += 1
						sfnum.value = v1
						sequence.insert(i+1, SFNum(sfnum.depth, v2))
						break

			if state == 'IDLE': 
				reduced = True
			else: 
				my_print(state, '=>', sequence)
		
		return sequence
				
		my_print('––––––––––')
	
	def get_magnitude(sequence):

		while len(sequence) > 1: 
			for i in range(0, len(sequence) - 1):
				left  = sequence[i]
				right = sequence[i+1]
				if left.depth == right.depth: 
					left.depth -= 1
					left.value = (left.value * 3) + (right.value * 2)
					sequence.pop(i+1)
					break
		return sequence[0].value

	# --------------------------------------------------------------------------------

	# Test / Real – 4140 / 3734

	start_time_ms = round(time.time() * 1000)

	num_hits = 0
	sequence = get_sequence_from_line(input_file[0].strip())

	for i in range(1, len(input_file)): 
		next_sequence = get_sequence_from_line(input_file[i].strip())
		sequence = add_sequences(sequence, next_sequence)
		sequence = reduce_sequence(sequence)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	print(get_sequence_from_line('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'))
	print(sequence)
	print(get_magnitude(sequence))
	print(run_title, "magnitude:", get_magnitude(sequence), ('(' + str(total_time) + "ms)"))
	print('––––––––––')

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
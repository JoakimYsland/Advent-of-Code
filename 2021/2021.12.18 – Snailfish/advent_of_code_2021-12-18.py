
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
	print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	# def reconstruct_sequence(sequence): 
	# 	depth = 0
	# 	# depth_streak = 0
	# 	prev_depth_change
	# 	reconstruction = ''
	# 	for i, sfnum in enumerate(sequence): 
	# 		depth_change = sfnum.depth - depth
	# 		if depth_change > 0: 
	# 			depth_streak = 1
	# 			reconstruction += '[' * depth_change
	# 		elif depth_change < 0: 
	# 			depth_streak = 1
	# 			reconstruction += ']' * abs(depth_change)
	# 		# else: 
	# 		# 	depth_streak += 1
	# 		# 	reconstruction += ']'

	# 		# if depth_streak % 2 == 0: 
	# 		# 	reconstruction += '],['
	# 		# if depth_streak % 2 == 1: 
	# 		# 	reconstruction += '],['


	# 		reconstruction += str(sfnum.value)

	# 		if depth_change == 0: 
	# 			reconstruction += ']'

	# 		# if depth_streak > 1: 
	# 			# reconstruction += ')'

	# 		# else: reconstruction += '],['
	# 		# if not depth_change <= 0: 
	# 		# reconstruction += ','
	# 		# if depth_change == 0: reconstruction += ']'
	# 		prev_depth_change = depth
	# 		depth = sfnum.depth
	# 	return reconstruction

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

	def reduce_line(line):
		
		sequence = get_sequence_from_line(line)
		
		print(line)
		print(sequence)
		print('––––––––––')

		done = False
		while not done: 
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
				elif sfnum.value > 9: 
					state = 'SPLIT'
					v1 = int(sfnum.value / 2)
					v2 = int((sfnum.value / 2) + 0.5)
					sfnum.depth += 1
					sfnum.value = v1
					sequence.insert(i+1, SFNum(sfnum.depth, v2))
					break

			if state == 'IDLE': 
				done = True
			else: 
				print(sequence, '–', state)
				
		print('––––––––––')

	# --------------------------------------------------------------------------------

	# Test / Real – 112 / 1908

	start_time_ms = round(time.time() * 1000)

	num_hits = 0

	for line in input_file: 
		reduce_line(line.strip())

	# # r = 100 # 447
	# # r = 200 # 753
	# # r = 250 # 1068
	# r = 300 # 1908

	# for x in range(0, r): 
	# 	velocity_x = x
	# 	for y in range(-r, r): 
	# 		velocity_y = y
	# 		velocity_str = str(velocity_x) + ',' + str(velocity_y)
	# 		probe = Probe(0, 0, velocity_x, velocity_y)
	# 		probe_status = 'VALID'
	# 		while probe_status == 'VALID': 
	# 			probe.update()
	# 			if probe.is_out_of_bounds(target_area): 
	# 				# print('Probe', velocity_str, '- Probe out of bounds (', probe.position, ')')
	# 				probe_status = 'OOB'
	# 			else: 
	# 				if probe.is_in_target_area(target_area): 
	# 					# print('Probe', velocity_str, '- Collision! (', probe.position, ')')
	# 					probe_status = 'HIT'
	# 		if probe_status == 'HIT': 
	# 			num_hits += 1

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	# print('––––––––––')
	# print(run_title, "num_hits:", num_hits, ('(' + str(total_time) + "ms)"))
	# print('––––––––––')

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
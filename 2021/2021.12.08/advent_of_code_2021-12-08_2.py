
# https://adventofcode.com/2021/day/8

import re # Split string with multiple delimiters

# --------------------------------------------------------------------------------

# Test / Real – 61229 / ???

# 0: 123-456 = 6
# 1: --3--5- = 2 *
# 2: 1-345-7 = 5
# 3: 1-34-67 = 5
# 4: -234-6- = 4 *
# 5: 12-4-67 = 5
# 6: 12-4567 = 6
# 7: 1-3--6- = 3 *
# 8: 1234567 = 7 *
# 9: 1234-67 = 6

def subtract_segments(subtraction, string):
	return re.sub('[' + subtraction + ']', '', string)

def get_shared_segments(patterns):
	joined = ''.join(patterns)
	shared = (c for c in joined if joined.count(c) == len(patterns))
	return ''.join(set(shared))

def run(run_title, input_file):

	for line in input_file:
		solution = [''] * 7
		entry = line.split(' | ')
		signal_patterns = entry[0].split(' ')
		output_value = entry[1].strip().split(' ')

		pattern_dict = {}
		for pattern in signal_patterns:
			pattern_dict.setdefault(len(pattern), []).append(pattern)
		
		solution[0] = subtract_segments(pattern_dict[2][0], pattern_dict[3][0]) # 7-1

		t = get_shared_segments(pattern_dict[5]) # 2/3/5
		t = subtract_segments(pattern_dict[4][0], t) # 4
		t = subtract_segments(pattern_dict[3][0], t) # 7
		solution[6] = t

		t = get_shared_segments(pattern_dict[5]) # 2/3/5
		t = subtract_segments(pattern_dict[3][0], t) # -7
		t = subtract_segments(solution[6], t)
		solution[3] = t

		t = pattern_dict[4][0] # 4
		t = subtract_segments(pattern_dict[2][0], t) # 1
		t = subtract_segments(solution[3], t)
		solution[1] = t

		t = pattern_dict[7][0] # 8
		t = subtract_segments(get_shared_segments(pattern_dict[5]), t) # 2/3/5
		t = subtract_segments(pattern_dict[4][0], t) # 4
		solution[4] = t

		t = get_shared_segments(pattern_dict[6]) # 0/6/9
		t = subtract_segments(''.join(solution), t)
		solution[5] = t

		solution[2] = subtract_segments(''.join(solution), 'abcdefg')

		mapping = [
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,1,2,  4,5,6])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [    2,    5  ])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,  2,3,4,  6])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,  2,3,  5,6])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [1,  2,3,  5  ])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,1,  3,  5,6])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,1,  3,4,5,6])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,  2,    5  ])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,1,2,3,4,5,6])), 
			''.join(sorted(s for i, s in enumerate(solution) if i in [0,1,2,3,  5,6])), 
		]

		print(signal_patterns, output_value)
		print(solution)
		print(mapping)

	# print(run_title, "unique_segment_digits:", unique_segment_digits)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())

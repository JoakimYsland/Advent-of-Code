
# https://adventofcode.com/2021/day/8

# import re # Split string with multiple delimiters

# --------------------------------------------------------------------------------

# Test / Real – 26 / ???

# 0: 123-456 = 6
# 1: --3--5- = 2
# 2: 1-345-7 = 5
# 3: 1-34-67 = 5
# 4: -234-6- = 4
# 5: 12-4-67 = 5
# 6: 12-4567 = 6
# 7: 1-3--6- = 3
# 8: 1234567 = 7
# 9: 1234-67 = 6

def run(run_title, input_file):

	# Given n number of segments, which segment
	# could the potential digits not fill
	asd = [
		[0,1,2,3,4,5,6], 	# 0
		[0,1,2,3,4,5,6], 	# 1
		[0,1,3,4,6], 		# 2
		[1,3,4,6], 			# 3
		[0,4,6], 			# 4
		[], 				# 5
		[], 				# 6
		[], 				# 7
	]

	for line in input_file:
		mapping = ['abcdefg'] * 7
		entry = line.split(' | ')
		signal_patterns = entry[0].split(' ')
		output_value = entry[1].strip().split(' ')
		
		for pattern in signal_patterns:
			for i in asd[len(pattern)]:
				for char in pattern: 
					mapping[i] = mapping[i].replace(char, '')
		
		print(signal_patterns, output_value)
		print(mapping)

	# print(run_title, "least_fuel_consumption:", least_fuel_consumption)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())

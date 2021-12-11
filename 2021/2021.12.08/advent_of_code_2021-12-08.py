
# https://adventofcode.com/2021/day/8

# import statistics

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
	
	# asd = [
	# 	[0,1,2,4,5,6], 		# 0
	# 	[2,5], 				# 1
	# 	[0,2,3,4,6], 		# 2
	# 	[0,2,3,5,6], 		# 3
	# 	[1,2,3,5], 			# 4
	# 	[0,1,3,5,6], 		# 5
	# 	[0,1,3,4,5,6], 		# 6
	# 	[0,2,5], 			# 7
	# 	[0,1,2,3,4,5,6], 	# 8
	# 	[0,1,2,3,5,6], 		# 9
	# ]

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
		# [], 				# 0
		# [], 				# 1
		# [2,5], 				# 2
		# [0,2,5], 			# 3
		# [1,2,3,5], 			# 4
		# [0,1,2,3,4,5,6], 	# 5
		# [0,1,2,3,4,5,6], 	# 6
		# [0,1,2,3,4,5,6], 	# 7
	]

	for line in input_file:
		mapping = [['a','b','c','d','e','f','g']] * 7
		entry = line.split(' | ')
		signal_patterns = entry[0].split(' ')
		output_value = entry[1].strip().split(' ')
		print(signal_patterns, output_value)
		for pattern in signal_patterns:
			for i in asd[len(pattern)]:
				print("1", mapping)
				for segment in [char for char in pattern]: 
					if segment in mapping[i]:
						mapping[i].remove(segment)
				print("2", mapping)
		print(mapping)

	# print(run_title, "least_fuel_consumption:", least_fuel_consumption)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())

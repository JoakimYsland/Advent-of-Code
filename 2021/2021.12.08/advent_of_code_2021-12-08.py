
# https://adventofcode.com/2021/day/8

# --------------------------------------------------------------------------------

# Test / Real – 26 / 456

def run(run_title, input_file):

	unique_segment_digits = 0

	for line in input_file:
		entry = line.split(' | ')
		signal_patterns = entry[0].split(' ')
		output_value = entry[1].strip().split(' ')

		for pattern in output_value:
			if len(pattern) in [2,4,3,7]:
				unique_segment_digits += 1

	print(run_title, "unique_segment_digits:", unique_segment_digits)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())

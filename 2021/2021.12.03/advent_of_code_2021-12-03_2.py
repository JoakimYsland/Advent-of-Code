
# https://adventofcode.com/2021/day/3

input_file = open('input.txt', 'r').readlines()

def check_oxygen(bit_balance, bit): 
	if (bit == '1' and bit_balance >= 0): return True
	if (bit == '0' and bit_balance < 0): return True
	return False

def check_co2(bit_balance, bit): 
	if (bit == '1' and bit_balance < 0): return True
	if (bit == '0' and bit_balance >= 0): return True
	return False

def get_rating(lines, comparator, bits_per_line):
	lines = lines.copy()
	for bit in range(0, bits_per_line, 1):
		bit_balance = 0
		for line in lines.values(): 
			bit_balance += 1 if line[bit] == '1' else -1

		for key in list(lines.keys()):
			is_match = comparator(bit_balance, lines[key][bit])
			if not is_match and len(lines) > 1:
				del lines[key]

	rating_string = ''.join(list(lines.values())[0])
	return int(rating_string, 2)

# --------------------------------------------------------------------------------

lines = { i:[char for char in input_file[i] if char.isdigit()] for i in range(0, len(input_file))}
bits_per_line = len(lines[0])

oxygen_generator_rating = get_rating(lines, check_oxygen, bits_per_line)
co2_scrubber_rating = get_rating(lines, check_co2, bits_per_line)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print("oxygen_generator_rating:", oxygen_generator_rating)
print("co2_scrubber_rating:", co2_scrubber_rating)
print("life_support_rating:", life_support_rating)

# oxygen_generator_rating: 825
# co2_scrubber_rating: 3375
# life_support_rating: 2784375

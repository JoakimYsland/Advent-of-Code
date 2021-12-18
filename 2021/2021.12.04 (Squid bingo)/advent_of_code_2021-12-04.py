
# https://adventofcode.com/2021/day/4

def check_for_bingo(board, drawn_numbers):

	def line_is_bingo(line):
		is_bingo = True
		for n in line:
			if not n in drawn_numbers: 
				is_bingo = False
		if is_bingo: 
			print("Bingo!", line)
			return True
		return False

	for row in board: 
		if line_is_bingo(row): 
			return True
	for i in range(0, 5, 1):
		column = [n for row in board for (col, n) in enumerate(row) if col == i]
		if line_is_bingo(column): 
			return True
	return False

# --------------------------------------------------------------------------------

def run():
	input_file = open('input.txt', 'r').readlines()
	number_pool = [int(n.strip()) for n in input_file[0].split(',')]
	boards = [[]]
	drawn_numbers = []

	for line in input_file[2:]: 
		numbers = [int(n.strip()) for n in line.split(' ') if n.strip().isdigit()]

		if (len(numbers) == 0):
			boards.append([])
			continue

		boards[-1].append(numbers)

	for i in range(0, len(number_pool), 1):
		drawn_numbers.append(number_pool[i])
		print("drawn_numbers:", drawn_numbers)
		for board in boards: 
			is_bingo = check_for_bingo(board, drawn_numbers)
			if (is_bingo): 
				sum_of_unmarked_numbers = sum(n for row in board for n in row if not n in drawn_numbers)
				print("Answer", sum_of_unmarked_numbers * drawn_numbers[-1])
				return

run()
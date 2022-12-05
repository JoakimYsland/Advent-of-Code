
# https://adventofcode.com/2022/day/5

import string

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

parsing_stacks = True
stacks = []

for line in input_file:

	line = line.rstrip()

	if len(line) == 0: 
		parsing_stacks = False
		continue

	# Parse initial stacks
	if parsing_stacks: 
		for i, crate in enumerate(line):
			if i % 4 == 1 and str.isalpha(crate): 
				column = int((i - 1) / 4)
				while column > len(stacks) - 1:
					stacks.append([])
				stacks[column].insert(0, crate)

	# Perform instructions
	else:
		words = line.split(' ')
		num_crates = int(words[1])
		from_col = int(words[3]) - 1
		to_col = int(words[5]) - 1

		for i in range(0, num_crates, 1): 
			crate = stacks[from_col].pop(-1)
			stacks[to_col].append(crate)

# Generate message
message = ""
for stack in stacks:
	message += stack[-1]

print("stacks:", stacks)
print("message:", message)
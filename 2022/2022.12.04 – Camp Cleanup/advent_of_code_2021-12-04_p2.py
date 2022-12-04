
# https://adventofcode.com/2022/day/4

import string

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

overlaps = 0

for line in input_file:

	line = line.rstrip()

	elves = line.split(',')
	elf_1 = [int(v) for v in elves[0].split('-')]
	elf_2 = [int(v) for v in elves[1].split('-')]

	if elf_1[0] >= elf_2[0] and elf_1[1] <= elf_2[1]: 
		overlaps += 1
	elif elf_2[0] >= elf_1[0] and elf_2[1] <= elf_1[1]: 
		overlaps += 1

print("overlaps:", overlaps)
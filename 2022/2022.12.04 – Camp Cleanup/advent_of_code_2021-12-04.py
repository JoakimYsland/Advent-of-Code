
# https://adventofcode.com/2022/day/4

import string
import re
from collections import namedtuple

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

Elf = namedtuple("Elf", 'start end')
overlaps = 0

for line in input_file:

	line = line.rstrip()
	line = re.split("-|,", line)

	elf_1 = Elf(int(line[0]), int(line[1]))
	elf_2 = Elf(int(line[2]), int(line[3]))

	if elf_1.start >= elf_2.start and elf_1.start <= elf_2.end: 
		overlaps += 1
	elif elf_2.start >= elf_1.start and elf_2.start <= elf_1.end: 
		overlaps += 1

print("overlaps:", overlaps)
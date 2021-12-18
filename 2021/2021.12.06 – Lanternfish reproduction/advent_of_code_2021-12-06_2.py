
# https://adventofcode.com/2021/day/6

from collections import deque

# --------------------------------------------------------------------------------

# Test / Real – 26984457539 / 1622533344325

def run(run_title, input_file):
	input_fish = [int(f) for f in input_file[0].split(',')]
	fish_data = deque([0] * 9)

	for fish in input_fish:
		fish_data[fish] += 1
	
	for day in range(0, 256):
		fish_data.rotate(-1)
		fish_data[6] += fish_data[-1]

	print(run_title, "Fish Count:", sum(fish_data))

run("[Test Data]", open('input_test.txt', 'r').readlines())
run("[Real Data]", open('input.txt', 'r').readlines())
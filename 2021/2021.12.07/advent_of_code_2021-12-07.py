
# https://adventofcode.com/2021/day/7

import statistics

# --------------------------------------------------------------------------------

# Test / Real – 37 / 326132

def run(run_title, input_file):
	crab_submarines = [int(f) for f in input_file[0].split(',')]
	least_fuel_consumption = 0

	crab_submarines.sort()
	median_position = int(statistics.median(crab_submarines))

	for sub_pos in crab_submarines: 
		least_fuel_consumption += abs(sub_pos - median_position)

	print(run_title, "least_fuel_consumption:", least_fuel_consumption)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())

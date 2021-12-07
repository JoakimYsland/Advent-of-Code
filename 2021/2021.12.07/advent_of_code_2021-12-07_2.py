
# https://adventofcode.com/2021/day/7

import statistics

# --------------------------------------------------------------------------------

# Test / Real – 168(5) / ???

def run(run_title, input_file):
	crab_submarines = [int(f) for f in input_file[0].split(',')]

	crab_data = {}
	for pos in crab_submarines: 
		crab_data[pos] = crab_data[pos] + 1 if pos in crab_data else 1
	
	least_fuel_consumption = -1
	least_fuel_consumption_pos = -1

	for pos in range(min(crab_submarines), max(crab_submarines)): 
		# print("Evaluation position", pos)
		fuel_consumption = 0
		for crab_pos in crab_data.keys(): 
			num_crabs = crab_data[crab_pos]
			pos_from = min(pos, crab_pos)
			pos_to = max(pos, crab_pos)
			fuel_steps = [p + 1 - pos_from for p in range(pos_from, pos_to)]
			fuel_consumption += sum(fuel_steps) * num_crabs
			# print(crab_pos, fuel_steps, "=", sum(fuel_steps))

		if (least_fuel_consumption == -1 or fuel_consumption < least_fuel_consumption):
			least_fuel_consumption = fuel_consumption
			least_fuel_consumption_pos = pos

	print(run_title, "least_fuel_consumption:", least_fuel_consumption)
	print(run_title, "least_fuel_consumption_pos:", least_fuel_consumption_pos)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
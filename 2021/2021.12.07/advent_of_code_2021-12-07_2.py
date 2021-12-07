
# https://adventofcode.com/2021/day/7

def evaluate_position(target_pos, crab_data):
	fuel = 0
	for crab_pos in crab_data.keys(): 
		num_crabs = crab_data[crab_pos]
		dist = abs(target_pos - crab_pos)
		fuel += int(dist * (dist + 1) / 2) * num_crabs # https://www.mathsisfun.com/algebra/triangular-numbers.html
	return fuel

# --------------------------------------------------------------------------------

# Test / Real – 168(5) / 88612508(447)

def run(run_title, input_file):
	crab_submarines = [int(f) for f in input_file[0].split(',')]

	crab_data = {}
	for p in crab_submarines: 
		crab_data[p] = crab_data[p] + 1 if p in crab_data else 1

	pos_min, pos_max = min(crab_submarines), max(crab_submarines)
	best_fuel = evaluate_position(pos_min, crab_data)
	best_position = pos_min

	for eval_pos in range(pos_min, pos_max): 
		fuel = evaluate_position(eval_pos, crab_data)
		if (fuel < best_fuel):
			best_fuel = fuel
			best_position = eval_pos

	print(run_title, "best_fuel:", best_fuel)
	print(run_title, "best_position:", best_position)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
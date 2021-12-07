
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
	for pos in crab_submarines: 
		crab_data[pos] = crab_data[pos] + 1 if pos in crab_data else 1
	
	fuel_consumption = -1
	position = -1

	for pos in range(min(crab_submarines), max(crab_submarines)): 
		fuel = evaluate_position(pos, crab_data)
		if (fuel_consumption == -1 or fuel < fuel_consumption):
			fuel_consumption = fuel
			position = pos

	print(run_title, "fuel_consumption:", fuel_consumption)
	print(run_title, "position:", position)

run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
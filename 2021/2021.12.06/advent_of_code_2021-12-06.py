
# https://adventofcode.com/2021/day/5

# --------------------------------------------------------------------------------

# Test: 	5934
# Answer: 	358214

def run(run_title, input_file):
	lantern_fishies = [int(f) for f in input_file[0].split(',')]
	reprod_cycle = 6
	simulation_days = 80
	
	for day in range(0, simulation_days):
		fish_count_at_day_start = len(lantern_fishies)
		for i in range(0, fish_count_at_day_start):
			if (lantern_fishies[i] == 0):
				lantern_fishies[i] = reprod_cycle
				lantern_fishies.append(reprod_cycle + 2)
			else:
				lantern_fishies[i] -= 1

	print(run_title, "lantern_fishies:", len(lantern_fishies))

run("[Test Run]", open('input_test.txt', 'r').readlines())
run("[Real Data]", open('input.txt', 'r').readlines())
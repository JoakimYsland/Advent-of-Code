
# https://adventofcode.com/2022/day/2

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

input_remap = {
	"A": 1, 
	"B": 2, 
	"C": 3, 
	"X": 1, 
	"Y": 2, 
	"Z": 3, 
	}

result_remap = { 
	0: 3, # Draw
	1: 0, # Lose
	2: 6, # Win
	}

victory_points = 0

def wrap(val, start, limit): 
	return start + (val - start) % (limit - start)

for line in input_file:

	line = line.rstrip()
	a, b = line.split(' ')
	a = input_remap[a]
	b = input_remap[b]

	r = wrap(a-b, 0, 3)
	victory_points += result_remap[r] + b

print("victory_points:", victory_points)
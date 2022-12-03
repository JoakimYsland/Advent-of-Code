
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

victory_points = 0

def wrap(val, start, limit): 
	return start + (val - start) % (limit - start)

for line in input_file:

	line = line.rstrip()
	a, b = line.split(' ')
	a = input_remap[a]
	b = input_remap[b]

	# Points for shape
	if   b == 1: victory_points += wrap(a-1, 1, 4)	# Lose
	elif b == 2: victory_points += a 				# Draw
	elif b == 3: victory_points += wrap(a+1, 1, 4) 	# Win

	# Points from result
	victory_points += (b - 1) * 3

print("victory_points:", victory_points)
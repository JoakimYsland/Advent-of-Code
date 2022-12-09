
# https://adventofcode.com/2022/day/9

import string

# input_file = open('test_input_p2.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

class Pos: 
	def __init__(self, x, y): 
		self.x = x
		self.y = y
	
	def __str__(self):
		s = "{0},{1}"
		return s.format(self.x, self.y)

def update_knot(knot, parent): 
	delta = Pos(parent.x - knot.x, parent.y - knot.y)
	delta_clamped = Pos(
		max(-1, min(delta.x, 1)), 
		max(-1, min(delta.y, 1)), 
	)

	if delta.x != 0 and delta.y != 0: # Diagonal
		if abs(delta.x) > 1 or abs(delta.y) > 1: # Gap
			knot.x += delta_clamped.x
			knot.y += delta_clamped.y
	elif abs(delta.x) > 1: # Horizontal
		knot.x += delta_clamped.x
	elif abs(delta.y) > 1: # Vertical
		knot.y += delta_clamped.y

head = Pos(0,0)
tail = Pos(0,0)
rope = [
	head, 
	Pos(0,0), 
	Pos(0,0), 
	Pos(0,0), 
	Pos(0,0), 
	Pos(0,0), 
	Pos(0,0), 
	Pos(0,0), 
	Pos(0,0), 
	tail, 
]

tail_positions_visited = []

for line in input_file:

	line = line.rstrip()
	direction, distance = line.split(' ')
	distance = int(distance)

	for step in range(0, distance, 1): 

		if direction == 'R':   head.x += 1
		elif direction == 'L': head.x -= 1
		elif direction == 'U': head.y += 1
		elif direction == 'D': head.y -= 1

		for i in range(1, len(rope), 1): 
			update_knot(rope[i], rope[i-1])

		tail_positions_visited.append(str(tail))

		# delta = Pos(head.x - tail.x, head.y - tail.y)
		# s = "{0} / {1} ({2})"
		# print(s.format(head, tail, delta))

print("tail_positions_visited:", len(set(tail_positions_visited)))

# https://adventofcode.com/2021/day/17

# import re
import time
import math

# https://scipython.com/book2/chapter-4-the-core-python-language-ii/examples/a-2d-vector-class/
class Vec2: 
	def __init__(self, x, y): 
		self.x = x
		self.y = y

	def __str__(self):
		return str(self.x) + ", " + str(self.y)

	def __add__(self, other):
		return Vec2(self.x + other.x, self.y + other.y)

class Probe: 
	def __init__(self, position_x, position_y, velocity_x, velocity_y): 
		self.position = Vec2(position_x, position_y)
		self.velocity = Vec2(velocity_x, velocity_y)
		self.path = [Vec2(0,0)]

	def update(self): 
		self.position += self.velocity
		self.path.append(self.position)
		if self.velocity.x > 0: self.velocity.x -= 1
		if self.velocity.x < 0: self.velocity.x += 1
		self.velocity.y -= 1

	def is_in_target_area(self, area):
		p = self.position
		return p.x >= area[0] and p.x <= area[1] and p.y >= area[2] and p.y <= area[3]

	def is_out_of_bounds(self, area): 
		return self.position.x > area[1] or self.position.y < area[2]

def my_print(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	# target_area = [20, 30, -10, -5]
	target_area = [241, 273, -97, -63]

	# --------------------------------------------------------------------------------

	# Test / Real – 112 / 1908

	start_time_ms = round(time.time() * 1000)

	num_hits = 0

	# r = 100 # 447
	# r = 200 # 753
	# r = 250 # 1068
	r = 300 # 1908

	for x in range(0, r): 
		velocity_x = x
		for y in range(-r, r): 
			velocity_y = y
			velocity_str = str(velocity_x) + ',' + str(velocity_y)
			probe = Probe(0, 0, velocity_x, velocity_y)
			probe_status = 'VALID'
			while probe_status == 'VALID': 
				probe.update()
				if probe.is_out_of_bounds(target_area): 
					# print('Probe', velocity_str, '- Probe out of bounds (', probe.position, ')')
					probe_status = 'OOB'
				else: 
					if probe.is_in_target_area(target_area): 
						# print('Probe', velocity_str, '- Collision! (', probe.position, ')')
						probe_status = 'HIT'
			if probe_status == 'HIT': 
				num_hits += 1

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	print(run_title, "num_hits:", num_hits, ('(' + str(total_time) + "ms)"))
	print('––––––––––')

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
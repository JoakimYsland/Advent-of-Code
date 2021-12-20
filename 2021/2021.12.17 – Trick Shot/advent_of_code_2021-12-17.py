
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

	def check_collision(self, area): 
		if self.position.x >= area[0] and self.position.x <= area[1]: 
			if self.position.y >= area[2] and self.position.y <= area[3]: 
				return True
		return False

def my_print(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	# target_area = [20, 30, -10, -5]
	target_area = [241, 273, -97, -63]

	# --------------------------------------------------------------------------------

	# Test / Real – n/a / 13476220616073 (2ms)

	start_time_ms = round(time.time() * 1000)

	probes = []

	init_velocity_x = 1

	for i in range(1, 100): 
		triangle_number = int(i * (i + 1) / 2) # https://www.mathsisfun.com/algebra/triangular-numbers.html
		if triangle_number > target_area[0]: 
			if triangle_number < target_area[1]: 
				init_velocity_x = i
				break

	print('init_velocity_x:', init_velocity_x)

	for i in range(1, 100):
		probes.append(Probe(0, 0, init_velocity_x, i))

	while len(probes) > 0: 
		for i, probe in enumerate(probes.copy()): 
			probe.update()

			if probe.position.x > target_area[1] or probe.position.y < target_area[2]: 
				print(probe.position, '- Probe out of bounds')
				probes.pop(i)
			else: 
				if probe.check_collision(target_area): 
					peak = 0
					for pos in probe.path: 
						if pos.y > peak: 
							peak = pos.y
					print(probe.position, '- Collision!', 'Peak:', peak)
					probes.pop(i)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	# print('––––––––––')
	# print(run_title, "sum_packet_version:", sum_packet_version, ('(' + str(total_time) + "ms)"))
	# print(run_title, "op_value_final:", op_value_final, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
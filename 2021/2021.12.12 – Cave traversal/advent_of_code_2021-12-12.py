
# https://adventofcode.com/2021/day/12

# import statistics
# from collections import deque
# from collections import namedtuple

# Vec2 = namedtuple("Vec2", ['x', 'y'])

def run(run_title, input_file):

	def can_visit(path, cave):
		is_small_cave = not cave[0].isupper()
		return not is_small_cave or (is_small_cave and not cave in path)

	def traverse(path):
		for connection in network[path[-1]]: 
			if connection == 'end': 
				new_path = path.copy() + [connection]
				paths.append(new_path)
			else: 
				if can_visit(path, connection):
					new_path = path.copy() + [connection]
					traverse(new_path)

	# --------------------------------------------------------------------------------

	# Test / Real – 19 / 4749

	total_paths = 0
	network = {}
	paths = []

	for line in input_file: 
		caves = line.strip().split('-')
		for i, cave in enumerate(caves):
			if not cave in network:
				network[cave] = []
			opposite = caves[i-1]
			if not opposite in network[cave] and opposite != 'start':
				network[cave].append(opposite)

	traverse(['start'])
	total_paths = len(paths)

	# for cave in network: print(cave, network[cave])
	for path in paths: print('-'.join(path))

	print(run_title, "total_paths:", total_paths)

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
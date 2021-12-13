
# https://adventofcode.com/2021/day/12

# import statistics
# from collections import deque
from collections import namedtuple

# Vec2 = namedtuple("Vec2", ['x', 'y'])
Path = namedtuple("Path", ['steps', 'visited_small'])

def run(run_title, input_file):

	def traverse(path):
		for connection in network[path.steps[-1]]: 
			if connection == 'end': 
				new_path = Path(path.steps + [connection], path.visited_small)
				paths.append(new_path)
			else: 
				is_small_cave = not connection[0].isupper()
				if (is_small_cave): 
					if not path.visited_small:
						new_path = Path(path.steps + [connection], True)
						traverse(new_path)
				else: 
					new_path = Path(path.steps + [connection], path.visited_small)
					traverse(new_path)				

	# --------------------------------------------------------------------------------

	# Test / Real – 19 / 268

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

	traverse(Path(['start'], False))
	total_paths = len(paths)

	# for cave in network: print(cave, network[cave])
	for path in paths: print('-'.join(path.steps))

	print(run_title, "total_paths:", total_paths)

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
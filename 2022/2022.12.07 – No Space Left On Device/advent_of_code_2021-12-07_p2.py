
# https://adventofcode.com/2022/day/7

import string

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

system = { "/": { "name": "/", "parent": None } }
current_dir = system["/"]

for line in input_file:

	line = line.rstrip()

	if line.startswith('$'): 
		line = line.split(' ')
		if line[1] == "cd": 
			target_dir = line[2]
			if target_dir == "..":
				current_dir = current_dir["parent"]
			elif target_dir == "/":
				current_dir = system["/"]
			else: 
				if not target_dir in current_dir: 
					dir_name = current_dir["name"] + "/" + target_dir
					current_dir[target_dir] = { "name": dir_name, "parent": current_dir }
				current_dir = current_dir[target_dir]
		# elif line[1] == "ls": 
	else: 
		line = line.split(' ')
		if line[0].isnumeric(): 
			file_size = int(line[0])
			file_name = line[1]
			current_dir[file_name] = { "name": file_name, "size": file_size }
		else:
			target_dir = line[1]
			if not target_dir in current_dir: 
				dir_name = current_dir["name"] + "/" + target_dir
				current_dir[target_dir] = { "name": dir_name, "parent": current_dir }

# Calculate recursive directory sizes

recursive_dir_size = {}

def get_recursive_size(directory): 
	dir_name = directory["name"]
	if not dir_name in recursive_dir_size: 
		recursive_dir_size[dir_name] = 0
	for k, v in directory.items(): 
		if k == "name" or k == "parent": 
			continue
		elif not "size" in v: 
			recursive_dir_size[dir_name] += get_recursive_size(v)
		else: 
			recursive_dir_size[dir_name] += v["size"]
	return recursive_dir_size[dir_name]

get_recursive_size(system["/"])

# Find smalles directory that would free up enough space

total_disk_space = 70000000
total_space_used = recursive_dir_size["/"]
required_unused_space = 30000000
min_space_deletion = required_unused_space - (total_disk_space - total_space_used)

valid_dir_sizes = []

for size in recursive_dir_size.values(): 
	if size > min_space_deletion: 
		valid_dir_sizes.append(size)

valid_dir_sizes.sort()

print("Smallest valid dir size:", valid_dir_sizes[0])

# https://adventofcode.com/2021/day/20

import time
import math
import re
from copy import deepcopy

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def pad_image():
		image.insert(0, ['0'] * len(image[0]))
		image.append(['0'] * len(image[0]))
		for row in image: 
			row.insert(0, '0')
			row.append('0')

	def crop_image():
		image.pop(-1)
		image.pop(0)
		for row in image: 
			row.pop(-1)
			row.pop(0)

	def print_image(): 
		for row in deepcopy(image): 
			joined_row = ''.join(row).replace('0', '.').replace('1', '#')
			print(joined_row)

	def enhance_image(): 
		image_copy = deepcopy(image)
		for y in range(1, len(image) - 1): 
			for x in range(1, len(image[0]) - 1): 
				tile = ''
				for r in range(0, 3): 
					tile += ''.join(image_copy[y-1+r][x-1:x+2])
				image[y][x] = enhancement_algorithm[int(tile, 2)]

	def get_lit_pixels(): 
		lit_pixels = 0
		for y in range(0, len(image)): 
			for x in range(0, len(image[0])): 
				if image[y][x] == '1': 
					lit_pixels += 1
		return lit_pixels

	# --------------------------------------------------------------------------------

	# Test / Real – 35 / 5486

	start_time_ms = round(time.time() * 1000)

	enhancement_algorithm = ''
	image = []

	for i, line in enumerate(input_file): 
		if i == 0: 
			row = line.strip().replace('.', '0').replace('#', '1')
			enhancement_algorithm = [c for c in row]
		elif i > 1: 
			row = line.strip().replace('.', '0').replace('#', '1')
			image.append([c for c in row])
	
	for i in range(0, 20): 
		pad_image()

	for i in range(0, 2): 
		pad_image()
		enhance_image()

	for i in range(0, 5): 
		crop_image()

	lit_pixels = get_lit_pixels()

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print(run_title, "lit_pixels:", lit_pixels, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())

# https://adventofcode.com/2022/day/13

import string
import math
import time
import re

def prt(*args, **kwargs):
	print(' '.join(map(str,args)), **kwargs)
	return

def get_time_now(): 
	# return datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
	return datetime.datetime.now().strftime("%H:%M:%S")

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

for i, line in enumerate(input_file):

	line = line.rstrip()

start_time_ms = round(time.time() * 1000)
print("Start time:", get_time_now())

# Code here

end_time_ms = round(time.time() * 1000)
print("End time:", get_time_now())
print("Total time:", end_time_ms - start_time_ms, "ms")
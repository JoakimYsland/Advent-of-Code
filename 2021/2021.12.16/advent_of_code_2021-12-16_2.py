
# https://adventofcode.com/2021/day/16

# import re
import time
import math

def my_print(*args, **kwargs):
	# print(' '.join(map(str,args)), **kwargs)
	return

def run(run_title, input_file):

	def parse_packet(packet): 

		packet_version = int(packet[0:3],2)
		packet_type = int(packet[3:6],2)
		offset = 6

		nonlocal sum_packet_version
		sum_packet_version += packet_version

		my_print('––––––––––')
		my_print('packet_version:', packet_version)
		my_print('packet_type:', packet_type)
		
		if packet_type == 4: 
			# Literal value
			literal_value = ''
			flag = 1
			while flag != '0':
				group = packet[offset:offset+5]
				flag = group[0:1]
				literal_value += group[1:5]
				offset += 5
			my_print('literal_packet:', packet[0:offset])
			my_print('literal_value:', literal_value, ('(' + str(int(literal_value, 2)) + ')'))
			return offset, literal_value
		else: 
			# Operator
			length_type = packet[6:7]
			offset += 1
			op_values = []
			my_print('length_type:', length_type)
			if (length_type == '0'): 
				# Length is a 15-bit number representing the number of bits in the sub-packets
				sub_packets_bit_length = int(packet[7:22], 2)
				my_print('sub_packets_bit_length:', sub_packets_bit_length)
				offset += 15
				sub_packet_end = offset + sub_packets_bit_length - 1
				while offset < sub_packet_end: 
					new_offset, literal_value = parse_packet(packet[offset:])
					offset += new_offset
					if type(literal_value) != int: 
						literal_value = int(literal_value, 2)
					op_values.append(literal_value)
			else: 
				# Length is a 11-bit number representing the number of sub-packets
				num_sub_packets = int(packet[7:18], 2)
				my_print('num_sub_packets:', num_sub_packets)
				offset += 11
				for i in range(0, num_sub_packets):
					new_offset, literal_value = parse_packet(packet[offset:])
					offset += new_offset
					if type(literal_value) != int: 
						literal_value = int(literal_value, 2)
					op_values.append(literal_value)

			op_value_final = 0

			my_print('––––––––––')
			if (packet_type == 0): # Sum
				op_value_final = sum(op_values)
				my_print('Returning sum of:', op_values, "=>", op_value_final)
			elif (packet_type == 1): # Product
				op_value_final = math.prod(op_values)
				my_print('Returning product of:', op_values, "=>", op_value_final)
			elif (packet_type == 2): # Minimum
				op_value_final = min(op_values)
				my_print('Returning min of:', op_values, "=>", op_value_final)
			elif (packet_type == 3): # Maximum
				op_value_final = max(op_values)
				my_print('Returning max of:', op_values, "=>", op_value_final)
			elif (packet_type == 5): # Greater than
				op_value_final = 1 if op_values[0] > op_values[1] else 0
				my_print('Returning > of:', op_values, "=>", op_value_final)
			elif (packet_type == 6): # Less than
				op_value_final = 1 if op_values[0] < op_values[1] else 0
				my_print('Returning < of:', op_values, "=>", op_value_final)
			elif (packet_type == 7): # Equal to
				op_value_final = 1 if op_values[0] == op_values[1] else 0
				my_print('Returning == of:', op_values, "=>", op_value_final)

			return offset, op_value_final

	hex_to_binary = {
		'0': '0000', 
		'1': '0001', 
		'2': '0010', 
		'3': '0011', 
		'4': '0100', 
		'5': '0101', 
		'6': '0110', 
		'7': '0111', 
		'8': '1000', 
		'9': '1001', 
		'A': '1010', 
		'B': '1011', 
		'C': '1100', 
		'D': '1101', 
		'E': '1110', 
		'F': '1111', 
	}

	# --------------------------------------------------------------------------------

	# Test / Real – n/a / 13476220616073 (2ms)

	start_time_ms = round(time.time() * 1000)

	op_value_final = 0
	sum_packet_version = 0

	for line in input_file: 
		binary = ''.join(hex_to_binary[c] for c in line.strip())
		_, op_value_final = parse_packet(binary)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	print(run_title, "sum_packet_version:", sum_packet_version, ('(' + str(total_time) + "ms)"))
	print(run_title, "op_value_final:", op_value_final, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
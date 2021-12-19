
# https://adventofcode.com/2021/day/16

# import re
import time
import math
# from copy import deepcopy

def run(run_title, input_file):

	def parse_packet(packet): 

		if int(packet, 2) == 0: 
			padding = len(packet)
			print('padding')
			return padding

		packet_version = int(packet[0:3],2)
		packet_type_id = int(packet[3:6],2)
		

		nonlocal sum_packet_version
		sum_packet_version += packet_version

		print('––––––––––')
		print('packet_version:', packet_version)
		print('packet_type_id:', packet_type_id)
		
		if packet_type_id == 4: 
			# Literal value
			print('literal_packet:', packet)
			offset = 6
			literal_value = ''
			flag = 1
			while flag != '0':
				group = packet[offset:offset+5]
				flag = group[0:1]
				literal_value += group[1:5]
				offset += 5
			print('literal_value:', literal_value, ('(' + str(int(literal_value, 2)) + ')'))
			padding = offset - len(literal_value)
			return ('0' * padding) + literal_value
		else: 
			# Operator
			length_type = packet[6:7]
			literal_values = []
			print('length_type:', length_type)
			if (length_type == '0'): 
				# Length is a 15-bit number representing the number of bits in the sub-packets
				sub_packets_bit_length = int(packet[7:22], 2)
				sub_packet = packet[22:22+sub_packets_bit_length]
				print('sub_packets_bit_length:', sub_packets_bit_length)
				offset = 0
				while offset < sub_packets_bit_length - 1: 
					literal_value = parse_packet(sub_packet[offset:])
					offset += len(literal_value)
					literal_values.append(int(literal_value, 2))
			else: 
				# Length is a 11-bit number representing the number of sub-packets
				num_sub_packets = int(packet[7:18], 2)
				sub_packet = packet[18:]
				print('num_sub_packets:', num_sub_packets)
				offset = 0
				for i in range(0, num_sub_packets):
					literal_value = parse_packet(sub_packet[offset:])
					offset += len(literal_value)
					literal_values.append(int(literal_value, 2))

			if 	 (packet_type_id == 0): return sum(literal_values) # Sum
			elif (packet_type_id == 1): return math.prod(literal_values) # Product
			elif (packet_type_id == 2): return min(literal_values) # Minimum
			elif (packet_type_id == 3): return max(literal_values) # Maximum
			elif (packet_type_id == 5): return 1 if literal_values[0] > literal_values[1] else 0 # Greater than
			elif (packet_type_id == 6): return 1 if literal_values[0] < literal_values[1] else 0 # Less than
			elif (packet_type_id == 7): return 1 if literal_values[0] == literal_values[1] else 0 # Equal to

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

	# Test / Real – n/a / ???

	start_time_ms = round(time.time() * 1000)

	transmission = 0
	sum_packet_version = 0

	for line in input_file: 
		binary = ''.join(hex_to_binary[c] for c in line.strip())
		transmission = parse_packet(binary)

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	# print(run_title, "sum_packet_version:", sum_packet_version, ('(' + str(total_time) + "ms)"))
	print(run_title, "transmission:", transmission, ('(' + str(total_time) + "ms)"))

run("[Test]", open('input_test.txt', 'r').readlines())
# run("[Real]", open('input.txt', 'r').readlines())
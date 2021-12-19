
# https://adventofcode.com/2021/day/16

# import re
import time
# from copy import deepcopy

def run(run_title, input_file):

	def parse_sub_packets_by_length(sub_packet):

		length = len(sub_packet)
		offset = 0
		while offset < length - 1: 
			offset += parse_packet(sub_packet[offset:])
			print('** sub-packet **')

	def parse_packet(packet): 

		if int(packet, 2) == 0: 
			padding = len(packet)
			return padding

		packet_version = int(packet[0:3],2)
		packet_type_id = int(packet[3:6],2)

		nonlocal sum_version_numbers
		sum_version_numbers += packet_version

		print('––––––––––')
		print('packet_version:', packet_version)
		print('packet_type_id:', packet_type_id)
		
		if packet_type_id == 4: # Literal value
			offset = 6
			literal_value = ''
			flag = 1
			while flag != '0':
				group = packet[offset:offset+5]
				flag = group[0:1]
				literal_value += group[1:5]
				offset += 5
			print('literal_value:', int(literal_value, 2))
			return offset
		else: # Operator
			length_type = packet[6:7]
			print('length_type:', length_type)
			if (length_type == '0'): # Length is a 15-bit number representing the number of bits in the sub-packets
				sub_packets_bit_length = int(packet[7:22], 2)
				sub_packet = packet[22:22+sub_packets_bit_length]
				print('sub_packets_bit_length:', sub_packets_bit_length)
				parse_sub_packets_by_length(sub_packet)
				return 22 + sub_packets_bit_length
			else: # Length is a 11-bit number representing the number of sub-packets
				num_sub_packets = int(packet[7:18], 2)
				print('num_sub_packets:', num_sub_packets)
				sub_packets_bit_length = 0
				for i in range(0,num_sub_packets):
					sub_packets_bit_length += parse_packet(packet[18+sub_packets_bit_length:])
					print('** sub-packet **')
				return 18 + sub_packets_bit_length

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

	# Test / Real – n/a / 940 (1576ms)

	start_time_ms = round(time.time() * 1000)

	sum_version_numbers = 0

	for line in input_file: 
		binary = ''.join(hex_to_binary[c] for c in line.strip())
		offset = 0
		while offset < len(binary) - 1:
			offset += parse_packet(binary[offset:])

	end_time_ms = round(time.time() * 1000)
	total_time = end_time_ms - start_time_ms

	print('––––––––––')
	print(run_title, "sum_version_numbers:", sum_version_numbers, ('(' + str(total_time) + "ms)"))

# run("[Test]", open('input_test.txt', 'r').readlines())
run("[Real]", open('input.txt', 'r').readlines())
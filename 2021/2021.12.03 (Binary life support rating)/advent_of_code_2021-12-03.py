
# https://adventofcode.com/2021/day/3

input_file = open('input.txt', 'r').readlines()
gamma_rate_bits = ''
bit_balances = {}

for line in input_file:
	line_bits = [char for char in line if char.isdigit()]
	for i, bit in enumerate(line_bits):
		if not i in bit_balances: bit_balances[i] = 0
		bit_balances[i] += 1 if (line_bits[i] == '1') else -1

for bit_balance in bit_balances.values(): 
	gamma_rate_bits += '1' if bit_balance > 0 else '0'

epsilon_rate_bits = ''.join('1' if bit == '0' else '0' for bit in gamma_rate_bits)

gamma_rate = int(gamma_rate_bits, 2)
epsilon_rate = int(epsilon_rate_bits, 2)
power_consumption = gamma_rate * epsilon_rate

print(gamma_rate_bits, "/", gamma_rate, "*", epsilon_rate_bits, "/", epsilon_rate, "=", power_consumption)
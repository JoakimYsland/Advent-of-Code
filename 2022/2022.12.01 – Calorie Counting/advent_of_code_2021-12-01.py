
# https://adventofcode.com/2022/day/1

# input_file = open('test_input.txt', 'r').readlines()
input_file = open('input.txt', 'r').readlines()

elves_calories = [0]

for line in input_file:
	try: 
		calories = int(line)
		elves_calories[-1] += calories
	except:
		elves_calories.append(0)

print("Elves:", elves_calories)
print("Elf Count:", len(elves_calories))
print("Most Calories:", max(elves_calories))
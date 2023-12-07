import sys
from functools import reduce

TEST_PATH = './test_data/input_06.txt'
DATA_PATH = './data/input_06.txt'

def get_data_1(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	with open(path) as f:
		lines = list(map(str.split, f.read().splitlines()))
		data = list(zip(map(int, lines[0][1:]), map(int, lines[1][1:])))
		return data
	
def get_data_2(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	with open(path) as f:
		lines = list(map(str.split, f.read().splitlines()))
		time, distance = int("".join(lines[0][1:])), int("".join(lines[1][1:]))
		data = [(time, distance)]
		return data
	
def check_race(time, record):
	wins = 0
	for i in range(1, record):
		result = (time - i) * i
		if result > record:
			wins += 1
	return wins

def part_1(data):
	num_wins = [check_race(time, record) for (time, record) in data]
	print(reduce(lambda x, y: x*y, num_wins))

def find_starting_point(time, record):
	lower, upper = 0, time
	x = int(time/2)

	while True:
		x = int((upper + lower) / 2)
		curr_distance = (time - x) * x
		if curr_distance > record:
			return x
		elif (time - (x + 1)) * (x + 1) > curr_distance:
			lower = x
		else:
			upper = x
	
def check_race_using_bounds(time, record):
	starting_point = find_starting_point(time, record)
	lower_bound, upper_bound = starting_point, starting_point

	while True:
		distance = (time - lower_bound) * lower_bound
		if distance < record:
			break
		lower_bound -= 1

	while True:
		distance = (time - upper_bound) * upper_bound
		if distance < record:
			break
		upper_bound += 1
	
	return upper_bound - lower_bound - 1

def part_2(data):
	num_wins = check_race_using_bounds(data[0][0], data[0][1])
	print(num_wins)

def main(is_test):
	part_1(get_data_1(is_test))
	part_2(get_data_2(is_test))

if __name__ == "__main__":
	is_test = len(sys.argv) > 1 and sys.argv[1].lower() == '--test'
	main(is_test)

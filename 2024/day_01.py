import sys
import math

TEST_PATH = './test_data/input_01.txt'
DATA_PATH = './data/input_01.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	lines = open(path).read().splitlines()
	data = []
	for line in lines:
		data.append(list(map(int, line.split())))
	return data

def part_one(data):
	left_list = sorted([x[0] for x in data])
	right_list = sorted([x[1] for x in data])
	
	score = 0
	
	for i in range(len(left_list)):
		score += abs(left_list[i] - right_list[i]) 
	return score

def part_two(data):
	left_list = sorted([x[0] for x in data])
	right_list = sorted([x[1] for x in data])
	right_counter = {}
	
	for item in right_list:
		if item in right_counter:
			right_counter[item] += 1
		else:
			right_counter[item] = 1
			
	score = 0

	for item in left_list:
		if item in right_counter:
			score += item * right_counter[item]
				
	return score	

def main(is_test):
	data = get_data(is_test)
	print('part one: ', part_one(data))
	print('part two: ', part_two(data))


if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

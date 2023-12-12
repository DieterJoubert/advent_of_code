import sys

TEST_PATH = './test_data/input_12.txt'
DATA_PATH = './data/input_12.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	lines = open(path).read().splitlines()

	data = []
	for line in lines:
		condition_record, sizes = line.split(' ')
		data.append((condition_record, list(map(int, sizes.split(',')))))
	
	return data

def part_1(data):
	print('part 1')

def assertions(is_test, result_1, result_2):
	pass

def main(is_test):
	data = get_data(is_test)
	print(data)


if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

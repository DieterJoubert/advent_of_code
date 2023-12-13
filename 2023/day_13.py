import sys

TEST_PATH = './test_data/input_13.txt'
DATA_PATH = './data/input_13.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	grid_lines = open(path).read().strip().split('\n\n')
	return list(map(lambda x: x.split('\n'), grid_lines))

def part_1(grids):
	for grid in grids:
		print('grid')
		print(grid)

def assertions(is_test, result_1, result_2):
	pass

def main(is_test):
	grids = get_data(is_test)
	print(grids)

	result_1 = part_1(grids)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

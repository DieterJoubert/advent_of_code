import sys

TEST_PATH = './test_data/input_07.txt'
DATA_PATH = './data/input_07.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	with open(path) as f:
		lines = list(map(str.split, f.read().splitlines()))
		hands = map(lambda x: x[0], lines)
		bids = map(lambda x: int(x[1]), lines)
		return list(zip(hands, bids))
	
def part_1(data):
	pass

def main(is_test):
	data = get_data(is_test)
	print(data)
	part_1(data)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

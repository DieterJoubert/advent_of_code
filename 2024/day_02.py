import sys

TEST_PATH = './test_data/input_02.txt'
DATA_PATH = './data/input_02.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	lines = open(path).read().splitlines()
	data = []
	for line in lines:
		data.append(list(map(int, line.split())))
	return data

def part_one(data):
	def is_safe(level):
		differences = set()

		for i in range(len(level)-1):
			a, b = level[i], level[i+1]
			differences.add(b-a)

		if 0 in differences:
			return False
		
		max_val = max(differences)
		min_val = min(differences)

		if min_val < 0 and max_val > 0:
			return False
		if min_val < -3 or max_val > 3:
			return False

		return True

	return sum([is_safe(level) for level in data])

def part_two(data):
	def is_safe(level):
		differences = []

		for i in range(len(level)-1):
			a, b = level[i], level[i+1]
			differences.append(b-a)

		if 0 in differences:
			return False
		
		max_val = max(differences)
		min_val = min(differences)

		if min_val < 0 and max_val > 0:
			return False
		if min_val < -3 or max_val > 3:
			return False

		return True

	return sum([is_safe(level) for level in data])

def main(is_test):
	data = get_data(is_test)
	print('one: ', part_one(data))

	if not is_test:
		assert part_one(data) == 236



if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

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

def part_one(data):
	return sum([is_safe(level) for level in data])

def get_subarrays(arr):
	result = []
	for i in range(len(arr)):
		subarray = arr[:i] + arr[i+1:]
		result.append(subarray)
	return result

def part_two(data):
	def is_safe_with_mod(level):
		if is_safe(level):
			return True
		
		sub_arrays = get_subarrays(level)

		for array in sub_arrays:
			if is_safe(array):
				return True
			
		return False

	return sum([is_safe_with_mod(level) for level in data])

def main(is_test):
	data = get_data(is_test)

	print('one: ', part_one(data))
	print('two: ', part_two(data))

	if not is_test:
		assert part_one(data) == 236
		assert part_two(data) == 308

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

import sys

TEST_PATH = './test_data/input_05.txt'
DATA_PATH = './data/input_05.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH

	with open(path) as f:
		lines = [x for x in f.read().splitlines() if x]

		initial_seeds = list(map(int, lines[0].split(':')[1].split()))

		maps = []

		cursor = 2
		curr_map = []

		while True:
			curr = lines[cursor]
			if curr[0].isnumeric():
				curr_map.append(tuple(map(int, curr.split())))
			else:
				maps.append(curr_map)
				curr_map = []

			cursor += 1
			if cursor >= len(lines):
				maps.append(curr_map)
				break

	return initial_seeds, maps

def convert_seed(seed, conversion_maps):
	for single_map in conversion_maps:
		for (destination_start, source_start, range_length) in single_map:
			if seed in range(source_start, source_start+range_length):
				delta = seed - source_start
				seed = destination_start + delta
				break
	return seed

def part_1(initial_seeds, conversion_maps):
	final_values = [convert_seed(x, conversion_maps) for x in initial_seeds]
	print(min(final_values))

def part_2(initial_seeds, conversion_maps):
	initial_seed_ranges = list(zip(initial_seeds[0::2], initial_seeds[1::2]))

	min_found = float('inf')

	for (initial_seed, seed_range) in initial_seed_ranges:
		for x in range(initial_seed, initial_seed+seed_range):
			this_result = convert_seed(x, conversion_maps)
			min_found = min(min_found, this_result)

	print(min_found)

def main(is_test):
	initial_seeds, conversion_maps = get_data(is_test)
	part_1(initial_seeds, conversion_maps)
	#part_2(initial_seeds, conversion_maps)

if __name__ == "__main__":
	is_test = len(sys.argv) > 1 and sys.argv[1].lower() == '--test'
	main(is_test)

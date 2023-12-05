from collections import deque

DATA_PATH = './data/input_05.txt'

def get_data():
	with open(DATA_PATH) as f:
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
	print(final_values)
	print(min(final_values))

def main():
	initial_seeds, conversion_maps = get_data()
	part_1(initial_seeds, conversion_maps)

if __name__ == "__main__":
	main()

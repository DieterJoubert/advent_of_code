from collections import deque

DATA_PATH = './test_data/input_05.txt'

class ConversionMap():
	def __init__(self, destination_range_start, source_range_start, range_length):
		self.destination_range_start = destination_range_start
		self.source_range_start = source_range_start
		self.range_length = range_length

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


def part_1():
	pass

def main():
	initial_seeds, conversion_maps = get_data()
	print(initial_seeds)
	print(conversion_maps)

	part_1()

if __name__ == "__main__":
	main()

from functools import reduce

DATA_PATH = './test_data/input_03.txt'

def get_data():
	with open(DATA_PATH) as f:
		lines = f.read().splitlines()
		
		return [list(x) for x in lines]

def get_neighbors(data, i, j):
	neighbors = []

	for i_delta in [-1, 0, 1]:
		for j_delta in [-1, 0, 1]:
			if i_delta == j_delta == 0:
				continue

			try:
				neighbor = data[i+i_delta][j+j_delta]
				neighbors.append(neighbor)
			except:
				pass

	return neighbors

def get_part_numbers(data):
	part_numbers = []

	for i in range(len(data)):
		row = data[i]

		for j in range(len(row)):
			this_cell = data[i][j]

			if this_cell == '.':
				continue
			if this_cell.isnumeric():
				neighbors = get_neighbors(data, i, j)

				has_adjacent_part = any(x != '.' and not x.isnumeric() for x in neighbors)

				if has_adjacent_part:
					part_numbers.append(int(this_cell))

	return part_numbers

def part_1(data):
	part_numbers = get_part_numbers(data)
	print(sum(part_numbers))

def main():
	data = get_data()
	print(data)

	part_1(data)

if __name__ == "__main__":
	main()

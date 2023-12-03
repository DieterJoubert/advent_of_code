from functools import reduce

DATA_PATH = './data/input_03.txt'

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

def get_number_and_neighbors(data):
	number_and_neighbors = []

	for i in range(len(data)):
		this_row = data[i]

		current_num = ''
		current_neighbors = []

		for j in range(len(this_row)):
			this_cell = data[i][j]

			if this_cell.isnumeric():
				current_num += this_cell
				neighbors = get_neighbors(data, i, j)
				for n in neighbors:
						current_neighbors.append(n)

			elif current_num:
				number_and_neighbors.append([int(current_num), current_neighbors])
				current_num = ''
				current_neighbors = []
		
		if current_num:
			number_and_neighbors.append([int(current_num), current_neighbors])
			current_num = ''
			current_neighbors = []

	return number_and_neighbors


def part_1(data):
	numbers_and_neighbors = get_number_and_neighbors(data)
	#print(numbers_and_neighbors)

	part_numbers = []

	for (number, neighbors) in numbers_and_neighbors:
		if any(x != '.' and not x.isnumeric() for x in neighbors):
			part_numbers.append(number)

	print(sum(part_numbers))

def main():
	data = get_data()
	#print(data)

	part_1(data)

if __name__ == "__main__":
	main()

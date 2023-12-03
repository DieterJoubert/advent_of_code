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
	part_numbers = []

	for (number, neighbors) in numbers_and_neighbors:
		if any(x != '.' and not x.isnumeric() for x in neighbors):
			part_numbers.append(number)

	print('part 1: ' + str(sum(part_numbers)))

def explore_new_number(data, i, j):
	explored = {(i, j)}
	
	new_number = data[i][j]

	cursor = (i, j)

	while True:
		cursor = (i, cursor[1]-1)
		if cursor[1] < 0:
			break

		cell_to_check = data[cursor[0]][cursor[1]]
		explored.add(cursor)

		if cell_to_check.isnumeric():
			new_number = cell_to_check + new_number
		else:
			break

	cursor = (i, j)

	while True:
		cursor = (i, cursor[1]+1)
		if cursor[1] >= len(data[0]):
			break

		cell_to_check = data[cursor[0]][cursor[1]]
		explored.add(cursor)

		if cell_to_check.isnumeric():
			new_number = new_number + cell_to_check
		else:
			break

	return int(new_number), explored

def get_neighboring_numbers(data, i, j):
	explored = set()
	neighboring_numbers = []

	for i_delta in [-1, 0, 1]:
		for j_delta in [-1, 0, 1]:
			if i_delta == j_delta == 0:
				continue

			new_i, new_j = i+i_delta, j+j_delta
			if (new_i, new_j) in explored:
				continue

			cell_to_explore = data[new_i][new_j]

			if cell_to_explore.isnumeric():
				new_number, new_explored = explore_new_number(data, new_i, new_j)
				for n in new_explored:
					explored.add(n)
				neighboring_numbers.append(new_number)

	return neighboring_numbers


def part_2(data):
	gears_with_two_neighbors = []

	for i in range(len(data)):
		for j in range(len(data[0])):
			this_cell = data[i][j]

			if this_cell == '*':
				neighboring_numbers = get_neighboring_numbers(data, i, j)

				if len(neighboring_numbers) == 2:
					gears_with_two_neighbors.append(neighboring_numbers)

	total = 0
	for x in gears_with_two_neighbors:
		total += (x[0] * x[1])

	print('part 2: ' + str(total))
				

def main():
	data = get_data()

	part_1(data)
	part_2(data)

if __name__ == "__main__":
	main()

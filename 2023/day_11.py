import sys

TEST_PATH = './test_data/input_11.txt'
DATA_PATH = './data/input_11.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	lines = open(path).read().splitlines()
	data = [list(x) for x in lines]
	curr = 1

	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == '#':
				data[i][j] = str(curr)
				curr += 1

	return data

def get_empty_rows_and_columns(grid):
	empty_rows = set()
	empty_columns = set()

	for i in range(len(grid)):
		is_row_empty = all(grid[i][j] == '.' for j in range(len(grid[0])))
		if is_row_empty:
			empty_rows.add(i)
	
	for j in range(len(grid[0])):
		is_column_empty = all(grid[i][j] == '.' for i in range(len(grid)))
		if is_column_empty:
			empty_columns.add(j)

	return empty_rows, empty_columns

def get_galaxy_name_to_coords(grid):
	galaxy_name_to_coords = {}

	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j].isnumeric():
				galaxy_name_to_coords[grid[i][j]] = (i,j)
	
	return galaxy_name_to_coords

def execute(grid, is_part_one):
	expansion_factor = 1 if is_part_one else 1000000

	empty_rows, empty_columns = get_empty_rows_and_columns(grid)

	galaxy_name_to_coords = get_galaxy_name_to_coords(grid)

	min_distances = {}

	for x in galaxy_name_to_coords.keys():
		for y in galaxy_name_to_coords.keys():
			if x != y:
				sorted_pair_names = tuple(sorted([x, y]))
				x_coords = galaxy_name_to_coords[x]
				y_coords = galaxy_name_to_coords[y]

				num_empty_rows_crossed = len([i for i in range(min(x_coords[0], y_coords[0])+1, max(x_coords[0]+1, y_coords[0])) if i in empty_rows])
				num_empty_columns_crossed = len([i for i in range(min(x_coords[1], y_coords[1])+1, max(x_coords[1]+1, y_coords[1])) if i in empty_columns])
				
				manhattan_distance = abs(x_coords[0] - y_coords[0]) + abs(x_coords[1] - y_coords[1])
				manhattan_distance += ((num_empty_rows_crossed + num_empty_columns_crossed ) * expansion_factor)

				if sorted_pair_names in min_distances:
					min_distances[sorted_pair_names] = min(min_distances[sorted_pair_names], manhattan_distance)
				else:
					min_distances[sorted_pair_names] = manhattan_distance

	return sum(min_distances.values())

def assertions(is_test, result_1, result_2):
	if is_test:
		assert result_1 == 374

	else:
		assert result_1 == 9556712


def main(is_test):
	data = get_data(is_test)

	result_1 = execute(data, True)
	print(result_1)

	result_2 = execute(data, False)
	print(result_2)

	assertions(is_test, result_1, result_2)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

import sys
import math
from collections import deque
from functools import reduce

TEST_PATH_1 = './test_data/input_10_p1.txt'
TEST_PATH_2 = './test_data/input_10_p2.txt'
DATA_PATH = './data/input_10.txt'

NORTH_AND_SOUTH = '|'
EAST_AND_WEST = '-'
NORTH_AND_EAST = 'L'
NORTH_AND_WEST = 'J'
SOUTH_AND_WEST = '7'
SOUTH_AND_EAST = 'F'
START = 'S'

def get_data(is_test, is_part_one):
	if is_test:
		path = TEST_PATH_1 if is_part_one else TEST_PATH_2
	else:
		path = DATA_PATH
	with open(path) as f:
		lines = f.read().splitlines()
		return [list(x) for x in lines]

def get_starting_coords(grid):
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == 'S':
				return (i, j)

def get_neighbors(grid, node):
	neighbors = {}
	for (direction, i, j) in [('UP', -1, 0), ('DOWN', 1, 0), ('LEFT', 0, -1), ('RIGHT', 0, 1)]:
		if i == j:
			continue
		try:
			neighbor = grid[node[0]+i][node[1]+j]
			neighbors[direction] = neighbor
		except Exception:
			pass

	return neighbors

def get_connected_sides(node_symbol):
	if node_symbol == 'S':
		return {'UP', 'DOWN', 'LEFT', 'RIGHT'}
	if node_symbol == NORTH_AND_SOUTH:
		return {'UP', 'DOWN'}
	if node_symbol == EAST_AND_WEST:
		return {'LEFT', 'RIGHT'}
	if node_symbol == NORTH_AND_WEST:
		return {'UP', 'LEFT'}
	if node_symbol == NORTH_AND_EAST:
		return {'UP', 'RIGHT'}
	if node_symbol == SOUTH_AND_WEST:
		return {'DOWN', 'LEFT'}
	if node_symbol == SOUTH_AND_EAST:
		return {'DOWN' ,'RIGHT'}
	return {}

def get_connected_neighbors(curr_coords, curr_symbol, neighbors):
	connected_neighbors = []
	connected_sides = get_connected_sides(curr_symbol)

	for side in connected_sides:
		neighbor = neighbors.get(side, None)
		if neighbor:
			if side == 'UP' and 'DOWN' in get_connected_sides(neighbor):
				connected_neighbors.append((curr_coords[0]-1, curr_coords[1]))
			if side == 'DOWN' and 'UP' in get_connected_sides(neighbor):
				connected_neighbors.append((curr_coords[0]+1, curr_coords[1]))
			if side == 'LEFT' and 'RIGHT' in get_connected_sides(neighbor):
				connected_neighbors.append((curr_coords[0], curr_coords[1]-1))
			if side == 'RIGHT' and 'LEFT' in get_connected_sides(neighbor):
				connected_neighbors.append((curr_coords[0], curr_coords[1]+1))
	
	return connected_neighbors


def explore(grid, starting_point):
	explored = set()

	distances = {}

	queue = deque()
	queue.append((starting_point, 0))

	while queue:
		curr_coords, curr_distance = queue.popleft()
		distances[curr_coords] = curr_distance
		explored.add(curr_coords)
		curr_symbol = grid[curr_coords[0]][curr_coords[1]]

		neighbors = get_neighbors(grid, curr_coords)
		connected_neighbor_coords = get_connected_neighbors(curr_coords, curr_symbol, neighbors)

		for neighbor_coord in connected_neighbor_coords:
			if neighbor_coord not in explored:
				queue.append((neighbor_coord, curr_distance+1))
	
	return distances

def part_1(grid):
	starting_coords = get_starting_coords(grid)
	distances = explore(grid, starting_coords)
	return max(distances.values())

def part_2(grid):
	starting_coords = get_starting_coords(grid)
	distances = explore(grid, starting_coords)

	#replace S with correct pipe

	#explore


# def part_2(grid):
# 	starting_coords = get_starting_coords(grid)
# 	distances = explore(grid, starting_coords)
# 	print("PART TWO")

# 	distances_keys = list(distances.keys())

# 	area_of_polygon = 0
# 	for i in range(len(distances_keys)-1):
# 		area_of_polygon += distances_keys[i][0] * distances_keys[i+1][1] - distances_keys[i+1][0] * distances_keys[i][1]
# 	area_of_polygon = 0.5 * max(area_of_polygon, -area_of_polygon)

# 	print('area', area_of_polygon)
# 	print("circ?", max(distances.values()))

# 	return area_of_polygon - len(distances_keys)

def assertions(is_test, result_1, result_2):
	if is_test:
		assert result_1 == 8
		assert result_2 == 10
	else:
		assert result_1 == 6812


def main(is_test):
	data_1 = get_data(is_test, True)
	result_1 = part_1(data_1)
	print()

	data_2 = get_data(is_test, False)
	result_2 = part_2(data_2)
	print('result 2', result_2)

	assertions(is_test, result_1, result_2)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

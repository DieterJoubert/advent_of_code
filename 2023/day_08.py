import sys
from enum import Enum
from functools import cmp_to_key

TEST_PATH = './test_data/input_08.txt'
DATA_PATH = './data/input_08.txt'

START_NODE = 'AAA'
END_NODE = 'ZZZ'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	with open(path) as f:
		lines = f.read().splitlines()

		instructions = lines[0].strip()
		graph = {}

		for line in lines[2:]:
			node, rest = line.split('=')
			graph[node.strip()] = tuple(map(str.strip, rest.replace('(', '').replace(')', '').split(',')))
		
		return instructions, graph
	
def part_1(instructions, graph):
	curr_node = START_NODE
	curr_instruction_idx = 0
	steps = 0

	while curr_node != END_NODE:
		node_neighbors = graph[curr_node]
		curr_instruction = instructions[curr_instruction_idx]

		if curr_instruction == 'L':
			print(curr_instruction, 'left')
			curr_node = node_neighbors[0]
		elif curr_instruction == 'R':
			print(curr_instruction, 'right')
			curr_node = node_neighbors[1]
		else:
			raise Exception("Invalid instruction")
		
		steps += 1
		
		curr_instruction_idx += 1
		if curr_instruction_idx >= len(instructions):
			curr_instruction_idx = 0

	return steps
	
def main(is_test):
	instructions, graph = get_data(is_test)
	
	steps_1 = part_1(instructions, graph)
	print(steps_1)



if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

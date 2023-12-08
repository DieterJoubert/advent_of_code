import sys
import math

TEST_PATH_P1 = './test_data/input_08_p1.txt'
TEST_PATH_P2 = './test_data/input_08_p2.txt'
DATA_PATH = './data/input_08.txt'

def get_data(is_test, is_part_one):
	if is_test:
		path = TEST_PATH_P1 if is_part_one else TEST_PATH_P2
	else:
		path = DATA_PATH

	print(path)
	with open(path) as f:
		lines = f.read().splitlines()

		instructions = lines[0].strip()
		graph = {}

		for line in lines[2:]:
			node, rest = line.split('=')
			graph[node.strip()] = tuple(map(str.strip, rest.replace('(', '').replace(')', '').split(',')))
		
		return instructions, graph

def get_next_node(curr_node, instruction, graph):
	neighbors = graph[curr_node]

	if instruction == 'L':
		return neighbors[0]
	elif instruction == 'R':
		return neighbors[1]
	else:
		raise Exception("Invalid instruction")
	
def get_steps_for_single_node(start_node, end_condition, instructions, graph):
	curr_node = start_node
	curr_instruction_idx = 0
	steps = 0

	while not end_condition(curr_node):
		curr_instruction = instructions[curr_instruction_idx]
		curr_node = get_next_node(curr_node, curr_instruction, graph)
		steps += 1
		
		curr_instruction_idx += 1
		if curr_instruction_idx >= len(instructions):
			curr_instruction_idx = 0

	return steps

def part_1(instructions, graph):
	START_NODE = 'AAA'
	return get_steps_for_single_node(START_NODE, lambda node: node == 'ZZZ', instructions, graph)

def part_2(instructions, graph):
	start_nodes = [x for x in graph.keys() if x[-1] == 'A']
	steps_per_node = [get_steps_for_single_node(x, lambda node: node[-1] == 'Z', instructions, graph) for x in start_nodes]
	return math.lcm(*steps_per_node)
	
def main(is_test):
	instructions_1, graph_1 = get_data(is_test, True)
	steps_1 = part_1(instructions_1, graph_1)
	print(steps_1)

	instructions_2, graph_2 = get_data(is_test, False)
	steps_2 = part_2(instructions_2, graph_2)
	print(steps_2)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

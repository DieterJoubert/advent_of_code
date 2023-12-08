import sys
import math

TEST_PATH = './test_data/input_08'
DATA_PATH = './data/input_08'

def get_data(is_test, is_part_one):
	path = (TEST_PATH if is_test else DATA_PATH) + ('_p1.txt' if is_part_one else '_p2.txt')
	print(path)
	with open(path) as f:
		lines = f.read().splitlines()

		instructions = lines[0].strip()
		graph = {}

		for line in lines[2:]:
			node, rest = line.split('=')
			graph[node.strip()] = tuple(map(str.strip, rest.replace('(', '').replace(')', '').split(',')))
		
		return instructions, graph

def get_steps_for_single_node(start_node, end_on_zzz, instructions, graph):
	curr_node = start_node
	curr_instruction_idx = 0
	steps = 0

	while True:
		if (curr_node == 'ZZZ' if end_on_zzz else curr_node[-1] == 'Z'):
			break
		
		node_neighbors = graph[curr_node]
		curr_instruction = instructions[curr_instruction_idx]

		if curr_instruction == 'L':
			curr_node = node_neighbors[0]
		elif curr_instruction == 'R':
			curr_node = node_neighbors[1]
		else:
			raise Exception("Invalid instruction")
		
		steps += 1
		
		curr_instruction_idx += 1
		if curr_instruction_idx >= len(instructions):
			curr_instruction_idx = 0

	return steps

def part_1(instructions, graph):
	START_NODE = 'AAA'
	return get_steps_for_single_node(START_NODE, True, instructions, graph)

def get_next_node(curr_node, instruction, graph):
	neighbors = graph[curr_node]

	if instruction == 'L':
		return neighbors[0]
	elif instruction == 'R':
		return neighbors[1]
	else:
		raise Exception("Invalid instruction")

def part_2(instructions, graph):
	start_nodes = [x for x in graph.keys() if x[-1] == 'A']
	steps_per_node = [get_steps_for_single_node(x, False, instructions, graph) for x in start_nodes]
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

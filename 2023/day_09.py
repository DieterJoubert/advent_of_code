import sys

TEST_PATH = './test_data/input_09.txt'
DATA_PATH = './data/input_09.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	with open(path) as f:
		lines = f.read().splitlines()
		return [list(map(int, x.split())) for x in lines]

def predict_for_single_history(history):
	history_sequencing = [history]

	while not all(x == 0 for x in history_sequencing[-1]):
		new_sequence = []
		last_sequence = history_sequencing[-1]

		for idx in range(len(last_sequence)-1):
			new_sequence.append(last_sequence[idx+1] - last_sequence[idx])
		
		history_sequencing.append(new_sequence)

	history_sequencing[-1].append(0)

	for idx in range(len(history_sequencing)-2, -1, -1):
		history_sequencing[idx].append(history_sequencing[idx][-1] + history_sequencing[idx+1][-1])

	return history_sequencing[0][-1]

def part_1(data):
	return sum(predict_for_single_history(x) for x in data)

def part_2(data):
	return sum(predict_for_single_history(x[::-1]) for x in data)

def assertions(is_test, result_1, result_2):
	if is_test:
		assert result_1 == 114
		assert result_2 == 2
	else:
		assert result_1 == 1904165718
		assert result_2 == 964

def main(is_test):
	data = get_data(is_test)

	result_1 = part_1(data)
	print(result_1)

	result_2 = part_2(data)
	print(result_2)

	assertions(is_test, result_1, result_2)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

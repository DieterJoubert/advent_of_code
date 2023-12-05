from collections import deque

DATA_PATH = './data/input_04.txt'

def get_data():
	with open(DATA_PATH) as f:
		data = []

		lines = f.read().splitlines()

		for line in lines:
			_, content = line.split(':')
			left, right = content.split('|')

			winning_numbers = list(map(int, left.split()))
			my_numbers = list(map(int, right.split()))

			data.append([winning_numbers, my_numbers])
		
		return data

def process_card(winning_numbers, my_numbers):
	count = 0
	for num in my_numbers:
		if num in winning_numbers:
			count += 1
	return count

def part_1(data):
	total_points = 0

	for winning_numbers, my_numbers in data:
		score = process_card(winning_numbers, my_numbers)

		if score > 0:
			total_points += (2 ** (score-1))

	print(total_points)

def part_2(data):
	idx_to_score = {idx: process_card(data[idx][0], data[idx][1]) for idx in range(len(data))}

	processed = []
	queue = deque([idx for idx in range(len(data))])

	while queue:
		curr_idx = queue.popleft()
		curr_score = idx_to_score[curr_idx]

		processed.append(curr_idx)

		for i in range(1, curr_score+1):
			queue.append(curr_idx+i)

	print(len(processed))

def main():
	data = get_data()

	part_1(data)
	part_2(data)

if __name__ == "__main__":
	main()

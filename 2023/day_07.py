import sys
from enum import Enum
from functools import cmp_to_key

TEST_PATH = './test_data/input_07.txt'
DATA_PATH = './data/input_07.txt'

def get_data(is_test):
	path = TEST_PATH if is_test else DATA_PATH
	with open(path) as f:
		lines = list(map(str.split, f.read().splitlines()))
		hands = map(lambda x: x[0], lines)
		bids = map(lambda x: int(x[1]), lines)
		return list(zip(hands, bids))
	
def get_hand_counter(hand):
	counter = {}
	for c in hand:
		counter[c] = counter.get(c, 0) + 1
	return counter

def get_joker_hand_counter(hand):
	num_jokers = 0
	counter = {}

	for c in hand:
		if c == 'J':
			num_jokers += 1
		elif c not in counter:
			counter[c] = 1
		else:
			counter[c] += 1

	if not counter: #edge case where only Jokers in hand
		return {'J': 5}

	counter_items = sorted(list(counter.items()), key=lambda x: x[1])
	max_item = counter_items[-1]

	for _ in range(num_jokers):
		counter[max_item[0]] += 1
	
	return counter

def get_card_bucket(hand_counter, hand_types):
	vals = list(hand_counter.values())

	if 5 in vals:
		return hand_types.FIVE_OF_A_KIND
	if 4 in vals:
		return hand_types.FOUR_OF_A_KIND
	if 3 in vals and 2 in vals:
		return hand_types.FULL_HOUSE
	if 3 in vals:
		return hand_types.THREE_OF_A_KIND
	if 2 in vals and vals.index(2) != (len(vals) - 1 - vals[::-1].index(2)):
		return hand_types.TWO_PAIR
	if 2 in vals:
		return hand_types.ONE_PAIR
	if 1 in vals and len(set(vals)) == 1:
		return hand_types.HIGH_CARD
	raise Exception('Could not place hand into bucket')

def card_compare(item_1, item_2, CARD_TYPES):
	for idx in range(len(item_1)):
		if CARD_TYPES.index(item_1[idx]) < CARD_TYPES.index(item_2[idx]):
			return -1
		elif CARD_TYPES.index(item_1[idx]) > CARD_TYPES.index(item_2[idx]):
			return 1
	raise Exception("Could not decide on comparison of hands")

def execute(data, is_part_one):
	HAND_TYPES = Enum('CARD_TYPES', [
		'FIVE_OF_A_KIND',
		'FOUR_OF_A_KIND',
		'FULL_HOUSE',
		'THREE_OF_A_KIND',
		'TWO_PAIR',
		'ONE_PAIR',
		'HIGH_CARD'
	])

	CARD_TYPES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'] if is_part_one else ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

	buckets = {e: [] for e in HAND_TYPES}

	hand_to_bid = {hand: int(bid) for (hand, bid) in data}

	for hand, _ in data:
		hand_counter = get_hand_counter(hand) if is_part_one else get_joker_hand_counter(hand)
		bucket_to_place_in = get_card_bucket(hand_counter, HAND_TYPES)
		buckets[bucket_to_place_in].append(hand)

	final_ranking = []

	for hand_type in HAND_TYPES:
		hands_in_bucket = buckets[hand_type]
		if hands_in_bucket:
			sorted_hands = sorted(hands_in_bucket, key=cmp_to_key(lambda x, y: card_compare(x, y, CARD_TYPES)))
			for hand in sorted_hands:
				final_ranking.append(hand)

	total_score = sum([(idx+1) * hand_to_bid[hand] for idx, hand in enumerate(final_ranking[::-1])])
	return total_score

def main(is_test):
	data = get_data(is_test)

	part_1_result = execute(data, is_part_one=True)
	print("Part 1: " + str(part_1_result))
	if not is_test: 
		assert part_1_result == 252656917

	part_2_result = execute(data, is_part_one=False)
	print("Part 2: " + str(part_2_result))
	if not is_test: 
		assert part_2_result == 253499763

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

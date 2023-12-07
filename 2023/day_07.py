import sys
from enum import Enum
from functools import cmp_to_key

TEST_PATH = './test_data/input_07.txt'
DATA_PATH = './data/input_07.txt'

HAND_TYPES = Enum('CARD_TYPES', [
	'FIVE_OF_A_KIND',
	'FOUR_OF_A_KIND',
	'FULL_HOUSE',
	'THREE_OF_A_KIND',
	'TWO_PAIR',
	'ONE_PAIR',
	'HIGH_CARD'
])

CARD_TYPES = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

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

def get_card_bucket(hand_counter):
	vals = list(hand_counter.values())

	if 5 in vals:
		return HAND_TYPES.FULL_HOUSE
	if 4 in vals:
		return HAND_TYPES.FOUR_OF_A_KIND
	if 3 in vals and 2 in vals:
		return HAND_TYPES.FULL_HOUSE
	if 3 in vals:
		return HAND_TYPES.THREE_OF_A_KIND
	if 2 in vals and vals.index(2) != (len(vals) - 1 - vals[::-1].index(2)):
		return HAND_TYPES.TWO_PAIR
	if 2 in vals:
		return HAND_TYPES.ONE_PAIR
	if 1 in vals and len(set(vals)) == 1:
		return HAND_TYPES.HIGH_CARD
	raise Exception('how did you get here')

def compare(item_1, item_2):
	for idx in range(len(item_1)):
		if CARD_TYPES.index(item_1[idx]) < CARD_TYPES.index(item_2[idx]):
			return -1
		elif CARD_TYPES.index(item_1[idx]) > CARD_TYPES.index(item_2[idx]):
			return 1
	raise Exception("Could not compare")

def part_1(data):
	buckets = {e: [] for e in HAND_TYPES}

	hand_to_bid = {hand: int(bid) for (hand, bid) in data}

	for hand, _ in data:
		hand_counter = get_hand_counter(hand)
		bucket_to_place_in = get_card_bucket(hand_counter)
		print(hand, bucket_to_place_in)
		buckets[bucket_to_place_in].append(hand)

	final_ranking = []

	for hand_type in HAND_TYPES:
		print(hand_type)
		hands_in_bucket = buckets[hand_type]
		if len(hands_in_bucket) == 1:
			final_ranking.append(hands_in_bucket[0])
		elif len(hands_in_bucket) > 1:
			sorted_hands = sorted(hands_in_bucket, key=cmp_to_key(compare))
			for hand in sorted_hands:
				final_ranking.append(hand)

	print("FINAL")
	print(final_ranking)

	total_score = 0

	for idx, hand in enumerate(final_ranking[::-1]):
		total_score += (idx+1) * hand_to_bid[hand]

	print(total_score)

def main(is_test):
	data = get_data(is_test)
	part_1(data)

if __name__ == "__main__":
	main(len(sys.argv) > 1 and sys.argv[1].lower() == '--test')

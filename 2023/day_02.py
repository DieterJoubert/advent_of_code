DATA_PATH = './data/input_02.txt'

BAG_CONTENT = {
	'red': 12,
	'green': 13,
	'blue': 14
}

def get_data():
	with open(DATA_PATH) as f:
		lines = f.read().splitlines()
		data = []

		for line in lines:
			_, game_content = line.split(':')
      			 
			this_game = []

			for set_content in game_content.split(';'):
				this_game_set = {}
				set_reveals = set_content.split(',')
				for reveal in set_reveals:
					num, color = reveal.strip().split()
					this_game_set[color] = int(num)
				
				this_game.append(this_game_set)
            
			data.append(this_game)
		
		return data

def get_possible_game_indexes(data):
	possible_games = []

	for idx in range(len(data)):
		game = data[idx]

		possible = True

		for reveal in game:
			for color, num in reveal.items():
				if BAG_CONTENT[color] < num:
					possible = False
					break

		if possible:
			possible_games.append(idx+1)
	
	return possible_games

def part_1(data):
	possible_games = get_possible_game_indexes(data)
	print(sum(possible_games))

def part_2(data):
	pass

def main():
	data = get_data()
	part_1(data)
	part_2(data)

if __name__ == "__main__":
  main()

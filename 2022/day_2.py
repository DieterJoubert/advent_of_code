# A for Rock, B for Paper, and C for Scissors.
# X for Rock, Y for Paper, and Z for Scissors.
# shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors)

choice_to_score = {
   'X': 1,
   'Y': 2,
   'Z': 3
}

choice_to_tie = {
   'X': 'A',
   'Y': 'B',
   'Z': 'C'
}

choice_to_victory = {
   'X': 'C',
   'Y': 'A',
   'Z': 'B'
}

def get_data():
   data = []
   with open('./data/input_2.txt') as f:
      lines = f.read().splitlines()
      for line in lines:
         data.append(tuple(line.split()))
   return data

def main():
   data = get_data()
   total_score = sum(map(get_score_for_round, data))
   print(total_score)

def get_score_for_round(round):
   score = 0

   opponent = round[0]
   you = round[1]

   score += choice_to_score[you]

   if choice_to_tie[you] == opponent:
      score += 3
   elif choice_to_victory[you] == opponent:
      score += 6

   return score

if __name__ == "__main__":
   main()

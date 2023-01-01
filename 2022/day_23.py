# If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

DIRECTIONS = {
   'N': (-1, 0),
   'S': (+1, 0),
   'W': (0, -1),
   'E': (0, +1),
   'NE': (-1, +1),
   'NW': (-1, -1),
   'SW': (+1, -1),
   'SE': (+1, +1)
}

DATA_PATH = './test_data/input_23.txt'

NUM_ROUNDS = 10

def get_input_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         data.append([x for x in line])
   return data

def get_grid_dict(data):
   grid = set()
   for i in range(len(data)):
      for j in range(len(data[0])):
         if data[i][j] == '#':
            grid.add((i,j))
   return grid

def get_move_direction(elf, proposition_options):
   pass

def play_round(proposition_options, elves):
   elf_to_proposal = {}
   proposal_to_elf = {}

   for elf in elves:
      direction = get_move_direction(elf, proposition_options)
      

def main():
   data = get_input_data()
   grid = get_grid_dict(data)

   proposition_options = ['N', 'S', 'W', 'E']

   for d in data:
      print(d)
   print(grid)
   
   for round in range(NUM_ROUNDS):
      play_round(proposition_options, grid)
   

if __name__ == "__main__":
   main()

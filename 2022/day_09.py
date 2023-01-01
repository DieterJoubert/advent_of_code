DATA_PATH = './data/input_9.txt'

direction_to_delta = {
   'U': (-1, 0),
   'D': (1, 0),
   'L': (0, -1),
   'R': (0, 1),
   'UL': (-1, -1),
   'UR': (-1, 1),
   'DL': (1, -1),
   'DR': (1, 1)
}

class GameState(object):
   def __init__(self):
      start = (4,0)
      self.head_pos = start
      self.tail_pos = start
      self.visited = {start}

def get_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         parsed = line.split()
         data.append((parsed[0], int(parsed[1])))
   return data

def get_neighbors(pos):
   i, j = pos
   neighbors = set()
   for x in range(-1, 2):
      for y in range(-1, 2):
         if x == y == 0:
            continue
         neighbors.add((i+x, j+y))
   return neighbors

def move_tail(state, direction):
   i_delta, j_delta = direction_to_delta[direction]
   new_tail_pos = (state.tail_pos[0] + i_delta, state.tail_pos[1] + j_delta)
   state.visited.add(new_tail_pos)
   state.tail_pos = new_tail_pos

   # print("-------")
   # print(state.head_pos)
   # print(state.tail_pos)

def check_tail(state):
   head_pos = state.head_pos
   tail_pos = state.tail_pos

   if head_pos == tail_pos:
      return
   neighbors = get_neighbors(tail_pos)
   if head_pos in neighbors:
      return
   
   if head_pos[0] == tail_pos[0]:
      if head_pos[1] > tail_pos[1]:
         return move_tail(state, 'R')
      else:
         return move_tail(state, 'L')

   if head_pos[1] == tail_pos[1]:
      if head_pos[0] > tail_pos[0]:
         return move_tail(state, 'D')
      else:
         return move_tail(state, 'U')

   if head_pos[0] > tail_pos[0]:
      if head_pos[1] > tail_pos[1]:
         return move_tail(state, 'DR')
      else:
         return move_tail(state, 'DL')

   if head_pos[0] < tail_pos[0]:
      if head_pos[1] > tail_pos[1]:
         return move_tail(state, 'UR')
      else:
         return move_tail(state, 'UL')

def perform_step(state, direction):
   i_delta, j_delta = direction_to_delta[direction]
   state.head_pos = (state.head_pos[0]+i_delta, state.head_pos[1]+j_delta)

def perform_instruction(state, instruction):
   direction, steps = instruction

   for _ in range(steps):
      perform_step(state, direction)
      check_tail(state)

def solve(instructions_list):
   state = GameState()

   for instruction in instructions_list:
      perform_instruction(state, instruction)

   return state.visited

def main():
   data = get_data()
   soln = solve(data)
   print(len(soln))

if __name__ == "__main__":
   main()

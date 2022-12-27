DATA_PATH = './data/input_10.txt'

cycles_to_check = [20, 60, 100, 140, 180, 220]

def get_input():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         parsed = line.split()
         if len(parsed) == 1:
            data.append((parsed[0], None))
         else:
            data.append((parsed[0], int(parsed[1])))
   return data

def get_cycle_to_signal_strength(input):
   signal_strength = {}

   register = 1
   cycle = 0
   curr_inst_idx = 0
   blocked = False

   while curr_inst_idx < len(input):
      cycle += 1
      curr_instruction = input[curr_inst_idx]

      signal_strength[cycle] = cycle * register

      if blocked:
         register += curr_instruction[1]
         curr_inst_idx += 1
         blocked = False
         continue
      if curr_instruction[0] == 'noop':
         curr_inst_idx += 1
         continue
      if curr_instruction[0] == 'addx':
         blocked = True

   return signal_strength

def main():
   input = get_input()
   print(input)
   signal_strength = get_cycle_to_signal_strength(input)

   soln = 0
   for x in cycles_to_check:
      soln += signal_strength[x]
   print(soln)

if __name__ == "__main__":
   main()

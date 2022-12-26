from functools import reduce

DATA_PATH = './data/input_5.txt'

def get_lines():
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      idx = lines.index('')
      return (lines[:idx], lines[idx+1:])

def get_initial_stacks(lines):
   data = {}
   stacks = lines[0]
   crates = lines[1:]

   for i in range(len(stacks)):
      curr_char = stacks[i]
      if curr_char.isdigit():
         curr_stack = int(curr_char)
         data[curr_stack] = []
         for j in range(len(crates)):
            curr_crate = crates[j][i]
            if curr_crate.isalpha():
               data[curr_stack].append(curr_crate)
   
   return data

def get_instructions_from_lines(lines):
   data = []
   for line in lines:
      curr_instruction = []
      for segment in line.split():
         if segment.isdigit():
            curr_instruction.append(segment)
      data.append(tuple(map(int, curr_instruction)))
   return data

def get_data():
   stack_lines, instruction_lines = get_lines()
   stacks = get_initial_stacks(stack_lines[::-1])
   instructions = get_instructions_from_lines(instruction_lines)
   return (stacks, instructions)

def perform_instruction(stacks, instruction, one_by_one):
   num, from_crate, to_crate = instruction

   if one_by_one:
      for _ in range(num):
         item = stacks[from_crate].pop()
         stacks[to_crate].append(item)
   else:
      items = []
      for _ in range(num):
         items.append(stacks[from_crate].pop())
      for item in items[::-1]:
         stacks[to_crate].append(item)

   return stacks

def perform_instructions(stacks, instructions, one_by_one=True):
   return reduce(lambda s, inst: perform_instruction(s, inst, one_by_one), instructions, stacks)

def get_soln(final_stacks):
   soln = ''
   for k in sorted(final_stacks.keys()):
      soln += final_stacks[k][-1]
   return soln

def run(one_by_one=True):
   stacks, instructions = get_data()
   final_stacks_one_by_one = perform_instructions(stacks, instructions, one_by_one)
   soln = get_soln(final_stacks_one_by_one)
   print(soln)

def main():
   run(True)
   run(False)

if __name__ == "__main__":
   main()

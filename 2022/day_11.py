
DATA_PATH = './test_data/input_11.txt'

class Monkey(object):
   def __init__(self, idx, starting_items, operation):
      self.idx = idx
      self.starting_items = starting_items
      self.operation = operation

def get_chunks(lines):
   chunks = [[]]
   for line in lines:
      if not line:
         chunks.append([])
         continue
      chunks[-1].append(line.strip())
   return chunks

def get_input_data():
   monkeys = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      chunks = get_chunks(lines)
      for chunk in chunks:
         idx = chunk[0]
         monkey = Monkey()
   return monkeys

def main():
   data = get_input_data()

if __name__ == '__main__':
   main()

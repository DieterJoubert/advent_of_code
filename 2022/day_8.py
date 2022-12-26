DATA_PATH = './data/input_8.txt'

class Highest(object):
   def __init__(self):
      self.left = 0
      self.right = 0
      self.top = 0
      self.bottom = 0

   def set_left(self, new_left):
      self.left = max(self.left, new_left)

   def set_right(self, new_right):
      self.right = max(self.right, new_right)

   def set_top(self, new_top):
      self.top = max(self.top, new_top)

   def set_bottom(self, new_bottom):
      self.bottom = max(self.bottom, new_bottom)

def get_data():
   grid = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         grid.append(list(map(int, line)))
   return grid
      
def initialize_lookup(grid):
   lookup = {}
   for i in range(len(grid)):
      for j in range(len(grid[0])):
         lookup[(i, j)] = Highest()
   return lookup

def solve(grid):
   lookup = initialize_lookup(grid)


def main():
   data = get_data()
   soln = solve(data)
   print(data)

if __name__ == "__main__":
   main()

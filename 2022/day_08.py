DATA_PATH = './data/input_8.txt'

class Highest(object):
   def __init__(self, height):
      self.left = 0
      self.right = 0
      self.top = 0
      self.bottom = 0
      self.height = height

def get_grid():
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
         height = grid[i][j]
         new_el = Highest(height)
         lookup[(i, j)] = new_el
   return lookup

def get_four_neighbors(i, j, lookup):
   top = lookup[(i-1, j)]
   bottom = lookup[(i+1, j)]
   left = lookup[(i, j-1)]
   right = lookup[(i, j+1)]
   return top, bottom, left, right

def explore_tree(i, j, lookup):
   curr = lookup[(i,j)]
   top, bottom, left, right = get_four_neighbors(i, j, lookup)

   curr.left = max(left.height, left.left)
   curr.right = max(right.height, right.right)
   curr.top = max(top.height, top.top)
   curr.bottom = max(bottom.height, bottom.bottom)

def get_completed_lookup(grid):
   lookup = initialize_lookup(grid)

   for i in range(1, len(grid)-1):
      for j in range(1, len(grid[0])-1):
         explore_tree(i, j, lookup)

   for i in range(len(grid)-2, 0, -1):
      for j in range(len(grid[0])-2, 0, -1):
         explore_tree(i, j, lookup)

   return lookup

def get_visible_from_lookup(grid, lookup):
   visible = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

   for i in range(len(grid)):
      for j in range(len(grid[0])):
         if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
            visible[i][j] = True
         else:
            curr = lookup[(i,j)]
            height = curr.height
            if height > min(curr.left, curr.right, curr.top, curr.bottom):
               visible[i][j] = True
   return visible

def get_num_visible(visible):
   total = 0
   for row in visible:
      total += row.count(True)
   return total

def explore_scenic_score(i, j, grid):
   grid_height = len(grid)
   grid_width = len(grid[0])

   for x in range(i-1, 0, -1):
      grid[x][j]

   for x in range(i+1, grid_height):
      grid[x][j]

   for x in range(j-1, 0, -1):
      grid[i][x]

   for x in range(j+1, grid_width):
      grid[i][x]

def get_max_scenic_score(grid):
   best_distance 
   for i in range(1, len(grid)-1):
      for j in range(1, len(grid[0])-1):
         distance = explore_scenic_score(i, j, grid)

def main():
   grid = get_grid()
   lookup = get_completed_lookup(grid)
   visible = get_visible_from_lookup(grid, lookup)
   num_visible = get_num_visible(visible)
   print(num_visible)

   max_scenic_score = get_max_scenic_score(grid)
   print(max_scenic_score)

if __name__ == "__main__":
   main()

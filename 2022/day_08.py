from functools import reduce

DATA_PATH = './data/input_08.txt'

direction_to_delta = {
   'N': (-1, 0),
   'S': (+1, 0),
   'W': (0, -1),
   'E': (0, +1)
}

def get_grid():
   grid = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         grid.append(list(map(int, line)))
   return grid
      
def is_visible_in_direction(grid, i, j, direction):
   this_height = grid[i][j]
   delta = direction_to_delta[direction]
   neighbor = (i + delta[0], j + delta[1])

   while True:
      if neighbor[0] < 0 or neighbor[0] >= len(grid):
         break
      if neighbor[1] < 0 or neighbor[1] >= len(grid[0]):
         break

      neighbor_height = grid[neighbor[0]][neighbor[1]]
      if neighbor_height >= this_height:
         return False

      neighbor = (neighbor[0] + delta[0], neighbor[1] + delta[1])

   return True
   
def is_node_visible(grid, i, j):
   if i == 0 or j == 0 or i == len(grid)-1 or j == len(grid[0])-1:
      return True

   for direction in direction_to_delta.keys():
      check_direction = is_visible_in_direction(grid, i, j, direction)
      if check_direction:
         return True

   return False

def get_visibility_grid(grid):
   is_visible = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

   for i in range(len(grid)):
      for j in range(len(grid[0])):
         is_visible[i][j] = is_node_visible(grid, i, j)

   return is_visible

def count_visible_trees(is_visible_grid):
   total = 0
   for row in is_visible_grid:
      for node in row:
         if node:
            total += 1
   return total

def get_viewing_distance_in_direction(grid, i, j, direction):
   distance = 0

   this_height = grid[i][j]
   delta = direction_to_delta[direction]
   neighbor = (i + delta[0], j + delta[1])

   while True:
      if neighbor[0] < 0 or neighbor[0] >= len(grid):
         break
      if neighbor[1] < 0 or neighbor[1] >= len(grid[0]):
         break

      distance += 1

      neighbor_height = grid[neighbor[0]][neighbor[1]]
      if neighbor_height >= this_height:
         break

      neighbor = (neighbor[0] + delta[0], neighbor[1] + delta[1])

   return distance

def get_viewing_distance(grid, i, j):
   distances = []

   for direction in direction_to_delta.keys():
      distances.append(get_viewing_distance_in_direction(grid, i, j, direction))

   return reduce(lambda x, y: x * y, distances)

def get_best_viewing_distance(grid):
   best = 0

   for i in range(1, len(grid)-1):
      for j in range(1, len(grid[0])-1):
         viewing_distance = get_viewing_distance(grid, i, j)
         best = max(best, viewing_distance)

   return best

def main():
   grid = get_grid()

   is_visible_grid = get_visibility_grid(grid)
   visibility_count = count_visible_trees(is_visible_grid)
   print(visibility_count)

   best_viewing_distance = get_best_viewing_distance(grid)
   print(best_viewing_distance)

if __name__ == "__main__":
   main()

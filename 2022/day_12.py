from collections import deque

DATA_PATH = './test_data/input_12.txt'

def get_input_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         data.append(list(line))
   return data

def get_coord(grid, letter):
   for i in range(len(grid)):
      for j in range(len(grid[0])):
         if grid[i][j] == letter:
            return (i, j)

def get_real_val(val):
   if not val.isalpha():
      raise Exception()
   if val == 'E':
      return 'z'
   if val == 'S':
      return 'a'
   return val

def get_accessible_neighbors(curr_node, grid):
   neighbors = []

   curr_val = get_real_val(grid[curr_node[0]][curr_node[1]])

   for x in range(-1, 2):
      for y in range(-1, 2):
         if abs(x) == abs(y):
            continue
         new_i = curr_node[0] + x
         new_j = curr_node[1] + y
         if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
            continue
         neighbor_val = get_real_val(grid[new_i][new_j])

         if ord(curr_val)+1 >= ord(neighbor_val):
            neighbors.append((new_i, new_j))

   return neighbors

def get_min_distances(grid):
   start_coord = get_coord(grid, 'S')
   
   distances = {start_coord: 0}
   explored = set()

   q = deque()
   q.append((start_coord, 0))

   while q:
      curr_node, curr_distance = q.popleft()

      if curr_node in explored:
         continue
      explored.add(curr_node)

      if curr_node not in distances:
         distances[curr_node] = curr_distance
      else:
         distances[curr_node] = min(curr_distance, distances[curr_node])

      accessible_neighbors = get_accessible_neighbors(curr_node, grid)
      for neighbor in accessible_neighbors:
         q.append((neighbor, curr_distance+1))

   return distances

def get_distance_to_end(grid, min_distances):
   end_coord = get_coord(grid, 'E')
   return min_distances[end_coord]

def get_coords(grid, letter):
   coords = []
   for i in range(len(grid)):
      for j in range(len(grid[0])):
         if grid[i][j] == letter:
            coords.append((i, j))
   return coords

def get_part_two(grid):
   start_coord = get_coord(grid, 'S')
   grid[start_coord[0]][start_coord[1]] = 'a'

   a_coords = get_coords(grid, 'a')
   
   explored = set()
   distances = {}
   q = deque()

   for coord in a_coords:
      q.append((coord, 0))

   while q:
      curr_node, curr_distance = q.popleft()

      if curr_node in explored:
         continue
      explored.add(curr_node)

      if curr_node not in distances:
         distances[curr_node] = curr_distance
      else:
         distances[curr_node] = min(curr_distance, distances[curr_node])

      accessible_neighbors = get_accessible_neighbors(curr_node, grid)
      for neighbor in accessible_neighbors:
         q.append((neighbor, curr_distance+1))

   return distances

def main():
   grid = get_input_data()

   # min_distances = get_min_distances(grid)
   # print(min_distances)
   # distance_to_end = get_distance_to_end(grid, min_distances)
   # print(distance_to_end)

   min_distances = get_part_two(grid)
   print(min_distances)
   distance_to_end = get_distance_to_end(grid, min_distances)
   print(distance_to_end)

if __name__ == "__main__":
   main()

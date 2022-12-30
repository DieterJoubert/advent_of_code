import re
from collections import deque

DATA_PATH = './test_data/input_15.txt'

def get_input_data():
   data = {}
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         s = re.split(' |=|;|,|:', line)
         sensor = tuple(map(int, [s[3], s[6]]))
         beacon = tuple(map(int, [s[13], s[16]]))
         data[sensor] = beacon
   return data

def get_grid(data):
   max_x, max_y = 0, 0
   for sensor, beacon in data.items():
      max_x = max(max_x, sensor[0], beacon[0])
      max_y = max(max_y, sensor[1], beacon[1])

   grid = [['_' for _ in range(max_y+1)] for _ in range(max_x+1) ]

   for sensor, beacon in data.items():
      grid[sensor[0]][sensor[1]] = 'S'
      grid[beacon[0]][beacon[1]] = 'B'

   return grid

def get_manhattan_distance(point_a, point_b):
   return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])

def get_manhattan_neighbors(grid, coord):
   neighbors = []
   for i in (-1, 0, 1):
      for j in (-1, 0, 1):
         new_i = coord[0]+i
         new_j = coord[1]+j
         if new_i < 0 or new_j < 0:
            continue
         if new_i >= len(grid) or new_j >= len(grid[0]):
            continue
         if abs(i) != abs(j):
            neighbors.append((new_i, new_j))
   return neighbors

def explore_for_point(grid, sensor, beacon):
   manhattan_distance = get_manhattan_distance(sensor, beacon)
   print(manhattan_distance)

   explored = set()

   q = deque()
   q.append((sensor, 0))

   while q:
      curr_node, curr_distance = q.popleft()
      if curr_node in explored:
         continue
      if curr_distance > manhattan_distance:
         continue

      explored.add(curr_node)

      if grid[curr_node[0]][curr_node[1]] == '_':
         grid[curr_node[0]][curr_node[1]] = '#'

      neighbors = get_manhattan_neighbors(grid, curr_node)
      print(curr_node, neighbors)

      for neighbor in neighbors:
         q.append((neighbor, curr_distance+1))

   for g in grid:
      print(g)
      #print("".join(g))
      
def explore_all_sensors(sensor_beacon_dict, grid):
   for sensor, beacon in sensor_beacon_dict.items():
      explore_for_point(grid, sensor, beacon)

def main():
   data = get_input_data()

   grid = get_grid(data)

   explore_all_sensors(data, grid)

if __name__ == "__main__":
   main()

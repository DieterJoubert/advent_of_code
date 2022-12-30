import re
from collections import deque

DATA_PATH = './data/input_15.txt'

BOUNDS = (0, 4000000)

def get_input_data():
   data = {}
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         s = re.split(' |=|;|,|:', line)
         sensor = tuple(map(int, [s[6], s[3]]))
         beacon = tuple(map(int, [s[16], s[13]]))
         data[sensor] = beacon
   return data

def get_grid(data):
   grid = {}

   for sensor, beacon in data.items():
      grid[sensor] = 'S'
      grid[beacon] = 'B'

   return grid

def get_manhattan_distance(point_a, point_b):
   return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])


def get_row_data(data, row_to_investigate):
   row_data = {}

   for sensor, beacon in data.items():
      if sensor[0] == row_to_investigate:
         row_data[sensor[1]] = 'S'
      if beacon[0] == row_to_investigate:
         row_data[beacon[1]] = 'B'

   return row_data

def explore_for_sensor(sensor, beacon, row_data, row_to_investigate):
   sensor_distance = get_manhattan_distance(sensor, beacon)
   coord_perpendicular = (row_to_investigate, sensor[1])
   row_distance = get_manhattan_distance(sensor, coord_perpendicular)

   if row_distance > sensor_distance:
      return

   distance_remaining = sensor_distance - row_distance

   for delta in range(-distance_remaining, distance_remaining+1):
      curr_j = sensor[1]+delta
      curr = (row_to_investigate, curr_j)
      if curr_j in row_data:
         continue
      row_data[curr_j] = '#'

def get_sensed_spaces_in_row(row_data):
   count = 0
   for key, value in row_data.items():
      if value == '#':
         count += 1
   return count

def main():
   row_to_investigate = 2000000 #10

   data = get_input_data()

   row_data = get_row_data(data, row_to_investigate)

   for sensor, beacon in data.items():
      explore_for_sensor(sensor, beacon, row_data, row_to_investigate)

   soln = get_sensed_spaces_in_row(row_data)
   print(soln)

if __name__ == "__main__":
   main()

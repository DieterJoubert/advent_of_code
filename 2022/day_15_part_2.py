import re
from collections import deque

DATA_PATH = './data/input_15.txt'

MIN_BOUND = 0
MAX_BOUND = 4000000

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

def get_sensor_to_range(sensor_beacon_dict):
   sensor_to_range = {}

   for sensor, beacon in sensor_beacon_dict.items():
      distance = get_manhattan_distance(sensor, beacon)
      sensor_to_range[sensor] = distance

   return sensor_to_range

def get_manhattan_distance(point_a, point_b):
   return abs(point_a[0]-point_b[0]) + abs(point_a[1]-point_b[1])

def get_frontier_points_for_sensor(sensor, range):
   print('for sensor')
   frontier = set()
   range_plus = range+1

   left = sensor[0], sensor[1]-range_plus
   right = sensor[0], sensor[1]+range_plus 
   top = sensor[0]-range_plus, sensor[1]
   bottom = sensor[0]+range_plus, sensor[1]

   sides = [get_side(left, top, (-1, +1)), 
            get_side(top, right, (+1, +1)),
            get_side(right, bottom, (+1, -1)), 
            get_side(bottom, left, (-1, -1))]

   for side in sides:
      for p in side:
         frontier.add(p)

   return frontier

def get_side(start, stop, modifier):
   points = set()
   curr = start

   while True:
      if curr[0] >= MIN_BOUND and curr[0] <= MAX_BOUND and curr[1] >= MIN_BOUND and curr[1] <= MAX_BOUND:
         points.add(curr)
      if curr == stop:
         break
      curr = (curr[0]+modifier[0], curr[1]+modifier[1])
   
   return points

def get_all_frontier_points(sensor_to_range):
   all_frontier_points = set()

   for sensor, range in sensor_to_range.items():
      frontier = get_frontier_points_for_sensor(sensor, range)
      for f in frontier:
         all_frontier_points.add(f)

   return all_frontier_points

def is_point_inside_sensor(point, sensor, range):
   distance = get_manhattan_distance(point, sensor)
   if distance > range:
      return False
   return True

def check_point(point, sensor_to_range):
   for sensor, range in sensor_to_range.items():
      is_inside = is_point_inside_sensor(point, sensor, range)
      if is_inside:
         return False
   return True

def get_soln(all_frontier_points, sensor_to_range):
   soln_points = []

   for p in all_frontier_points:
      foo = check_point(p, sensor_to_range)
      if foo:
         soln_points.append(p)

   return soln_points

def main():
   data = get_input_data()

   sensor_to_range = get_sensor_to_range(data)
   print(sensor_to_range)

   all_frontier_points = get_all_frontier_points(sensor_to_range)
   print(len(all_frontier_points))

   soln = get_soln(all_frontier_points, sensor_to_range)
   print("SOLN", soln)

if __name__ == "__main__":
   main()

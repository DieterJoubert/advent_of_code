import re
from collections import deque

DATA_PATH = './test_data/input_16.txt'

def get_input_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         s = re.split(' |=|;|,', line)
         valve = s[1]
         rate = int(s[5])
         leads_to = [x for x in s[11:] if x]
         data.append([valve, rate, leads_to])
   return data

def get_valve_graph_and_rate(input_data):
   valve_graph = {}
   valve_to_rate = {}

   for d in input_data:
      valve, rate, leads_to = d
      valve_graph[valve] = leads_to
      valve_to_rate[valve] = rate

   return valve_graph, valve_to_rate

def get_pairwise_distances(valve_graph):
   pairwise_distances = {}

   for start_node in valve_graph.keys():
      explored = set()

      q = deque()
      q.append((start_node, 0))

      while q:
         curr, curr_distance = q.pop()
         explored.add(curr)

         if (start_node, curr) not in pairwise_distances:
            pairwise_distances[(start_node, curr)] = curr_distance
         else:
            pairwise_distances[(start_node, curr)] = min(curr_distance, pairwise_distances[(start_node, curr)])

         neighbors = valve_graph[curr]
         for neighbor in neighbors:
            if neighbor in explored:
               continue
            q.append((neighbor, curr_distance+1))
   
   return pairwise_distances

def main():
   input_data = get_input_data()
   valve_graph, valve_to_rate = get_valve_graph_and_rate(input_data)
   pairwise_distances = get_pairwise_distances(valve_graph)
   print(pairwise_distances)


if __name__ == "__main__":
   main()

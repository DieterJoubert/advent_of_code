import re
from collections import deque
from functools import reduce

DATA_PATH = './data/input_07.txt'

### CLASS DEFINITIONS

class Directory(object):
   def __init__(self, name, parent):
      self.name = name
      self.parent = parent
      self.children = []
      self.type = 'DIR'
   
   def add_child(self, child):
      self.children.append(child)

   def get_size(self):
      return sum(map(lambda x: x.get_size(), self.children))

class File(object):
   def __init__(self, name, size, parent):
      self.name = name
      self.size = size
      self.parent = parent
      self.type = 'FILE'

   def get_size(self):
      return self.size

## INPUT PARSING

def get_input_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         data.append(line.split())
   return data

def get_dir_content(idx, data):
   content = []

   pointer = idx+1

   while True:
      if pointer >= len(data):
         break
      curr = data[pointer]
      if curr[0] == '$':
         break
      content.append(curr)
      pointer += 1

   return content

def build_file_tree(data):
   root = Directory("/", None)
   curr = root

   data = data[1:]

   for idx in range(len(data)):
      line = data[idx]
      if line[0] == '$':
         if line[1] == 'cd':
            if line[2] == '..':
               curr = curr.parent
            else:
               new_dir_name = line[2]
               new_dir = Directory(new_dir_name, curr)
               curr.add_child(new_dir)
               curr = new_dir
         if line[1] == 'ls':
            content = get_dir_content(idx, data)
            for c in content:
               if c[0] != 'dir':
                  new_file = File(name=c[1], size=int(c[0]), parent=curr)
                  curr.add_child(new_file)

   return root

## COMPUTATION

def get_leaves_and_directories_bfs(root):
   q = deque()

   leaves = []
   directories = []

   q.append(root)

   while q:
      curr = q.popleft()

      if curr.type == 'FILE':
         leaves.append(curr)
      else:
         directories.append(curr)

      if hasattr(curr, "children"):
         for child in curr.children:
            q.append(child)

   return leaves, directories

def get_sum_of_dirs_less_than_max(directories):
   max_size = 100000
   total = 0

   for d in directories:
      size = d.get_size()
      if size <= max_size:
         total += size

   return total

def get_directory_to_delete(root, directories):
   max_disk_space_used = 40000000
   current_space_used = root.get_size()

   best = (None, 0)

   for d in directories:
      size = d.get_size()
      potential_space = current_space_used - size
   
      if potential_space < max_disk_space_used:
         if best[1] < potential_space:
            best = (d, potential_space)

   return best[0]

def solve(tree_root):
   leaves, directories = get_leaves_and_directories_bfs(tree_root)

   sum_of_dirs = get_sum_of_dirs_less_than_max(directories)
   print("SUM SIZE", sum_of_dirs)

   to_delete = get_directory_to_delete(tree_root, directories)
   print("TO DELETE", to_delete.name, to_delete.get_size())


def main():
   data = get_input_data()
   tree_root = build_file_tree(data)
   solve(tree_root)

if __name__ == "__main__":
   main()

DATA_PATH = './data/input_4.txt'

def get_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         first_half, second_half = line.split(",")
         data.append((tuple(map(int, first_half.split('-'))), tuple(map(int, second_half.split('-')))))
   return data

def is_fully_contained(a, b):
   if a[0] <= b[0] and a[1] >= b[1]:
      return True
   if a[0] >= b[0] and a[1] <= b[1]:
      return True
   return False

def main():
   data = get_data()
   soln = sum([1 if is_fully_contained(x[0], x[1]) else 0 for x in data])
   print(soln)

if __name__ == "__main__":
   main()

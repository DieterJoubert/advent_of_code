DATA_PATH = './data/input_8.txt'

def get_data():
   grid = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         grid.append(list(map(int, line)))
   return grid
      
def main():
   data = get_data()
   print(data)

if __name__ == "__main__":
   main()

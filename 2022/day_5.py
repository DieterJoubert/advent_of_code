DATA_PATH = './data/input_5.txt'

def get_data():
   stacks = {}
   instructions = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         print(line)
         if not line:
            break
   return data


def main():
   data = get_data()


if __name__ == "__main__":
   main()

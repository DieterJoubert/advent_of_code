DATA_PATH = './data/input_6.txt'

def get_data():
   with open(DATA_PATH) as f:
      return f.read().splitlines()[0]
      
def get_buffer_len(stream, size):
   for i in range(len(stream)):
      curr = stream[i:i+size]
      if len(set(curr)) == size:
         return i+size

def main():
   data = get_data()
   soln = get_buffer_len(data, 4)
   print(soln)
   
   soln = get_buffer_len(data, 14)
   print(soln)


if __name__ == "__main__":
   main()

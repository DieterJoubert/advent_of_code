DATA_PATH = './data/input_01.txt'

def get_data():
    with open(DATA_PATH) as f:
        lines = f.read().splitlines()
        return lines

int_map = {
   'one': 1,
   'two': 2, 
   'three': 3, 
   'four': 4, 
   'five': 5, 
   'six': 6, 
   'seven': 7, 
   'eight': 8, 
   'nine': 9
}

def check_for_hidden_int(segment):
   if segment[:3] in int_map:
      return int_map[segment[:3]]
   if segment[:4] in int_map:
      return int_map[segment[:4]]
   if segment[:5] in int_map:
      return int_map[segment[:5]]
   return None 
   
def get_line_calibration_value_with_hidden(line):
  first, last = None, None
  
  for idx in range(len(line)):
      char = line[idx]
      if char.isnumeric():
         first = int(char)
         break
      hidden_int = check_for_hidden_int(line[idx:idx+5])
      if hidden_int:
         first = hidden_int
         break
      
  for idx in range(len(line)-1, -1, -1):
      char = line[idx]
      if char.isnumeric():
         last = int(char)
         break
      hidden_int = check_for_hidden_int(line[idx:idx+5])
      if hidden_int:
         last = hidden_int
         break
  
  return int(str(first) + str(last))
      
def part_1(data):
   def get_line_calibration_value(line):
      first = next(x for x in line if x.isnumeric())
      last = next(x for x in line[::-1] if x.isnumeric())
      return int(first + last)
   
   calibration_values = [get_line_calibration_value(x) for x in data]
   print(sum(calibration_values))

def part_2(data):
  calibration_values = [get_line_calibration_value_with_hidden(x) for x in data]
  print(sum(calibration_values))

def main():
  data = get_data()

  part_1(data)
  part_2(data)

if __name__ == "__main__":
  main()

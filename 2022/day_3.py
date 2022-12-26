# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

DATA_PATH = './data/input_3.txt'

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
item_to_priority = {chars[x]: (x+1) for x in range(len(chars)) }

def get_data():
   data = []
   with open(DATA_PATH) as f:
      lines = f.read().splitlines()
      for line in lines:
         first_half = line[:int(len(line)/2)]
         second_half = line[int(len(line)/2):]
         data.append((first_half, second_half))
   return data

def get_duplicate_item(rucksack):

   first_compartment = set([x for x in rucksack[0]])
   for item in rucksack[1]:
      if item in first_compartment:
         return item
   raise Exception("How did you get here")

def main():
   data = get_data()
   duplicate_items = map(get_duplicate_item, data)
   soln = sum([item_to_priority[x] for x in duplicate_items])
   print(soln)

if __name__ == "__main__":
   main()

def get_data():
    data = [[]]
    with open('./data/input_1.txt') as f:
        lines = f.read().splitlines()
        for line in lines:
          if not line:
            data.append([])
          else:
            data[-1].append(int(line))
    return data

def main():
  data = get_data()

  sums = [sum(x) for x in data]
  print(max(sums))

if __name__ == "__main__":
  main()

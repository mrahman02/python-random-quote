import random

def main_func():
  #print("Keep it logically awesome.")

  f = open("./quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)

  print(quotes[rnd])

if __name__== "__main__":
  main_func()

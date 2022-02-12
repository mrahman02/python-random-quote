from email.quoprimime import quote
import random

def main_func():
  #print("Keep it logically awesome.")

  f = open("./quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes)-1
  rnd = random.randint(0, last)
  rnd2 = random.randint(0, last)
  
  selected_quote = quotes[rnd].replace('\n', ' : ') + " "+ quotes[rnd2]
  print(selected_quote)
  #print(quotes[rnd2])

if __name__== "__main__":
  main_func()

from email.quoprimime import quote
import random
import sys

def main_func():
  #print("Keep it logically awesome.")

  f = open("./quotes.txt", "r")
  quotes = f.readlines()
  f.close()

  if(len(quotes)==0):
    print("No quotes found!")
  else:

    last = len(quotes)-1
    rnd = random.randint(0, last)
    rnd2 = random.randint(0, last)
    
    selected_quote = quotes[rnd].replace('\n', ' : ') + " "+ quotes[rnd2]
    print(selected_quote)
  

  print("You can input quotes (q to quit):")
  for line in sys.stdin:
    if 'q' == line.rstrip():
      break

    f = open("./quotes.txt", "a")
    f.write(line)
    f.close()
    print(f'Saved : {line}')
    print("You can input another quote (q to quit):")

  

if __name__== "__main__":
  main_func()

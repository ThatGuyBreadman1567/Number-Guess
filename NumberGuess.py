#Benjamin Readman
#NumberGuess
import random
num=random.randrange(1,20)
numg=int(input("Please try to guess the number I'm thinking of."))
if numg == num:
  print("Good job, you guessed, ",num,". That is correct.", sep=(""))
elif numg >= 1 and numg <= 20 and numg != num:
  print("Sorry, that is not the correct number. The number I was thinking of was, ",num,".",sep=(""))
elif numg > 20 or numg < 1:
  print("That is not exceptable, goodbye.")

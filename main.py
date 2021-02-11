import random

print("Coin Flip")

# 1 = heads, 2 = tails
coin = random.randint(1,2)

if(coin == 1):
  print("It's heads!")
else:
  print("It's tails!")

print("Dice Roll")

# Exercise: Create a code that mimics a dice roll using random numbers. The code should print out what number is "rolled", letting the use know what the result is.

dice = random.randint(1,6)

if(dice == 1):
  print("You rolled a 1")
elif(dice == 2):
  print("You rolled a 2")
elif(dice == 3):
  print("You rolled a 3")
elif(dice == 4):
  print("You rolled a 4")
elif(dice == 5):
  print("You rolled a 5")
else:
  print("You rolled a 6")
#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(10000):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
  #find the sum total of the two dice
    diceSum=(dice1+dice2)
    rolls[diceSum-1]=rolls[diceSum-1]+1
  #print statictics for dice rolls
  diceSum=1
  print("Count:")
  for count in rolls:
    print(diceSum, ":", count)
    diceSum=diceSum  + 1
  diceSum=1
  print("Percentage:")
  for item in rolls:
    print(diceSum, ":", item/100, "%")
    diceSum=diceSum+1
if __name__ == '__main__':
  main()

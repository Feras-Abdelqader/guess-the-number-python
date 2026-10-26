# Guess The Correct Number
import random

def Check(num):
    while num < 1 or num > 10:
        num = int(input("Please Enter Number between 1 and 10: "))
    return num
  
print("""
====================================
       🎮 GUESS THE NUMBER 🎮
====================================

Welcome, Player!

📝 HOW TO PLAY:
1. The computer will generate a secret number
   between 1 and 100.
2. Your mission is to guess the secret number.
3. After each guess, the computer will give you a hint:
   - HIGH
   - LOW
   - CORRECT
4. Invalid numbers (outside 1-10) don't count.

Good Luck, Player!
====================================
""")

computer = random.randint(1,10)
num = int(input("Pick a number from 1 and 10: "))
user = Check(num)
attempts = 5
while attempts > 0:
    
  if user < computer:
    print(f"YOUR NUMBER IS LOW,")
  elif user > computer:
    print(f"YOUR NUMBER IS HIGH,")
  else:
    print("\nCorrect! You Win!")
    break
    
  attempts -=1
  if attempts == 0:
    print("\n 💀 GAME OVER!")
    print("The correct number was:", computer)
    break
  
  num = int(input(f"Try Again! Attempts left: {attempts}: "))
  user = Check(num)
  

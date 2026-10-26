# Guess The Correct Number
import random

def check(num):
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
   between 1 and 10.
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
num = int(input("Pick a number between 1 and 10: "))
user = check(num)
attempts = 5
while attempts > 0:
    
  if user < computer:
    print("Too low! Try a higher number.")
  elif user > computer:
    print("Too high! Try a lower number.")
  else:
    print("\nCorrect! You Win!")
    break
    
  attempts -=1
  if attempts == 0:
    print("\n 💀 GAME OVER!")
    print("The correct number was:", computer)
    break
  
  num = int(input(f"Attempts left {attempts} : "))
  user = check(num)
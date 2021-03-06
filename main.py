#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random

selected_number = random.randint(1, 100)
is_game_over = False
guess = 0
print("Welcome to the Guessing Game.")
difficulty = input("Easy or Hard?\n").lower()

if difficulty == 'easy':
  guess = 10
elif difficulty =='hard':
  guess = 5

while not is_game_over:
  plr_guess = int(input("Guess a number between 1-100:\n"))
  if plr_guess < selected_number:
    guess -= 1
    print(f"Too Low. {guess} tries left.")
  elif plr_guess > selected_number:
    guess -= 1
    print(f"Too High. {guess} tries left.")
  elif plr_guess == selected_number:
    is_game_over = True
    print(f"Correct!! The selected_number was: {selected_number}, with only {guess} tries left.")
  if guess == 0:
    is_game_over = True
    print(f"Game Over! The number was {selected_number}.")
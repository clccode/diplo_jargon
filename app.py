import random
import os
import subprocess
from diplomacy_words import DIPLOMACY_WORDS

# clear screen
def clear_screen():
  if os.name == 'nt':
    subprocess.run(["cls"], shell=True)
  else:
    subprocess.run(["clear"])

# game play
def play_game():
  print("~" * 45)
  print()
  print("   Welcome to Diplo Jargon Jumble!")
  print("   A Diplomacy-Themed Word Scramble Game")
  print()
  print("~" * 45)

  ROUNDS = 10
  round_num = 1
  score = 0
  used = []

  while round_num <= ROUNDS:
    
    word, hint = random.choice(DIPLOMACY_WORDS)

    while (word, hint) in used:
      word, hint = random.choice(DIPLOMACY_WORDS)

    used.append((word, hint))

    letters = list(word)
    random.shuffle(letters)
    scrambled_word = "".join(letters).upper()

    print(f"\nRound {round_num}\n")
    
    print(f"\nScrambled: {scrambled_word}\n")

    guess = input("Guess the word (or type 'hint' / 'skip' / 'quit'): ").strip().lower()

    if guess == "hint":
      print(f"\nHint: {hint}\n")

      guess = input("Your guess (or 'skip' / 'quit'): ").strip().lower()

    if guess == "quit":
      print("Thanks for playing!")
      break
    elif guess == "skip":
      print(f"Skipped! The word was '{word}'.")
    elif guess == word:
      score += 1
      print("✅  Correct!")
    else:
      print(f"❌ Sorry, the word was '{word}'.")

    round_num += 1

  print(f"\nFinal score: {score}/{ROUNDS}\n")

  if score >= ROUNDS - 1:
    print("Nice! You're practically an ambassador.\n")
  elif score >= ROUNDS - 3 and score <= ROUNDS - 2: 
    print("Near perfect, just need a little more polishing.\n")
  elif score > ROUNDS - 5 and score < ROUNDS - 3:
    print("Hello, vice consul.\n")
  else: 
    print("Study up.")

while True:
  play_game()

  play_again = input("Would you like to play again (y/n)?: ")

  if play_again == 'y':
    clear_screen()
  else:
    print("\nThanks for playing!\n")
    break
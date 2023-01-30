
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
print(logo)
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = []
for _ in range(word_length):
    display += "_"
ae = "_"
while ae in display and lives > 0:
  print(stages[lives])
  guess = input("Guess a letter: ").lower()
  found = False
  if guess in display:
    print(f"Sorry, you already tried {guess}, please choose another one")
  else:
    for i in range(len(chosen_word)):
      if chosen_word[i] == guess:
          display[i] = guess
          found = True
    if not found:
      lives -= 1
      print(f"{guess}it's not in the word, you lost a life, try again.")
  print(display)
if lives == 0:
  print(stages[lives])
  print("End Game, you lose.")
else:
  print("Yon won, do like a cookie?")
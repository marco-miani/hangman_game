import random
import hangman_art
import hangman_words

#Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(hangman_words.word_list)
word_lenght = len(chosen_word)
endgame = False
lives = 6

print(hangman_art.logo)
print("")

display = []
for letter in chosen_word:
  display += "_"
print(display)

#Ask the user to guess a letter and assing their answer to a variable called guess. Make guess lowercase.
while not endgame:
  guess = input("Guess a letter: ").lower()
  print("")

  #Check if the user inputs the same letter
  if guess in display:
    print(f"You've already inputs {guess}.")

  #Check if the letter the user guessed (guess) is one of the letter in the choser_word.
  for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    print(f"You've guessed {guess}, that's not in the word. You lose a life.")
    print("")
    lives -= 1
    if lives == 0:
      endgame = True
      print("You lose!")
      print("")

  print(display)

  if "_" not in display:
    endgame = True
    print("You win!")
    print("")

  print(hangman_art.stages[lives])

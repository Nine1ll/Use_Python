import hangman_art
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(hangman_art.logo)

print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

already_guess =[]

while not end_of_game:
  
    guess = input("Guess a letter: ").lower()
    
    if guess in already_guess :
      print(f"You've already guessed {guess}")
    else : 
      already_guess+=guess
      for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
      #Check if user is wrong.
      if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            print("You lose.")
            print(hangman_art.stages[lives])
            break
          
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(hangman_art.stages[lives])
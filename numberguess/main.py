import random
import art
print(art.logo)
  
def number_compare(guess_number, answer_number, remain_attemps) :
  if guess_number > answer_number :
    if attempts !=1 :
      print("Too high.")
    return False
  elif guess_number < answer_number :
    if attempts !=1 :
      print("Too low")
    return False
  else :
    print(f"You got it! The answer was {answer_number}.")
    return True

print("Welcome to the Number Guessing Game!")
print("I'm Thinking of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 0

if difficulty == "easy" :
  attempts = 10
elif difficulty == "hard" :
  attempts = 5

answer = random.randint(1,100)

while attempts != 0 :
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = input("Make a guess: ")
  correct = number_compare(int(guess), answer, attempts)
  if not correct:
    attempts-=1
    if attempts != 0 :
      print("Guess again.")
    else : 
      print(f"You've run out of guesses, you lose. The answer was {answer}.")
  else :
    attempts = 0
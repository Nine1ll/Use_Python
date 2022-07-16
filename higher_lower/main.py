import game_data
import art
import random
from replit import clear

def choose_person() :
  index = random.randint(0,len(game_data.data)-1)
  return game_data.data[index]


def correct_answer(pA, pB):
  if pA['follower_count'] > pB['follower_count'] :
    return "a"
  else :
    return "b"
    

def correct(input, const) :
  if input == const :
    return True
  else :
    return False


score = 0

while True :
  clear()
  print(art.logo)
  print(f"You're right! Current score: {score}")
  person_A = choose_person()
  person_B = choose_person()
  
  answer = correct_answer(person_A, person_B)
  
  print(f"Compare A: {person_A['name']}, {person_A['description']}, from {person_A['country']}")
  print(art.vs)
  print(f"Compare B: {person_B['name']}, {person_B['description']}, from {person_B['country']}")
  
  input_answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  if correct(input_answer,answer) :
    score+=1
    
  else :
    clear()
    print(f"Sorry, that's wrong. Final score: {score}")
    break
  

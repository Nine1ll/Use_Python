import random
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_start = True
while game_start :
  game=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if game == "n":
    game_start = False 
    clear()
    break
  clear()
  import art
  print(art.logo)

  player_cards = []
  for i in range(2):
    cards_num = random.randint(0,12)
    player_cards.append(cards[cards_num])
  player_sum = 0
  for score in player_cards :
    player_sum+=score
  print(f"\tYour cars: {player_cards}, current score: {player_sum}")

  computer_cards = []
  for i in range(2):
    cards_num = random.randint(0,12)
    computer_cards.append(cards[cards_num])
    
  computer_sum = 0
  for score in computer_cards:
    computer_sum+=score
    
  print(f"\tComputer's first card: {computer_cards[0]}")
    
  another_card =True
  while another_card == True and player_sum < 21:
    card=input("Type 'y' to get another card, type 'n' to pass: ")
    if card == "n":
      another_card = False
    else :
      card_num = random.randint(0,12)
      player_cards.append(cards[card_num])
      player_sum+=player_cards[len(player_cards)-1]
      if player_sum > 21 and 11 in player_cards :
        player_cards.remove(11)
        player_cards.append(1)
        player_sum=sum(player_cards)
      print(f"\tYour cars: {player_cards}, current score: {player_sum}")
      print(f"\tComputer's first card: {computer_cards[0]}")

    if not player_sum >= 21:
      while computer_sum < 17 :
        card_num = random.randint(0,12)
        computer_cards.append(cards[cards_num])
        computer_sum = sum(computer_cards)
        if computer_sum > 21 and 11 in computer_cards :
          computer_cards.remove(11)
          computer_cards.append(1)
          computer_sum=sum(computer_cards)
    
  print(f"\tYour final hand: {player_cards}, final score: {player_sum}")
  print(f"\tComputer's final hand: {computer_cards}, final score: {computer_sum}")
  
  if player_sum > 21 :
    print("You went over. You lose 😭")
  elif player_sum == 21:
    print("Win with a Blackjack 😎")
  elif player_sum < 21 :
    if computer_sum >21 :
      print("Opponent went over. You win 😁")
    elif player_sum > computer_sum :
      print("You win 😁")
    elif player_sum < computer_sum :
      print("You lose 😭")
    elif computer_sum == 21 :
      print("Lose with a Blackjack 😥")
    else :
      print("Draw 😅")
  

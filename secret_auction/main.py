from replit import clear
import art

bidders = {}
existent = "yes"

print(art.logo)
print("Welcom to the secret auction program.")

while (existent != "no") :
  name = input("What is your name?: ")
  bid = input("What's your bid? (ex : $50): ")
  existent = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  bidders[name] = bid
  if existent == "yes" :
    clear()

bidder_bid = []
for bidder_name in bidders :
  bidder_bid.append(int(bidders[bidder_name][1:]))
winner_bill = max(bidder_bid)

winner = ""
for bidder_name in bidders :
  if bidders[bidder_name] == ("$"+str(winner_bill)) :
    winner = bidder_name

clear()
print(f"The winner is Jenny with a bid of {bidders[winner]}")
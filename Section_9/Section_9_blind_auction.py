from os import system
from Section_9_blind_auction_art import hammer

system("cls")
print(f"{hammer}\nWelcome to the secret auction program!")

active_bidders = True
bidders = {}

while active_bidders:
    name = input("What is your name? ")
    price = int(input("What's your bid? $"))
    bidders[name] = price
    other_bidder = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if other_bidder == "no":
        active_bidders = False
    else:
        system("cls")

highest_bid = 0
highest_bid_name = ""
for key in bidders:
    if bidders[key] > highest_bid:
        highest_bid = bidders[key]
        highest_bid_name = key

system("cls")
print(f"The winner is {highest_bid_name} with a bid of ${highest_bid}.")

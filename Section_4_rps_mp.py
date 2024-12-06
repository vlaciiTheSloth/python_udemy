#Section 4 main project - Rock Paper Scissors
import random

rock = '''
   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player_decision = int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for Scissors.\n"))
computer_decision = random.randint(0,2)

if player_decision == 0:
    print(rock)
elif player_decision == 1:
    print(paper)
elif player_decision == 2:
    print(scissors)
else:
    print("Insufficient input!")
    exit()

print("\nComputer chose:\n")

if computer_decision == 0:
    print(rock)
elif computer_decision == 1:
    print(paper)
elif computer_decision == 2:
    print(scissors)

if (player_decision == 0 and computer_decision == 0) or (player_decision == 1 and computer_decision == 1) or (player_decision == 2 and computer_decision == 2):
    outcome = "Draw"
elif (player_decision == 0 and computer_decision == 2) or (player_decision == 1 and computer_decision == 0) or (player_decision == 2 and computer_decision == 1):
    outcome = "You win!"
elif (player_decision == 0 and computer_decision == 1) or (player_decision == 1 and computer_decision == 2) or (player_decision == 2 and computer_decision == 0):
    outcome = "You lose!"

print(outcome)
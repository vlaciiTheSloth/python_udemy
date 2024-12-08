# Section 5 - Password generator
# This project has 2 difficulty levels: easy (just put letters, numbers and characters in a sequence) and hard (completely randomize)

import random

# Data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Inputs
print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# EASY difficulty
password_easy = ""

for cnt in range(0, nr_letters): # original self-made solution was range(1, nr_xxx+1), but simplified based on video to current state (which is simpler and more logical)
    if cnt <= nr_letters:
        password_easy += random.choice(letters)

for cnt in range(0, nr_symbols):
    if cnt <= nr_symbols:
        password_easy += random.choice(symbols)

for cnt in range(0, nr_numbers):
    if cnt <= nr_numbers:
        password_easy += random.choice(numbers)

print(f"Simple password: {password_easy}")

# HARD difficulty
chosen_characters = []
password_hard = ""

for cnt in range(0, nr_letters): # original self-made solution was range(1, nr_xxx+1), but simplified based on video to current state (which is simpler and more logical)
    if cnt <= nr_letters:
        chosen_characters.append(random.choice(letters))

for cnt in range(0, nr_symbols):
    if cnt <= nr_symbols:
        chosen_characters.append(random.choice(symbols))

for cnt in range(0, nr_numbers):
    if cnt <= nr_numbers:
        chosen_characters.append(random.choice(numbers))

nm_of_characters = len(chosen_characters)

for cnt in range(0, nm_of_characters):
    if len(chosen_characters) >= 0:
        random_char_index = random.randint(0, len(chosen_characters)-1)
        password_hard += chosen_characters.pop(random_char_index)

print(password_hard)

# Based on the video: random.shuffle() -> it shuffles / randomizes all elements of a list.
# So the last 'for' can be simplied by using random.shuffle(chosen_characters), then iterating over every element of that list with a 'for' and add them to a string one by one.

# random.shuffle(chosen_characters)
# for char in chosen_characters:
#     password_hard += char
# print(password_hard)
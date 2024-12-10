import random

hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for cnt in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)
game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = str(input("Take a guess! ")).lower()
    print(guess)

    display = ""

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += "_"
            lives -= 1

    print(hangman_stages[lives])
    print(display)

    if "_" not in display:
        game_over = True
        print("You win")

    if lives == 0:
        print("You lose")
        break

import random
from Section_7_hm_words import words
import Section_7_hm_art

chosen_word = random.choice(words)

print(Section_7_hm_art.hangman_ascii)

placeholder = ""
for cnt in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)
game_over = False
correct_letters = []
lives = 6

while not game_over:
    print(f"******************** {lives}/6 LIVES LEFT ********************")
    guess = str(input("Take a guess! ")).lower()
    print(guess)
    if guess in correct_letters:
        print("You've already guessed this letter: " + guess)

    display = ""

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print("You guessed " + guess + ", which is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"You lose. The word was: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("You win")


    print(Section_7_hm_art.hangman_stages[lives])
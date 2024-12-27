import random
from Section_7_hm_words import words
import Section_7_hm_art

chosen_word = random.choice(words)

print(Section_7_hm_art.hangman_ascii)

placeholder = ""
for cnt in range(0, len(chosen_word)):
    placeholder += "_"
chosen_word_len = len(chosen_word)

print(f"{placeholder} ({chosen_word_len})")
game_over = False
correct_letters = []
wrong_guesses = []
lives = 6

while not game_over:
    print(f"\n******************** {lives}/6 LIVES LEFT ********************")
    guess = str(input("Take a guess! ")).lower()

    if guess in correct_letters:
        print("You've already guessed this letter: '" + guess + "'.")
    elif len(guess) == len(chosen_word):
        if guess == chosen_word:
            print("Are you late from somewhere? Nevermind, you got the word! You won!")
            print(Section_7_hm_art.you_won)
            game_over = True
            break
        else:
            print("Don't rush this! Slow and steady wins the race ;)")
    elif len(guess) > 1:
        print("Please make a guess on one single letter.")

    display = ""

    for char in chosen_word:
        if char == guess:
            display += char
            correct_letters.append(char)
        elif char in correct_letters:
            display += char
        else:
            display += "_"

    print(f"{display} ({chosen_word_len})")

    if guess not in chosen_word:
        if guess in wrong_guesses:
            print("You've already guessed the letter '" + guess + ",' which is not in the word.")
        else:
            lives -= 1
            print("You guessed " + guess + ", which is not in the word. You lose a life.")
            if lives == 0:
                game_over = True
                print(f"You lose. The word was: {chosen_word}")
        wrong_guesses += guess
 
    if "_" not in display:
        game_over = True
        print("You win!")
        print(Section_7_hm_art.you_won)


    print(Section_7_hm_art.hangman_stages[lives])
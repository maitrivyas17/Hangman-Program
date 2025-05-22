import random


from hangaman_wordList import word_list
from hangman_art import stages
from hangman_art import logo
lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)
place_holder=""
for position in chosen_word:
    place_holder = place_holder + "_"
print(place_holder)

game_over = False
correct_letters = []

while not game_over:
    print(f"************{lives}/6 LIVES LEFT************")


    guess = input("Guess the word : ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if(letter==guess):
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life :(")
        if lives == 0:
            game_over = True
            print(f"************IT WAS {chosen_word}. You lose************")


    if "_" not in display:
        game_over=True
        print("************You win!************")

    print(stages[lives])
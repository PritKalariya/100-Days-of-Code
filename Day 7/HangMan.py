import random
from replit import clear
from hangman_words import  word_list
from hangman_art import stages, logo

print(logo)

display = []
end_of_game = False
lives = 6
chosen_word = random.choice(word_list)

#testing code
#print(f"The choosen word is: {chosen_word}")

length = len(chosen_word)
for _ in range(length):
    display += "_"


while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear() #Clear the screen after each guess

    #Formating  
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"\nYou guessed {guess}, that's no in the word. You loose a life!")

    if guess in display:
        print(f"\nYou have already guessed {guess}.")

    #Check if the letter the user guessed is one of the letters in the chosen_word.
    for position in range(length):
        letter = chosen_word[position]
        if letter in guess:
            display[position] = letter

    #Win
    if "_" not in display:
        end_of_game = True
        print("\nYou Win!")

    #loose
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou loose!")

    print(stages[lives])
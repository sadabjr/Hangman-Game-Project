#step 5             
import random

#TODO-1 : Update the word list to use the 'word_list' from hangman_words.py
#delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo, stages
print(logo)

#Testing code
#print(f'Pssst, the chosen word is {chosen_word}')

#create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter:").lower()
    
    #TODO-4: - if the user has entered a letter they have already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        #TODO-5: - if the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
            print("You Lose.")

    #join all the elements in the list and turn its into a string.
    print(f"{' '.join(display)}")

    #check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You Win.")

    #TODO-2: - Import thestaes from hangman_art.py and make this erroe go away. 
    print(stages[lives])
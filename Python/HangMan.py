import random
from words import word_list

# Function that returns words for our game
def get_word():
    word = random.choice(word_list)
    return word.upper() # Convert all user input to uppercase

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []  # Hold letter user guess
    guessed_words = []  # Hold the words user guess
    tries = 6  # How many tries the user guess for head body arms and legs

    #Print statement to help guide the user
    print("Welcome to Hangman!")
    #Print the initial state of hangman
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
     
     # While loop that runs until the word is guessed or out of tries
    while not guessed and tries > 0:
        guess = input("Enter a letter or word: ").upper()
       
        # Inside loop 3 different branches for 3 possible conditional guessing letter, word or something other than single letter or word of right length
        if len(guess) == 1 and guess.isalpha(): # Guessing a letter would mean guess has a len of 1 and only contains chars from alphabet
           # New condition block checking if letter has already been guessed or is not in the word
            if guess in guessed_letters:
                print("Letter has already been guessed:", guess)
            elif guess not in word:
                print(guess, "is not in the word")
                # Decrement tries since incorrect guess
                tries -= 1
            else:
                print("Nice job,", guess, "is in the word!")
                guessed_letters.append(guess)
                # Converting word completion from a string a list to reveal to user all occurrences of guess
                word_as_list = list(word_completion)
                # Need to find all index word guess occurs in a word using list comprehension
                indices = [i for i, letter in enumerate(word) if letter == guess]  # Calling enumerate to get both the index I and Letter at the index at each iteration
                for index in indices:
                    word_as_list[index] = guess # Using for loop to replace each underscore at index guess
                word_completion = "".join(word_as_list) # Updating word completion to convert back to string
                # Possible guess completes the word
                if "_" not in word_completion: # Checks if it completes
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha(): # Guessing a word would mean len of guess = len of word and holds only letters
            if guess in guessed_words:
                print("Word has already been guessed:", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Invalid guess.")  # Handles everything else
        # Print current state of hang/word after each guess
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats! You guessed the word! You win!!")
    else:
        print("Oh no! You ran out of tries. The word was " + word + ". Try again next time :)")

def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)  # We need to run the game once
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)
        # Making the program run as long as the user wants


if __name__ == "__main__":
    main()
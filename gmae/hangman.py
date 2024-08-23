import random

def get_random_word():
    words = ["python", "hangman", "programming", "developer", "openai", "algorithm"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    return stages[tries]

def play_hangman():
    print("Welcome to Hangman!")
    word = get_random_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    
    tries = 6
    guessed_word = ['_'] * len(word)
    
    while tries > 0 and len(word_letters) > 0:
        print(display_hangman(tries))
        print('Current word:', ' '.join(guessed_word))
        print('Used letters:', ' '.join(used_letters))
        
        guess = input("Guess a letter: ").lower()
        
        if guess in alphabet - used_letters:
            used_letters.add(guess)
            
            if guess in word_letters:
                word_letters.remove(guess)
                for index, letter in enumerate(word):
                    if letter == guess:
                        guessed_word[index] = guess
            else:
                tries -= 1
                print(f"Letter {guess} is not in the word.")
                
        elif guess in used_letters:
            print("You've already used that letter. Try again.")
        else:
            print("Invalid input. Please enter a letter.")
        
        if ''.join(guessed_word) == word:
            print(f"Congratulations! You've guessed the word: {word}")
            break
    
    if tries == 0:
        print(display_hangman(tries))
        print(f"Sorry, you ran out of tries. The word was: {word}")

# Start the game
play_hangman()

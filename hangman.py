import random

# ASCII Art for Hangman Stages         
HANGMAN_PICS = [
    """
       --------
       |      |
       |      
       |      
       |      
       |
    """,
    """
       --------
       |      |
       |      O
       |      
       |      
       |
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |
    """,
    """
       --------
       |      |
       |     😶
       |     /|\\
       |     / 
       |
    """,
    """
       --------
       |      |
       |     😨
       |     /|\\
       |     / \\
       |
    """,
    """
       --------
       |    |  
       |    |
       |    
       |   💀
       |   
    """
]

# Word list for the game
WORD_LIST = ["codealpha","python", "developer", "hangman", "programming", "challenge", "algorithm"]

def get_random_word():
    """Returns a random word from the list."""
    return random.choice(WORD_LIST).upper()

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and underscores for unguessed letters."""
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    """Runs the Hangman game."""
    word = get_random_word()
    guessed_letters = set()
    attempts = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print("\n🎮 Welcome to Hangman! Guess the word before the man is fully hanged!\n")

    while attempts < max_attempts:
        print(HANGMAN_PICS[attempts])
        print("\nWord: ", display_word(word, guessed_letters))
        print("Guessed Letters: ", " ".join(guessed_letters) if guessed_letters else "None")

        guess = input("\nEnter a letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Invalid input! Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⏳ You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print(f"❌ Incorrect! '{guess}' is not in the word.")
            attempts += 1
        else:
            print(f"✅ Good guess! '{guess}' is in the word.")

        if set(word) <= guessed_letters:
            print("\n🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print(HANGMAN_PICS[max_attempts])
        print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    play_hangman()

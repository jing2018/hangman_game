# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
    

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for w in secret_word:
        if w in letters_guessed:
            continue
        else:
            return False
   
    return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # current_word: tuple
    current_word=()
    for s in secret_word:
        if s in letters_guessed:
            current_word=current_word+(s,)
        else:
            current_word=current_word+("_ ",)
    current_word=''.join(current_word)
    return current_word
            
        



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # avai_letters:string
    avai_letters = string.ascii_lowercase
    # convert avai_letters to list
    avai_letters=list(avai_letters)
    for g in letters_guessed :
        if g in avai_letters:
            avai_letters.remove(g)  
    avai_letters=''.join(avai_letters)
    return avai_letters       
    
    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    
    guess_time=6;
    letters_guessed=""
    warn_num=3
    print("You have 3 warnings left")
    

    while  guess_time>0:
        print("------------------------------")
        if is_word_guessed(secret_word, letters_guessed):
            # word: tuple
            word=()
            for i in secret_word:
                if i not in word:
                    word=word+(i,)
            unique_letter=len(word)
            
            print("Congratulations, you won!")
            print("Your total score for this game is : ", guess_time * unique_letter)
            break
        
        print("You have ", guess_time, " guesses left"  )
        print("Availiable letters: ", get_available_letters(letters_guessed))       
        user_guess=input("Please guess a letter:")
        # If the user inputs a letter 
        # that has already been guessed, 
        # print a message telling the user 
        # the letter has already been guessed before.
        if user_guess in letters_guessed:
            if warn_num>=1:
                warn_num=warn_num-1
            else:
                guess_time = guess_time-1
            print("Oops! You've already guesses that letter. You now have ", warn_num, " warnings:", get_guessed_word(secret_word, letters_guessed))
            continue
                           
        if str.isalpha(user_guess):
            str.lower(user_guess)
            # convert string to list
            # add the new guessed letter
            letters_guessed=list(letters_guessed)
            letters_guessed.extend(user_guess)
            # convert list to string
            letters_guessed=''.join(letters_guessed)
            
            if user_guess in secret_word:
                print("Good guess: " , get_guessed_word(secret_word, letters_guessed))
            else:
                # if the letter is a vowel,
                # the user loses two guesses;
                # if it is a consonants,
                # the user loses one guess.
                if user_guess in "aeiou":
                    guess_time = guess_time-2
                else:
                    guess_time = guess_time-1
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                
        else:
            if warn_num>=1:
                warn_num=warn_num-1
                print("Oops! That is not a valid letter. You have ", warn_num, " warnings left:", get_guessed_word(secret_word, letters_guessed))
            else:
                guess_time = guess_time-1
        
    if guess_time<=0 and is_word_guessed(secret_word, letters_guessed)== False:
        print("Sorry, you ran out of guesses. The word was : ", secret_word)
    return 
                


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

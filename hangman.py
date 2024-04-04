
# Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

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
    # if the guessed word has all the letters in the secret word
    # and no underscores left, the secret word has been guessed
    return secret_word == get_guessed_word(secret_word, letters_guessed)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word_list = []
    # start with list of underscores for each letter in secret_word
    for char in secret_word:
        guessed_word_list.append("_ ")
    # see if any letter guessed is in secret_word
    for letter in letters_guessed:
        for index, i in enumerate(secret_word):
            # if letter found in secret_word, replace "_" in
            # guessed_word_list with letter at the appropriate index
            if letter == i:
                guessed_word_list[index] = letter
    # convert guessed_word_list into a string
    guessed_word_str = ''.join(guessed_word_list)
    return guessed_word_str


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # make a list of all letters of alphabet
    avail_letters = list(string.ascii_lowercase)
    # if a letter has been guessed, remove it from
    # the list of available letters
    for letter in letters_guessed:
        if letter in avail_letters:
            avail_letters.remove(letter)
    # convert list of available letters into a string
    avail_letters_str = ''.join(avail_letters)
    return avail_letters_str


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word_cleaned = my_word.replace(" ", "")
    comp_test = []
    # eliminate any words that are a different length than guessed word
    if len(my_word_cleaned) != len(other_word):
        return False
    else:
        # used zip function to group chars from both words in same position together
        # allows direct comparison
        for (char1, char2) in zip(my_word_cleaned, other_word):
            # if chars in same location match, add char to test list
            if char1 == char2:
                comp_test.append(char2)
            # if chars don't match, but char2 is not one of the letters already revealed
            # in secret word & char1 is an underscore, add "_" to test list
            elif char1 != char2:
                if char1 == "_" and char2 not in my_word_cleaned:
                    comp_test.append(char1)
    # convert test list to string
    comp_test_string = ''.join(comp_test)
    # if the test word looks the same as the guessed word,
    # the test word is a possible match for the secret word
    return comp_test_string == my_word_cleaned


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns:  every word in wordlist that matches my_word
    '''
    matched_words = []
    # iterate through list of all possible words
    for i in wordlist:
        # if the revealed letters of user's guessed word match with word in wordlist ...
        if match_with_gaps(my_word, i):
            # add that word to list of possible matches
            matched_words.append(i)
    if not matched_words:
        print("No matches found")
    else:
        # convert list of possible matches into string with
        # each word separated by a comma
        matched_words_str = ','.join(matched_words)
        return matched_words_str


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    RULES OF THE GAME:

    * At the start of the game, you will be told the length of the secret word

    * You will have 6 guesses to guess the correct word.

    * Before each round, you will see how many guesses
      you have left and the letters that you have not yet guessed.

    * You may only guess ONE letter per round.

    * If you want a hint, guess '*', and you will see all the words in wordlist that
      matches the current guessed word. You will not lose any guesses.

    * Entering an invalid guess (non-alphabetic character or previously guessed letter) will
      cost you a warning. After 3 warnings, you will lose a guess.


    '''
    secret_word_len = len(secret_word)
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {secret_word_len} letters long.")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    letters_guessed = []
    attempt = 6
    warning_count = 3
    unique_letter = 0
    # user enters new round of game as long as they have attempts left and have not guessed the secret word
    # at the beginning of each round, user sees number of guesses left, number of warnings left,
    # and all the letters they have not yet guessed
    while not is_word_guessed(secret_word, letters_guessed) and attempt > 0:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"You have {warning_count} warnings left.")
        print(f"You have {attempt} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        # prompts user to input letter guess
        guess = str.lower(input("Guess a letter: "))
        # if user asks for a hint, show_possible_matches func. is called w/
        # current guessed word passed in
        if guess == "*":
            print("The possible matches are: ")
            print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
        # if user enters invalid guess, a warning count is deducted
        elif not str.isalpha(guess) or guess in letters_guessed:
            if warning_count > 1:
                warning_count -= 1
                print(f"Okay are you even paying attention?? You only have {warning_count} warnings left now.")
            # if last warning count deducted,one attempt/guess is also deducted
            elif warning_count == 1:
                attempt -= 1
                warning_count = 0
                print(f" Nice job, you buffoon. "
                      f"You ran out of warnings. You now only have {attempt} guesses left.")
        # user enters valid guess
        elif str.isalpha(guess) and guess not in letters_guessed:
            # the guessed letter is added to the letters_guessed list
            # that letter will be removed from the string of available letters next round
            letters_guessed.append(guess)
            # if the guess is incorrect, deduct one attempt and display guessed word
            if guess not in secret_word:
                attempt -= 1
                print(f"Yikes! This letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            # if guess is correct, add 1 to unique letter count and do not deduct from attempt count
            elif guess in secret_word:
                unique_letter += 1
                # check if the user has now guessed all the letters that make up the secret word
                if not is_word_guessed(secret_word, letters_guessed):
                    # if they have not yet guessed the secret word, display guessed word
                    print(f"Good guess! {get_guessed_word(secret_word, letters_guessed)}")
                # if they guessed the secret word, the user's score is calculated and displayed
                elif is_word_guessed(secret_word, letters_guessed):
                    print(f"Congrats! You won the game. You correctly guessed that my word is {secret_word}.")
                    total_score = attempt * unique_letter
                    print(f"Your total score was {total_score}")
                    break
    # if the user used up all 6 guesses before guessing the secret word,
    # they lose the game
    if attempt == 0:
        print(f"You ran out of guesses and LOST! The correct word was {secret_word}")


if __name__ == "__main__":

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)


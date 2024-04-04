# hangman-game

## Welcome to my Hangman Game! 
  I built this game based on a problem set in MIT's "Introduction to Computer Science and Programming in Python" undergraduate course. 
  This program allows a user to guess which letters are in a **secret word**(this word is randomly selected from a word list provided in the **words.txt** file). 
  There are several rules that the user must abide by, including: 
  - The user can only guess 1 letter per round 
  - The user has 6 tries to guess all the letters in the secret word
  - If the user is stuck and needs help, they may input an asterisk('*') instead of a letter guess and they will see all the words in the word list that could be the secret 
    word based on the correctly guessed letters thus far 
  - Guessing a letter correctly or asking for a hint will NOT affect the number of guess attempts a user has left! 
  More rules are provided in the docstrings of the **hangman_with_hints** function. 

  The MIT instructors provided: 
    - code for the first 2 functions in the hangman.py file (def load_words() and def choose_word(wordlist)) 
    - **words.txt** file 
    - names and docstrings for all functions 

  Please Note: I made several modifications to the provided docstrings and chose not to include certain aspects of the pset assignment in this repository,
  such as the *'hangman'* function, as I felt it was an unncessary redundancy (it's essentially the same game as the *'hangman_with_hints'* function, but without 
  the option of asking for a hint). 

  I have provided extensive comments explaining my code, but please feel free to reach out with any questions. 
  The game is harder than you think and super fun ...... ENJOY!!! 

# Author: Brendan Ryan
# Date: September 1, 2021

import random
import os               # for relative path
# word = "PERSEVERE"
guessed = [""]
guessed_correctly = []


class Game_Word:
    def __init__(self):
        self.word = ""

class Incorrect:
    def __init__(self):
        self.incorrect_guesses = 0

def setup_guessed():
    for i in range(len(word)):
        guessed_correctly.append("_")


# Begin main functions

def user_guess():
    """ Gets user input """
    letter = input("\nGuess a letter in the mystery word\n")
    letter = letter.upper()
    check_repeats(letter)


def check_repeats(letter):
    """ Checks to see if guess is a repeat """
    if letter in guessed:                                   # consider: 'if letter in guessed'
        print("\nYou already chose this letter. Try again\n")
        main()
    check_exists(letter)


def check_exists(letter):
    """ Checks to see if the guessed letter is in the word """
    if letter in word and word.count(letter) > 1:
        print("\n\nThe word contains", word.count(letter), letter + 's')
        guessed.append(letter)
        update_array(letter)
    elif letter in word:
        print("\n\nThe word contains", word.count(letter), letter)
        guessed.append(letter)
        update_array(letter)
    else:
        print("\nThe letter you chose isn't found in the word\n")
        hangman.incorrect_guesses += 1
        guessed.append(letter)
        print("Incorrect guesses:", hangman.incorrect_guesses)              
        main()


def update_array(letter):
    for i in range(len(word)):
        if word[i] == letter:
            guessed_correctly[i] = letter
    main()
    

def display():
    print("\n")
    print("\t\t\t\t","*" * 47)
    print("\t\t\t\t*\t\t\t\t\t\t*")
    print("\t\t\t\t*\tThe mystery word has", len(word), "letters\t\t*")
    print("\t\t\t\t*\t"," ".join(guessed_correctly), "\t\t\t\t*")
    print("\t\t\t\t*\t\t\t\t\t\t*")
    print("\t\t\t\t*\tYou have previously guessed:" , " ".join(guessed), "\t\t*")
    print("\t\t\t\t","*" * 47)


def game_end_conditions():
    if hangman.incorrect_guesses == 6:
        print("You failed to find all of the letters within the alotted number of chances. Game over")
        print("\nThe word was", word)
        quit()
    #else:
    #    print("The game continues")
    if "_" not in guessed_correctly:
        print("\nCongratulations! You solved it!\n")
        quit()


def select_difficulty():
    print("\nHow challenging do you want the game to be?")
    difficulty = int(input("\n1. Easy: Words with fewer than 7 characters\n2. Moderate: Words between 7 and 12 characters\n3. Tough: Words with more than 12 characters\n"))
    if difficulty > 0 and difficulty < 4:
        return difficulty
    else:
        select_difficulty()

def word_selector():
    difficulty = select_difficulty()
    split_words = read_word_file()
    selection_list = []
    if difficulty == 1:
        for i in range(len(split_words)):
            if len(split_words[i]) <= 6:
                selection_list.append(split_words[i])
    elif difficulty == 2:
        for i in range(len(split_words)):
            if len(split_words[i]) > 6 and len(split_words[i]) < 13:
                selection_list.append(split_words[i])
    else:
        for i in range(len(split_words)):
            if len(split_words[i]) > 12:
                selection_list.append(split_words[i])
    
    for i in range(len(selection_list)):
        word = selection_list[random.randint(0, len(selection_list)-1)]
        word = word.upper()
    return word

def read_word_file():
    file_path = os.path.dirname(__file__)           # gets working directory
    vocab = os.path.join(file_path, "vocab.txt")    # joins working directory with filename
    text_file = open(vocab, "r")
    words = []
    words = text_file.read()
    text_file.close()
    split_words = words.split()
    return split_words

# need to generalize the start of the game so 'play again' functionality can work

#def play_again():
#    proceed = input("\nDo you want to play again?\n")
#    if proceed == 'Y' or proceed == 'y':



hangman = Incorrect()


def main():
    game_end_conditions()
    display()
    user_guess()

word = word_selector()
setup_guessed()         
main()

#   WARNING:    the code that follows will make you cry;
#               a safety pig is provided below for your benefit
#                         _ 
# _._ _..._ .-',     _.._(`)) 
#'-. `     '  /-._.-'    ',/ 
#   )         \            '. 
#  / _    _    |             \ 
# |  a    a    /              | 
# \   .-.                     ;   
#  '-('' ).-'       ,'       ; 
#     '-;           |      .' 
#        \           \    / 
#        | 7  .__  _.-\   \ 
#        | |  |  ``/  /`  / 
#       /,_|  |   /,_/   / 
#          /,_/      '`-' 
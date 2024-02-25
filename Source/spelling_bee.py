#!/usr/bin/env python3
"""
Author : rstorni <rstorni@localhost>
Date   : 2024-02-18
Purpose: comand line version of the NYT spelling bee game
"""

import argparse
import random
import os
import game_manager as gm


# -------------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='CL version of NYT Spelling Bee',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        type=int,
                        metavar='random seed',
                        help='seed for letter generation',
                        default=None)

    parser.add_argument('-df',
                        '--dictionary_file',
                        help='file containing a dictionary of words',
                        metavar='FILE',
                        type=argparse.FileType('r'),
                        default='dictionary.txt')

    return parser.parse_args()


# -------------------------------------------------------
def main():
    """Main function where all logic will be executed"""

    # Gets Arguments and Establishes Random Seed
    args = get_args()
    random.seed(args.seed)
    DICTIONARY = [line.rstrip() for line in args.dictionary_file]

    sm = gm.Manager(DICTIONARY)

    while len(sm.get_words()) < 10:
        sm = gm.Manager(DICTIONARY)

    # ------------------------ starting Prompt --------------------------
    os.system('cls||clear')
    print('Welcome to the comand line version of Spelling Bee!')
    print("Create as many words as you can with the following set of letters:")
    print(f'{sm.get_letters()}')
    print(f'Please note that all created words must contain the letter "{sm.get_key_letter()}"')
    input('Press any key to continue: ...')
    os.system('cls||clear')

    # ------------------------ Game loop --------------------------------
    while sm.get_playing():
        # For Debug
        # print(sm.get_words())
        # print(max_score)

        sm.describe()
        guessed_word = input("Enter a word: ").rstrip().lower()

        if sm.is_word_valid(guessed_word):
            sm.get_correct_words().append(guessed_word)
            sm.update_score(guessed_word)
            print(f'Congrats, "{guessed_word}" Got You {sm.word_score(guessed_word)} Points!')
        else:
            print(f'"{guessed_word}" Is not a valid word, try again.')

        playing = input('Type "QUIT" to stop playing or hit any key to continue: ...\n').lower().rstrip()
        if playing == 'quit':
            break
        else:
            os.system('cls||clear')

        if sm.is_game_over():
            print("You created all possible words!")
            print(f'Correct Words: {sm.get_correct_words()}')
            print(f'Player Score: {sm.get_score()}')
            print(f'all words created: {sm.get_words()}')

    print('Thank you for playing')


# --------------------------------------------------
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Author : rstorni <rstorni@localhost>
Date   : 2024-02-18
Purpose: class to manage game state for CL NYT Spellingbee
"""
import random
import string
import math
import re
import pickle

class Manager:
    """ Manages game state for spelling_bee.py """

    # Constants
    NUMBER_OF_LETTERS = 7
    MIN_NUM_CONSONANTS = 3
    MAX_NUM_CONSONANTS = 6

    # ------------------------------------------------------
    def __init__(self, dictionary):
        """ constructor for the manager class """
        self.consonants = random.choice(range(self.MIN_NUM_CONSONANTS, self.MAX_NUM_CONSONANTS))
        self.num_vowels = self.NUMBER_OF_LETTERS - self.consonants

        self.letters = self.rand_letters(self.consonants, self.num_vowels)
        self.key_letter = random.choice(self.letters)
        self.words = self.possible_words(self.letters, self.key_letter, dictionary)
        self.max_score = sum([self.word_score(w) for w in self.words])
        
        self.playing = True
        self.correct_words = []
        self.score = 0

    # ------------------------------------------------------
    def get_playing(self):
        """"""
        return self.playing


    # ------------------------------------------------------
    def get_letters(self):
        """"""
        return self.letters


    # ------------------------------------------------------
    def get_key_letter(self):
        """"""
        return self.key_letter


    # ------------------------------------------------------
    def get_words(self):
        """"""
        return self.words
    

    # ------------------------------------------------------
    def get_correct_words(self):
        """"""
        return self.correct_words
    

    # ------------------------------------------------------
    def get_max_score(self):
        return self.max_score
    

    # ------------------------------------------------------
    def get_score(self):
        return self.score


    # ------------------------------------------------------
    def set_playing(self, value):
        self.playing = value
        

    # ------------------------------------------------------
    def set_words(self, list_of_words):
        self.words = list_of_words


    # ------------------------------------------------------
    def set_score(self, score):
        self.score = score


    # -------------------------------------------------------
    def rand_letters(self, num_consonants, num_vowels):
        """generates a random set of letters including consonants and vowels"""
        vowels = list('aeiou')
        consonants = [c for c in string.ascii_lowercase if c not in vowels]
        random_consonants = random.sample(vowels, num_vowels)
        random_vowels = random.sample(consonants, num_consonants)
        letters = random_consonants + random_vowels
        random.shuffle(letters)

        return letters

    # -------------------------------------------------------
    def possible_words(self, letter_set, key_letter, dictionary):
        """
        Takes a letter set and a key letter and returns the
        a list of words that can be created
        """

        letter_set_str = "".join(letter_set)
        # any word that contains a
        # combination of the key letter and
        # letters from the set where len>3
        pattern = re.compile(f'[{letter_set_str}]*{key_letter}[{letter_set_str}]*')


        words = []
        for line in dictionary:
            match = pattern.match(line)
            if len(line) >= 4 and match and match.end() == len(line):
                words.append(line)

        sorted(words)
        return words

    # -------------------------------------------------------
    def word_score(self, word):
        """Calculates the score of a given word"""
        LEN_4_SCORE = 1

        word_length = len(word)
        score = 0
        if word_length == 4:
            score += LEN_4_SCORE
        elif word_length >= 5:
            score += word_length

        return score
    

    # ------------------------------------------------------
    def is_game_over(self):
        if len(self.correct_words) == len(self.words):
            self.playing = False
        return not self.playing
    

    # ------------------------------------------------------
    def is_word_valid(self, word):
        return (word in self.words) and (word not in self.correct_words)
    

    # ------------------------------------------------------
    def save(self, savefile):
        pickle_out = open(f'../save_states/{savefile}.pickle', 'wb')
        pickle.dump(self, pickle_out)
        pickle_out.close()


    # ------------------------------------------------------
    def load(self, savefile):
        pickle_in = open(f'../save_states/{savefile}.pickle', 'rb')
        example = pickle.load(pickle_in)
        
        self.consonants = example.consonants
        self.num_vowels = example.num_vowels

        self.letters = example.letters
        self.key_letter = example.key_letter
        self.words = example.words
        self.max_score = example.max_score
        
        self.playing = True
        self.correct_words = example.correct_words
        self.score = example.score


    # ------------------------------------------------------
    def update_score(self,word):
        self.score += self.word_score(word)


    # ------------------------------------------------------
    def fancy_letter(self, letter):
        print("*   ___   ")
        print("*  /   \  ")
        print(f"*  | {letter} |  ")
        print("*  \   /  ")
        print("*   ---   ")


    # ------------------------------------------------------
    def describe(self, debug=False):
        """Test Function"""
        if debug:
            print(f'all possible words: {self.words}')

        print('SPELLING BEE')
        print("*"*100)
        print(f'*   list of letters: {self.letters}')
        print(f'*   key letter: {self.key_letter}')
        print(f'*   maximum score: {self.max_score}')  
        print(f'*   Score: {self.score}')
        print(f'*   Percentage: {math.floor((self.score / self.max_score) * 100)}%')
        print(f'*   List of discovered words: {self.correct_words}')
        print("*"*100)

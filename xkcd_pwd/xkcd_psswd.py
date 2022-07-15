#!/bin/env python3
import os as OS
import argparse as ARGPARSE
import secrets as SECRET
import random as RANDOM
import math as MATH
import parser as PARSER

WORDS = PARSER.Words()

class PasswordItem:
    def new(self):
        pass
    def entropy(self):
        pass
    def add_to_pool(self, elements):
        pass
    def del_from_pool(self, elements):
        pass

'''
This class will represent a Randomly chosen word of a specific length.
Word will be chosen from the list of corresponding word sizes and 
random choice entropy will be calculated thereafter.
'''
class RandomWord(PasswordItem):
    '''
    Constructor takes the range of word lengths that we want to use for password
    '''
    def __init__(self):
        pass
    def entropy(self):
        pass
    def add_to_pool(self, elements):
        pass
    def del_from_pool(self, elements):
        pass


'''
This class will represent a Randomly chosen word of a specific length.
Word will be chosen from the list of corresponding word sizes and 
random choice entropy will be calculated thereafter.
'''
class RandomWord(PasswordItem):
    '''
    Constructor takes the range of word lengths that we want to use for password
    '''
    def __init__(self, langs=PARSER.LANGUAGES, min_len = 4, max_len = 10):
        self.__update = False
        self.__min_len, self.__max_len = min_len, max_len
        if isinstance(langs,str):
            langs = [ langs ]
        self.__langs, self.__word_list = set(langs), list()
        self.__entropy, self.__options_total, self.__entropy = 0, 0, 0
        self.__secret = SECRET.SystemRandom()
        self.__update = True
        self.update_list()
    
    def new(self):
        if self.__min_len < 4 or self.__max_len > 10:
            print("Using default min[4] and max[10]", file=sys.stderr)
            set_min_len(4)
            set_max_len(10)

        self.update_list()
        i = self.__secret.randint(0,self.__options_total)
        if self.__secret.randint(0,1) == 1:
            return self.__word_list[i].lower()
        else:
            return self.__word_list[i].upper()
    
    def get_entropy(self):
        return self.__entropy

    def add_to_pool(self, lang):
        self.__update = True
        self.__langs.add(lang)
        pass

    def del_from_pool(self, lang):
        self.__update = True
        if lang in self.__langs:
            self.__langs.remove(lang)
        pass

    def set_min_len(self, i):
        self.__update = True
        self.__min_len = i
        pass

    def update_list(self):
        if self.__update:
            self.__word_list = WORDS.compile_words(self.__langs, self.__min_len, self.__max_len)
            self.__options_total= len(self.__word_list)
            self.__entropy = MATH.log(self.__options_total*2,2)
            self.__update = False

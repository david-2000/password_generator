#!/bin/env python3
import os as OS
import argparse as ARGPARSE
import secrets as SECRET
import random as RANDOM
import math as MATH
import parser as PARSER

WORDS = PARSER.Words()

def get_number(EXPLICIT=False):
    return SECRET.SystemRandom().randint(0,10)

'''
This class will represent a Randomly chosen word of a specific length.
Word will be chosen from the list of corresponding word sizes and 
random choice entropy will be calculated thereafter.
'''
class RandomWord:
    '''
    Constructor takes the range of word lengths that we want to use for password
    '''
    def __init__(self, langs=PARSER.LANGUAGES, min_len = 4, max_len = 10):
        self.__update = False
        self.__min_len = min_len
        self.__max_len = max_len
        self.__langs = langs
        self.__word_set = parser.
        self.__entropy = 0
        self.__options_total = 0
        self.__secret = SECRET.SystemRandom()
        if parser == None:
            parser = PARSER.Words()
        for (fn, wl, fl) in self.__options:
            try:
                wl_int = int(wl)
                fl_int = int(fl)
            except ValueError:
                print(f"ERROR: Cannot convert to int: (wl:{wl}|fl:{fl})", file=sys.stderr)
                continue
            if wl_int >= self.__min_len and wl_int <= self.__max_len:
                with open(f'../docs/{fn}', 'r') as f:
                    self.__word_list.extend([i.strip() for i in f.readlines()])
                    self.__options_total += fl_int
        assert(self.__options_total == len(self.__word_list))
        self.__entropy = MATH.log(self.__options_total*2,2)
    
    def get_random(self, lang='all', min_l=4, max_l=):
        i = self.__secret.randint(0,self.__options_total)
        if self.__secret.randint(0,2) % 2== 1:
            return self.__word_list[i].lower()
        else:
            return self.__word_list[i].upper()
    
    def get_entropy(self):
        return self.__entropy
    def add_lang(self, lang):
        pass
    def del_lang(self, lang):
        pass
    def set_min_len(self, i):
        pass
    def set_max_len(self, i):
        pass
    def update_list(self):
        if self.__update:
            word_list = WORDS.compile_words(self.)
        pass


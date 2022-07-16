#!/bin/env python3
import os as OS
import argparse as ARGPARSE
import secrets as SECRET
import random as RANDOM
import math as MATH
import parser as PARSER

WORDS = PARSER.Words()

'''
Super-Class for all things that can be elements of a password.
'''
class PasswordItem:
    def __init__(self):
        self.__pool_items = set([i for i in range(10)])
        self.__cases = 1
        self.__secret = SECRET.SystemRandom()
        self.__entropy = 0

    def get_new(self):
        pass
    def entropy(self):
        pass
    def add_to_pool(self, elements):
        pass
    def del_from_pool(self, elements):
        pass

    def update_entropy(self):
        self.__entropy = MATH.log(len(self.__pool_items)*self.__cases,2)

    def get_entropy(self):
        return self.entropy

'''
This class will represent a Randomly chosen number 
'''
class RandomNumber(PasswordItem):
    '''
    Constructor takes the range of word lengths that we want to use for password
    '''
    def __init__(self):
        super().__init__()

    def get_new(self):
        return 

    def entropy(self):
        return math.log(len(self.__pool_items),2)

    def add_to_pool(self, elements):
        if isinstance(elements,(int,float)):
            self.__pool_items.add(elements)
        elif isinstance(elements, (list,set,iter)):
            for i in elements:
                self.__pool_items.add(i)
        else:
            pass

    def del_from_pool(self, elements):
        if isinstance(elements,(int,float)) and elements in self.__pool_items:
            self.__pool_items.remove(elements)
        elif isinstance(elements, (list,set,iter)):
            for i in elements:
                self.__pool_items.add(i)
        else:
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
        super().__init__()
        self.__min_len, self.__max_len = min_len, max_len
        if isinstance(langs,str):
            langs = [ langs ]
        self.__langs = set(langs)
        self.__cap_strategies = []
        self.__cap_strategies.append(lambda w: w.upper())
        self.__cap_strategies.append(lambda w: w.lower())
        self.__cap_strategies.append(lambda w: w[0].lower()+w[1:-1].upper()+w[-1].lower())
        self.__cap_strategies.append(lambda w: w[0].upper()+w[1:-1].lower()+w[-1].upper())
        self.update()

    
    def get_new(self):
        if self.__min_len < 4 or self.__max_len > 10:
            print("Using default min[4] and max[10]", file=sys.stderr)
            set_min_len(4)
            set_max_len(10)

        i = self.__secret.randint(0,self.__options_total)
        f = self.__secret.randint(0,len(self.__cap_strategies))
        return self.__cap_strategies[f](self.__pool_items[i])
    

    def add_to_pool(self, lang):
        self.__langs.add(lang)
        self.update()

    def del_from_pool(self, lang):
        if lang in self.__langs:
            self.__langs.remove(lang)
            self.update()

    def set_min_len(self, i):
        self.__min_len = i
        self.update()

    def set_max_len(self, i):
        self.__max_len = i
        self.update()

    def update(self):
        self.__pool_items = WORDS.compile_words(self.__langs, self.__min_len, self.__max_len)
        self.__options_total= len(self.__pool_items)
        self.__cases = len(self.__cap_strategies)
        self.update_entropy()

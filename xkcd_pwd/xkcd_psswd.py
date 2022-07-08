#!/bin/env python3
import os as OS
import argparse as ARGPARSE
import secrets as SECRET
import random as RANDOM
import math as MATH

def main():
    arr=[]
    f = open('../docs/full','r')
    FULL = f.readlines()
    f.close()
    for f in OS.listdir('../docs/'):
        if f[0] == 'L':
            ff = open(f"../docs/{f}", 'r')
            fl = ff.readlines()
            ff.close()
            arr.append((len(fl),fl))
    t = 0
    for s,f in arr:
        t += s
    print('File\t# Words\tPercent of Total')
    i=4
    for s,f in arr:
        p = s/t
        print(f'{i}\t{s}\t{p}')
        i += 1


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
    def __init__(self, min_len=4, max_len=9):
        with open("../docs/stats","r") as stats:
            self.__options = [ i.strip().split(',') for i in stats.readlines()[1:] ]
        self.__min_len = min_len
        self.__max_len = max_len
        self.__word_list = []
        self.__entropy = 0
        self.__options_total = 0
        self.__secret = SECRET.SystemRandom()
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
    
    def get_random(self):
        i = self.__secret.randint(0,self.__options_total)
        if self.__secret.randint(0,2) % 2== 1:
            return self.__word_list[i].lower()
        else:
            return self.__word_list[i].upper()
    
    def get_entropy(self):
        return self.__entropy





if __name__ == '__main__':
    main()

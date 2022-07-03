from math import log

## Number of words in dictionary
es_word_set = 126000
en_word_set = 40000
word_set = es_word_set + en_word_set

## Capitalization cases
# 1 -> all caps    2-> all lowercase    3-> Only first letter Cap   4-> FirsT and last CaP
word_set *= 4

num_set = 8 ## Only ten possible digits in number set  minus {0,1} since they can be confusting

sym_alph = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}' ,'[', ']', ':', ';' ,',', '<', '>', '.', '?']
sym_set = len(sym_alph) ## Assume only above symbols are available

## Define how many of each you want in password
num_words = 3
num_numbers = 2
num_symbols = 2

## Calculate entropy:
#Individually
word_entropy = num_words * log(word_set,2)
num_entropy = num_numbers * log(num_set,2)
symbol_entropy = num_symbols * log(sym_set,2)
print("Total entropy is " + str(word_entropy + num_entropy + symbol_entropy));

print("--\nEntropy for old-fashioned password")
charset = 26 * 2
charset += 10 # digits
charset += 10 # symbols
print("Regular entropy is " + str(8* log(charset,2)));

print("--\nEntropy for mixed password")
num_words=3
num_numbers=1
num_symbols=1
num_chars=3
char_set = 26 *2
word_entropy = num_words * log(word_set,2)
num_entropy = num_numbers * log(num_set,2)
symbol_entropy = num_symbols * log(sym_set,2)
char_entropy = num_chars * log(char_set,2)
print("Mixed entropy is " + str(word_entropy+num_entropy+symbol_entropy+char_entropy));

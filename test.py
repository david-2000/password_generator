from math import log

## Number of words in dictionary
word_set = 15000
word_set *= 2 ## Multiply *2 to account for lower and upper case uptions
word_set *= 2 ## Multiply by however many languages you are translating words to

num_set = 10 ## Only ten possible digits in number set

sym_alph = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}' ,'[', ']', ':', ';' ,',', '<', '>', '.', '?']
sym_set = len(sym_alph) ## Assume only above symbols are available

## Define how many of each you want in password
num_words = 4
num_numbers = 3
num_symbols = 1

## Calculate entropy:
#Individually
word_entropy = num_words * log(word_set,2)
num_entropy = num_numbers * log(num_set,2)
symbol_entropy = num_symbols * log(sym_set,2)
print("Total entropy is " + str(word_entropy + num_entropy + symbol_entropy));
#Collectively
C = (word_set ** num_words) * (num_set ** num_numbers) * (sym_set ** num_symbols)
print("Total entropy is " + str(log(C,2)));

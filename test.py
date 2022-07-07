from math import log

def arr_to_str(arr):
    for i,x in enumerate(arr):
        if i%5 == 0:
            print("\n\t"+str(x), end='')
        else:
            print("\t"+str(x), end='')
    print()

def ent(L,C):
    return L * log(C,2)

## Number of words in dictionary
es_word_set = 83000
en_word_set = 50000
word_set = es_word_set + en_word_set
#word_set = 50000

## Capitalization cases
# 1 -> all caps    2-> all lowercase    3-> Only First Letter Cap   4-> oNLY fIRST lETTER lOW
word_set *= 2

## ALl letters lower and upper case
char_set = 26 *2

n_set = 8 ## Only ten possible digits in number set  minus {0,1} since they can be confusting

sym_alph = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '}' ,'[', ']', ':', ';' ,',', '<', '>', '.', '?']
sym_set = len(sym_alph) ## Assume only above syms are available

rand_set = char_set + sym_set


## Calculate entropy:
#Individually
print("Legend: Meaning\nW: Random word from word dictionary (en|es|EN|ES)")
print("S: Random symbol from set:")
arr_to_str(sym_alph)
print("N: Random number between 2-9")
print("C: Random character between a-z and A-Z")
print("R: Random character between a-z, A-Z, 0-9, {10 UNIQ syms}")
print("---\tFor all of the above the succeeding number represents uniqeuness.")
print("\ti.e. N1 == N1 & N2 != N1 & N2 != C1 & C1 == C1 & C1 != C2 ...etc...")
print("\n")

print("\n--\bBaseline entropies:")
print(f"\tW: {ent(1,word_set)}") 
print(f"\tN: {ent(1,n_set)}") 
print(f"\tS: {ent(1,sym_set)}") 
print(f"\tC: {ent(1,char_set)}") 
print(f"\tR: {ent(1,rand_set)}") 
print(f"\tN|S: {ent(1,n_set+sym_set)}") 


## Define how many of each you want in password
n_words, n_nums, n_syms = 3, 2, 2
word_ent, n_ent, symbol_ent = ent(n_words,word_set), ent(n_nums, n_set), ent(n_syms, n_set)
form=f"W: {n_words}\tN: {n_nums}\tS: {n_syms}"
print(f"Entropy for a password: [{form}]")
print("\t" + str(word_ent + n_ent + symbol_ent));

charset = 26 * 2
charset += 10 # digits
charset += 10 # syms
n_chars = 4
form=f"R: {n_chars}"
print(f"Entropy for a password: [{form}]")
print("\t" + str(n_chars* log(charset,2)));


charset = 26 * 2
n_chars = 4
form=f"C: {n_chars}"
print(f"Entropy for a password: [{form}]")
print("\t" + str(n_chars* log(charset,2)));

n_words, n_nums, n_syms, n_chars = 3, 2, 2, 3
word_ent, n_ent = ent(n_words, word_set), ent(n_nums, n_set)
symbol_ent, char_ent = ent(n_syms, sym_set), ent(n_chars, char_set)
form=f"W: {n_words}\tN: {n_nums}\tS: {n_syms}\tC: {n_chars}"
print(f"Entropy for a password: [{form}]")
print("\t" + str(word_ent+n_ent+symbol_ent+char_ent));


n_words, n_nums, n_syms, n_chars = 4, 1, 1, 2
word_ent, n_ent = ent(n_words, word_set), ent(n_nums, n_set)
symbol_ent, char_ent = ent(n_syms, sym_set), ent(n_chars, char_set)
form=f"W: {n_words}\tN: {n_nums}\tS: {n_syms}\tC: {n_chars}"
print(f"Entropy for a password: [{form}]")
print("\t" + str(word_ent+n_ent+symbol_ent+char_ent));

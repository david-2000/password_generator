#!/bin/env python3
import os as OS
impory sys as SYS

LANGUAGES = OS.listdir('../docs')

def categorize(use_langs):
    word_sets = {}
    for lang in use_langs:
        if lang not in LANGUAGES:
            print(f'Dictionary for {lang} is not available. Skipping...', file=SYS.stderr)
            continue
        with open(f"{lang}/full") as lang_file:
            for word in lang_file.readlines():
                word_clean = cleanup_word(word)
                word_len = len(word_clean)
                if word_len not in word_sets:
                    word_sets[word_len] = set()
                word_sets[word_len].add(word_clean)
    return word_sets


def cleanup_word(word):
    word = word.lower().strip()
    word = word.replace('\u00e1', 'a') # Unicode for accented a [á]
    word = word.replace('\u00e9', 'e') # Unicode for accented e [é]
    word = word.replace('\u00ed', 'i') # Unicode for accented i [í]
    word = word.replace('\u00f3', 'o') # Unicode for accented o [ó]
    word = word.replace('\u00fa', 'u') # Unicode for accented u [ú]
    word = word.replace('\u00fc', 'u') # Unicode for umlaut-u [ü]
    word = word.replace('\u00f1', 'n') # Unicode for tilded-n [ñ]
    return word

if __name__ == '__main__':
    main()

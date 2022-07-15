#!/bin/env python3
import os as OS
import sys as SYS
import parser as PARSER

LANGUAGES = set(OS.listdir('../docs'))

class Words:
    def __init__(self, use_langs=LANGUAGES):
        self.langs = set()
        self.l_range = (4,10)
        self.word_sets = {}
        if isinstance(use_langs, str):
            use_langs = [ use_langs ]
        self.word_sets = {}
        for lang in use_langs:
            if lang not in LANGUAGES:
                print(f'Dictionary for {lang} is not available. Skipping...', file=SYS.stderr)
                continue
            self.langs.add(lang)
            with open(f"../docs/{lang}") as lang_file:
                for word in lang_file.readlines():
                    word_clean = word.strip().lower()
                    word_len = len(word_clean)
                    if (lang,word_len) not in self.word_sets:
                        self.word_sets[(lang, word_len)] = set()
                    self.word_sets[(lang,word_len)].add(word_clean)
    
    def compile_words(self, lang=None , min_len=4, max_len=10):
        if lang == None:
            lang = self.langs
        min_len = 4 if min_len < 4 else min_len
        max_len = 10 if max_len > 10 else max_len
        compiled_list = []
        if isinstance(lang,str):
            lang = set([lang])
        for i in lang:
            if i not in self.langs:
                continue
            for j in range(min_len, max_len+1):
                if j < self.l_range[0] or j > self.l_range[1]:
                    continue
                compiled_list.extend(self.word_sets[(i,j)])
        return compiled_list


WORDS = PARSER.Words()

#!/bin/env python3
import os as OS

def main():
    arr=[]
    for f in OS.listdir('../docs/'):
        if f[0] == 'L':
            with open(f"../docs/{f}", 'r') as word:
                arr.append((f,word.readlines()))
    out = 'filename,word_length,file_length'
    for (fn,fl) in arr:
        out += f"\n{fn},{len(fl[0])-1},{len(fl)}"
    print(out)
    with open("../docs/stats",  "w") as of:
        of.write(out)




if __name__ == '__main__':
    main()

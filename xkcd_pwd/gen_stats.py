#!/bin/env python3
import os
import argparse

def main():
    arr = []
    for f in os.listdir(""):
        if f[0] == 'L':
            arr.append((f,len(f.readlines()))
    t = 0
    for f,s in arr:
        t+=s
    print("File\t# Words\tPercent of Total")
    for f,s in arr:
        p = s/t
        print(f"{f}\t{s}\t{p}")


if __name__ == "__main__":
    main()

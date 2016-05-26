#!/usr/bin/python
# this script seperate genbank file
# usage: python separate_genbank_file.py input

import sys

def main():
    fread = open(sys.argv[1],'r')
    for line in fread:
        if (line[:5] == 'LOCUS'):
            print line.split(' ')[7]
        else:
            continue

if __name__ == '__main__':
    main()

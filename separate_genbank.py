#!/usr/bin/python
# this script seperate genbank file
# usage: python separate_genbank_file.py input

import sys
def write_file(cont):
    print cont[0]
    filename = cont[0].split(" ")[7]+".gbk"
    fwrite = open(filename,'w')
    for line in cont:
        fwrite.write(line)
    fwrite.close()

def main():
    cont = []
    fread = open(sys.argv[1],'r')
    for line in fread:
        if (line[:2] == '//'):
            cont.append(line)
            write_file(cont)
            cont = []
        else:
            cont.append(line)

if __name__ == '__main__':
    main()

#!/usr/bin/python

#this script generate list of rast id from refsoil database file
#example: python refsoil_to_rastid.py refsoil.unix.txt > refsoil.rast.id

import sys

for n, line in enumerate(open(sys.argv[1],'r')):
    if n == 0:
        continue
    spl = line.strip().split('\t')
    rastids = spl[11]
    if rastids.startswith('"') and rastids.endswith('"'):
        rastids = rastids[1:-1]
    rastspl = rastids.split(',')
    for x in rastspl:
        print x

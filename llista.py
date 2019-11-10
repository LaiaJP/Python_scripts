#!python

import sys

# Iteration over all arguments:
sys.argv.remove('proba.py')
for eachArg in sys.argv:   
        eachArg_list = []
        with open(eachArg, 'r') as infile:
            for line in infile:
                eachArg_list.extend(line.strip().split(' '))
            #eachArg_list.pop(0)
            #eachArg_list.pop(-1)
            print(eachArg,'=',eachArg_list)

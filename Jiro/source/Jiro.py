#!/usr/bin/env python3

#       _ _
#      | (_)_ __ ___
#   _  | | | '__/ _ \
#  | |_| | | | | (_) |
#   \___/|_|_|  \___/



import sys

import JRParser
import Utils

args = sys.argv
invokeName = args.pop(0)
verbose = False

# print("Passed arguments: " + Utils.listtostring(args))

if args.__len__() == 0:
    Utils.jr_help(invokeName)
else:
    if '-h' in args:
        Utils.jr_init()
        Utils.jr_help(invokeName)
    else:
        if '-v' in args:
            Utils.jr_init()
            verbose = True
            print(args)
            args.remove('-v')
            print(args)
        p = JRParser.Parser(verbose)
        p.parse(open(args[0]).readlines(), True)

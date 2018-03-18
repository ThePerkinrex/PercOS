#!/usr/bin/env python3

#   ____               ____            _       _
#  |  _ \ ___ _ __ ___/ ___|  ___ _ __(_)_ __ | |_
#  | |_) / _ \ '__/ __\___ \ / __| '__| | '_ \| __|
#  |  __/  __/ | | (__ ___) | (__| |  | | |_) | |_
#  |_|   \___|_|  \___|____/ \___|_|  |_| .__/ \__|
#                                       |_|

import sys

import PSParser
import Utils

args = sys.argv
invokeName = args.pop(0)
verbose = False

# print("Passed arguments: " + Utils.listtostring(args))

if args.__len__() == 0:
    Utils.ps_help(invokeName)
else:
    if '-h' in args:
        Utils.psinit()
        Utils.ps_help(invokeName)
    else:
        if '-v' in args:
            Utils.psinit()
            verbose = True
            print(args)
            args.remove('-v')
            print(args)
        p = PSParser.Parser(verbose)
        p.parse(open(args[0]).readlines(), True)

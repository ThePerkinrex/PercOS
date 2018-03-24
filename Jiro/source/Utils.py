import re
import Tokens


var_id = '^[A-Za-z_]\w*$'
var_id_mid = '[A-Za-z_]\w*'

class LogColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    RESPONSE = '\033[1;36m'
    LANG = '\033[1;34m'
    WARNING = '\033[93m'  # WARNINGS
    FAIL = '\033[91m'  # ERRORS & END
    SETUP = '\033[32m'  # SETUP
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def jr_init():
    print(LogColors.SETUP + "\n\n #### - WELCOME TO - ####")
    print(" #                      #")
    print(" #       _ _            #")
    print(" #      | (_)_ __ ___   #")
    print(" #   _  | | | '__/ _ \  #")
    print(" #  | |_| | | | | (_) | #")
    print(" #   \___/|_|_|  \___/  #")
    print(" #                      #")
    print(" ########################\n\n" + LogColors.ENDC)

def listtostring(mylist):
    r = "["
    for item in mylist:
        r = r + item + ","
    r = r.rstrip(",") + "]"
    return r

def print_script(printfunc, verbose, script):
    for i in range(len(script)):
        line = script[i]
        printfunc(verbose, str(i) + ':\t', line.strip('\n'))


def jr_help(invokeName):
    print("------------| Jiro Help |------------")
    print(invokeName + " <filepath> -> run the Jiro file in <filepath>")
    print(invokeName + " -> print this help message")
    print(invokeName + " -h -> print this help message")
    print("\n\n")


def error(name, text, line):
    print(LogColors.FAIL + "\n----------- ERROR -----------\n" + name)
    print("in " + text)
    print("line " + str(line) + LogColors.ENDC)
    quit(1)

def log(verbose, *text):
    if verbose:
        r = ''
        for t in text:
            r += str(t) + ' '
        print(r)


def call_native(name, args):
    # print("Native func " + name + " getting called with args " + str(args))
    if name == 'print':
        print(args[0])


def replace_regex(base: str, regex: str, replacing: str):
    m = re.search(regex, base)
    if m:
        return base.replace(m.group(0), replacing)
    return None


def val_to_jr(val):
    if type(val) == str:
        return str('"' + val + '"')
    elif type(val) == float:
        return str(val)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def tokenize(s: str, text, line, localvar, localval, parser=None):
    t = None
    s = s.strip()
    # print(s)
    verbose = False
    if parser:
        verbose = parser.verbose
    log(verbose, localvar, localval)
    if True:
        m = re.search(var_id_mid, s)
        # print(m)
        if m:
            # print(m.group(0))
            if parser and m.group(0) in parser.variables:
                s = s.replace(m.group(0), val_to_jr(parser.getval(m.group(0))))

            if m.group(0) in localvar:
                val = localval[localvar.index(m.group(0))]
                log(verbose, m.group(0), localvar, val)
                s = s.replace(m.group(0), val_to_jr(val))
    log(verbose, 'TOKEN:', s)
    for token in Tokens.valid_token_literals:
        m = re.search('^' + token[0] + '$', s)
        if m:
            if ' ' in m.groups():
                error(str(s) + ' is not a valid token', text, line)
            l = list(m.groups())
            #print(l)
            t = token[1](l, text, line, localvar, localval)
            #print(t)
            break
    if t is None:
        error(str(s) + ' is not a valid token', text, line)
    return t

def create_dict(keys, values):
    r = {}
    if len(keys) != len(values):
        raise ValueError("Keys and Values have to be the same lenght")
    i = 0
    while i < keys:
        r[keys[i]] = values[i]
        i += 1
    return r

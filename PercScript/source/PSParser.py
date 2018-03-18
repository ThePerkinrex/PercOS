# PercScript Parser V1.1.0-alpha
import re

import Utils
from Utils import log
from Utils import error
from Utils import var_id

import Tokens


class Parser:
    V = "1.1.0-alpha"

    functions = [("print", 1)]  # Function names and nº of args
    arguments = [['toPrint']]  # Function arguments names
    codes = [("perc.lang.print", -1, -1)]  # Function codes and location in file
    variables = ["plang"] # Variable names
    values = ["PercScript for Perk!"]  # Variable values
    script = []  # The script to run

    def __init__(self, verbose):
        self.verbose = verbose
        log(self.verbose, "PercScript Parser V" + self.V + "\n\n\n")

# V ----FUNCTIONS---- V

    def get_args(self, name, args):  # Get a function's arguments
        return self.arguments[self.functions.index((name, len(args)))]

    def register_functions(self, toRegister):  # Find the functions and their code
        blocks = []
        finding_end = False
        start = None
        #for line in toRegister:
        for i in range(len(toRegister)):
            line = toRegister[i]
            m = re.search('func\s+(\w+)\s*\((.*?)\)\s*{', line)
            if m:
                if finding_end:
                    error("Cannot declare a function inside another function", self.script[i], i + 1)
                start = i
                finding_end = True
                blocks.append(m.group(0).rstrip('{'))
                continue
            m = re.search('(.*?){', line)
            if m:
                blocks.append(m.groups(0)[0])
                continue
            m = re.search('}', line)
            if m:
                popped = blocks.pop(len(blocks)-1)
                log(self.verbose, "FUNC REGISTRATION: End for " + popped + " found")
                if len(blocks) == 0:
                    finding_end = False
                    m = re.search('func\s+(\w+)\s*\((.*?)\)\s*', popped)
                    if m:
                        arg_str = m.groups(0)[1]
                        args = re.split('\s*,\s*', arg_str)
                        self.functions.append((m.groups(0)[0], len(args)))
                        self.arguments.append(args)
                        self.codes.append(('script', start, i))
        log(self.verbose, "FUNC REGISTRATION ENDED")
        log(self.verbose, "FUNCS ",self.functions, self.arguments, self.codes)
        log(self.verbose, "SCRIPT:")
        Utils.print_script(log, self.verbose, self.script)
        log(self.verbose, "\n" * 10)

    def register_var(self, name, value, line):  # Find variables and their values
        self.variables.append(name)
        self.values.append(self.detect_val(value, line))

    def getcode(self, name, args):  # Get the block where a function is located
        return self.codes[self.functions.index((name, len(args)))]

    def getfunction(self, name, args):  # Get a function's script
        code = self.getcode(name, args)
        return self.script[code[1]:code[2] + 1]

    # V ----VARIABLES---- V

    def getval(self, name):  # Get a variable's value
        return self.values[self.variables.index(name)]

    def get_type(self, val, line, localvar, localval):  # Get a variable's type
        m = re.search(var_id, val)
        if m:
            # print('A variable!')
            if val in self.variables:
                return self.get_type(Utils.val_to_ps(self.getval(val)), line, localvar, localval)
            else:
                error(val + " is not a registered variable", self.script[line - 1], line)
        if not m:
            if val != "":
                m = Utils.tokenize(val, self.script[line - 1], line, localvar, localval)
                if m:
                    # print("A number")
                    # return 'num'
                    if type(m) == Tokens.Num:
                        return 'num'
                    elif type(m) == Tokens.Str:
                        return 'str'
                    elif type(m) in [Tokens.Bool, Tokens.And, Tokens.Equal]:
                        return 'bool'
            else:
                return None
        # if not m:
        #     m = re.search('^".*?"$', val)
        #     if m:
        #         # print("A string")
        #         return 'str'
        if not m:
            error(val + " is not a registered variable", self.script[line - 1], line)

    def detect_val(self, val, line, localvar=None, localval=None):  # Get a variable's value or infer the texts type and return it's value
        log(self.verbose, line, localvar, localval)
        if localval is None:
            localval = []
        if localvar is None:
            localvar = []
        m = re.search(var_id, val)
        if m:
            # Variable: get it's value
            if val in self.variables:
                return self.getval(val)
            elif val in localvar:
                return localval[localvar.index(val)]
            else:
                error(val + " is not a registered variable", self.script[line-1], line)
        if not m and val != "":
            m = Utils.tokenize(val, self.script[line - 1], line, localvar, localval, self)
            if m:
                # print("A number")
                # return 'num'
                return m.value()
        if val == "":
            return None
            # Not a variable: infer it's type and return it's value
            #m = re.search('^\d+$', val)
            #if m:
                # Number (num)
            #    return int(val)
        # if not m:
        #     m = re.search('^".*?"$', val)
        #     if m:
        #         # String (str)
        #         return val.strip('"')
        if not m:
            error(val + " is not a registered variable", self.script[line-1], line)

    def ps_function(self, name, args):  # Parse a function call
        log(self.verbose, "calling function " + name + " with arguments " + str(args))
        code = self.getcode(name, args)
        if code[0].startswith("perc.lang"):
            Utils.call_native(name, args)
        else:
            self.parse_func(self.getfunction(name, args), False, self.get_args(name, args), args)

    def function_call(self, name, args, line, localvar, localval):  # Analyze a function call
        line = line + 1
        if (name, len(args)) in self.functions:
            argspass = []
            # print("Function " + name + " exists!")
            for arg in args:
                arg = arg.strip(' ')
                argspass.append(self.detect_val(arg, line, localvar, localval))
            #print(line, name, argspass, '->')
            self.ps_function(name, argspass)
        else:
            func = str(self.script[line - 1].strip('\n'))
            for arg in args:
                func = func.replace(arg, self.get_type(arg, line, localvar, localval))
            error("The function " + func + " is not registered",
                        self.script[line - 1].strip('\n'), line)

    def parse(self, myscript, isSplit):  # Parse the main script
        if isSplit:
            lines = myscript
        else:
            lines = myscript.split("\n")
        self.script.extend(lines)
        # print("Script has " + len(lines).__str__() + " lines")
        self.register_functions(lines)
        self.parse_func(lines, True)

    def parse_func(self, toParse, isMain=False, localvariables=None, localvalues=None):  # Parse an actual code block
        if localvalues is None:
            localvalues = []
        if localvariables is None:
            localvariables = []
        #print(localvariables, localvalues)
        for line in toParse:
            i = toParse.index(line)
            inside = False
            #print("PARSING", line)
            for func in self.codes:
                log(self.verbose, func)
                if func[1] < i < func[2]:
                    inside = True
                    break
            if inside:
                if not isMain:
                    #print("LINE", line)
                    m = re.search('(\w+?)\((.*?)\)$', line)
                    if m:
                        #print(m.groups())
                        #print("CALLING:", m.groups(0)[0])
                        self.function_call(m.groups(0)[0], re.split(',\s*', m.groups(0)[1]), i, localvariables, localvalues)
            else:
                # Match a function
                #print("LINE", line)
                m = re.search('(\w+?)\((.*?)\)$', line)
                if m:
                    #print(m.groups())
                    #print("CALLING:", m.groups(0)[0])
                    self.function_call(m.groups(0)[0], re.split(',\s*', m.groups(0)[1]), i, localvariables, localvalues)
                # Match a global variable declaration
                regex = '(global\s+)?(\w+)\s*=\s*(".*"|\d+|\w+)$'
                if not isMain:
                    regex = '(global\s+)(\w+)\s*=\s*(".*"|\d+|\w+)$'
                # Match a global variable declaration
                m = re.search(regex, line)
                if m:
                    self.register_var(m.groups(0)[1], m.groups(0)[2], i)
                m = re.search('if\s*\((.*?)\){', line)
                if m:
                    blocks = []
                    finding_end = False
                    start = None
                    for line in toParse:
                        i = toParse.index(line)
                        m = re.search('if\s*\((.*?)\){', line)
                        if m:
                            if finding_end:
                                error("Cannot declare a function inside an if block", self.script[i], i + 1)
                            start = i
                            finding_end = True
                            blocks.append(m.group(0).rstrip('{'))
                            continue
                        m = re.search('(.*?){', line)
                        if m:
                            blocks.append(m.groups(0)[0])
                            continue
                        m = re.search('}', line)
                        if m:
                            popped = blocks.pop(len(blocks) - 1)
                            if len(blocks) == 0:
                                finding_end = False
                                m = re.search('if\s*\((.*?)\){', popped)
                                if m:
                                    arg_str = m.groups(0)[1]
                                    args = re.split('\s*(==|<=|<|>=|>)\s*', arg_str)
                                    self.functions.append((m.groups(0)[0], len(args)))
                                    self.arguments.append(args)
                                    self.codes.append(('script', start, i))

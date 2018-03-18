import Utils

class Token:
    elements = None
    linetext = ''
    line = 0

    def __init__(self, elements, linetext, line, localvar, localval):
        self.linetext = linetext
        self.line = line
        self.localvar = localvar
        self.localval = localval
        if(type(elements) == type([])):
            assignee = self.check(elements)
            self.elements = assignee
        else:
            raise TypeError(str(elements) + ' is not a list')

    def __str__(self):
        return str(self.elements)

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        if type(other) is not type(self):
            raise ValueError(str(other), 'is not of type', str(type(self)))
        return self.value() + other.value()

    def check(self, elements):
        pass

    def rawvalue(self):
        return str(self.value())

    def value(self):
        return self.elements


class Plus(Token):
    def check(self, elements):
        if len(elements) > 1:
            i1 = Utils.tokenize(str(elements[0]), self.linetext, self.line, self.localvar, self.localval)
            i2 = Utils.tokenize(str(elements[1]), self.linetext, self.line, self.localvar, self.localval)

            if type(i1.value()) == type(i2.value()):
                if type(i1.value()) != bool:
                    return [i1, i2]
                else:
                    Utils.error('Can\'t add boolean elements', self.linetext, self.line)
            else:
                Utils.error('Can\'t add two elements of diferent types', self.linetext, self.line)
        else:
            raise ValueError('Elements is smaller than 2')

    def rawvalue(self):
        val = self.value()
        if type(val) == str:
            return '"' + val + '"'
        else:
            return val

    def value(self):
        r = type(self.elements[0].value())()
        for e in self.elements:
            r += e.value()
        return r


class Num(Token):

    def check(self, elements):
        if len(elements) > 0:
            i = str(elements[0])
            if Utils.is_number(i):
                return float(i)
            else:
                raise ValueError('Input string is not of type num (' + i + '): ' + str(i.isdecimal()))
        else:
            raise ValueError('Elements is empty')

    def value(self):
        return self.elements


class Str(Token):
    def check(self, elements):
        if len(elements) > 0:
            return str(elements[0])
        else:
            raise ValueError('Elements is empty')

    def rawvalue(self):
        return '"' + self.value() + '"'

    def value(self):
        return self.elements

class Bool(Token):
    def check(self, elements):
        if len(elements) > 0:
            i = str(elements[0]).lower()
            if i == 'true':
                return True
            elif i == 'false':
                return False
            else:
                raise ValueError(i + ' is not a bool')
        else:
            raise ValueError('Elements is empty')

    def value(self):
        return self.elements


class And(Token):
    def check(self, elements):
        if len(elements) > 1:
            i1 = Utils.tokenize(str(elements[0]), self.linetext, self.line, self.localvar, self.localval)
            i2 = Utils.tokenize(str(elements[1]), self.linetext, self.line, self.localvar, self.localval)

            return [i1, i2]
        else:
            raise ValueError('Elements is smaller than 2')

    def value(self):
        return self.elements[0].value() and self.elements[1].value()

class Equal(Token):
    def check(self, elements):
        if len(elements) > 1:
            i1 = Utils.tokenize(str(elements[0]), self.linetext, self.line, self.localvar, self.localval)
            i2 = Utils.tokenize(str(elements[1]), self.linetext, self.line, self.localvar, self.localval)

            return [i1, i2]
        else:
            raise ValueError('Elements is smaller than 2')

    def value(self):
        return self.elements[0].value() == self.elements[1].value()

class Parenthesis(Token):
    def check(self, elements):
        if len(elements) > 0:
            return Utils.tokenize(elements[0], self.linetext, self.line, self.localvar, self.localval)
        else:
            raise ValueError('Elements is empty')

    def value(self):
        return self.elements.value()


num_literal_regex = '(-?\d+(\.\d*)?)'
str_literal_regex = '["\'](.*)["\']'
plus_literal_regex = '(.+)? *\+ *(.+)'
parents_literal_regex = '\((.+)\)'
bool_literal_regex = '([Tt]rue|[Ff]alse)'
and_literal_regex = '(\S+) *&& *(\S+)'
equal_literal_regex = '(.+)? *== *(.+)'

valid_token_literals = [
    (plus_literal_regex, Plus),
    (num_literal_regex, Num),
    (str_literal_regex, Str),
    (bool_literal_regex, Bool),
    (parents_literal_regex, Parenthesis),
    (and_literal_regex, And),
    (equal_literal_regex, Equal)
]

from command import Command

class Calc(Command):
    name = "calculator|calc"
    desc = "Opens the calculator tool"
    author = "ThePerkinrex"
    usage = "(calc|calculator)"

    def call(self, args=None):
        def getInput(y):
            if y==1:
                x = input("Write the first number: ")
            else:
                x = input("Write the second number: ")
            return x


        print("Options: ")
        print("-Add: write 'add'")
        print("-Subtract: write 'sub'")
        print("-Multiplication: write 'mult'")
        print("-Division: write 'div'")
        print("-Power: write 'pow'")
        print("-Quotient and remainder of a division: write 'CoRe'")

        sel = input("Select an option: ")
        result = 0
        x = float(getInput(1))
        y = float(getInput(2))

        if sel=="add":
            result = x + y
        elif sel == "sub":
            result = x - y
        elif sel == "mult":
            result = x * y
        elif sel == "div":
            result = x / y
        elif sel == "pow":
            result = x ** y
        elif sel == "CoRe":
            result = "Quotient: " + str(x // y) + "\nRemainder: " + str(x % y)
        else:
            print("That's not an option")
        print(result)
        state = 0

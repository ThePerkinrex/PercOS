from command import Command
import random

class UpDown(Command):
    name = 'upDown'
    desc = 'The upDown game'
    usage = "The usage for this command hasn't been implemented yet"
    author = 'ThePerkinrex'

    def call(self, args=None):
        x = random.randint(0,100)
        print("Guess a number between 0 and 100")
        while True:
            y = int(input("Write the number you think: "))
            if y == x:
                print("Correct :)")
                break
            elif y < x:
                print("The number is bigger")
                continue
            elif y > x:
                print("The number is smaller")
                continue

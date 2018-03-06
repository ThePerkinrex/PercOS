from command import Command

class Balls(Command):
    name = "balls"
    desc = "This is the balls game"
    author = "ThePerkinrex"
    usage = "balls"

    def call(self, args=None):
        nballs = 15
        p1 = self.usr
        p2 = input("P1 > " + p1 + ", P2 > ")
        while True:
            print("There are " + str(nballs) + " balls")
            P1in = int(Utils.getProbedInput(p1 + " > ", ["1","2"]))
            if P1in == 1 or P1in == 2:
                nballs -= P1in
                if nballs == 0:
                    print(p2 + " gana")
                    break
            print("There are " + str(nballs) + " balls")
            p2in = int(Utils.getProbedInput(p2 + " > ", ["1", "2"]))
            if p2in == 1 or p2in == 2:
                nballs -= p2in
                if nballs == 0:
                    print(p1 + " wins")
                    break

class StringHandler:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

odj = StringHandler()
odj.getString()
odj.printString()
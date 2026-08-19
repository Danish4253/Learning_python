class Calculator:
    def __init__(self, n):
        self.number = n

    def square(self):
        print(f"The square is {self.number*self.number}")

    def cube(self):
        print(f"The cube is {self.number*self.number*self.number}")

    def squareroot(self):
        print(f"The squareroot is {self.number**1/2}")


a = Calculator(4)
a.square()
a.cube()
a.squareroot()


a = Calculator(92)
a.square()
a.squareroot()
a.cube()

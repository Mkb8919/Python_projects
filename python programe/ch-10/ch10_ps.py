# problem1
import random


# class programmer:
#     company = "Microsoft"
#     def __init__(self, name, salary, pin):
#         self.name = name
#         self.salary = salary
#         self.pin = pin


# p = programmer("mohit", 1200000, 302020)
# print(p.name, p.salary,p.pin, p.company)
# r = programmer("rohan", 1200000, 302020)
# print(r.name, r.salary,r.pin,r.company)

# problem2

# class calculator:
#     def __init__(self,n):
#         self.n = n

    # def square(self):
    #     print(f"the square is {self.n*self.n}")

    # def cube(self):
    #     print(f"the cube is {self.n*self.n*self.n}")

    # def squareroot(self):
    #         print(f"the squareroot is {self.n**1/2}")


# a = calculator(4)
# a.square()
# a.cube()
# a.squareroot()

# problem3

# class demo:
#     a = 4  # class attribute doesnot change

# o = demo()
# print(o.a)   # prints the class attribute because instance attribute is not present
# o.a = 0 # instance attribute is set
# print(o.a)  # prints the instance attribute because instance attribute is present
# print(demo.a) # prints the class attribute

# problem4

# class Calculator:
#     def __init__(self, n):
#         self.n = n

    # def square(self):
    #     print(f"The square is {self.n * self.n}")

    # def cube(self):
    #     print(f"The cube is {self.n * self.n * self.n}")

    # def squareroot(self):
    #     print(f"The squareroot is {self.n ** 1 / 2}")

    # @staticmethod
    # def hello():
    #     print("Hello there!")


# a = Calculator(4)
# a.hello()
# a.square()
# a.cube()
# a.squareroot()

# problem5

# from random import randint
# class Train:

#   def __init__(self, trainNo)
#       self.trainNo = trainNo

    # def book(self,fro,to):
    #     print(f"ticket is booked in train no: {self.trainNo} from{fro} to{to}")

    # def getstatus(self):
    #     print(f"trainNo{self.trainNo} is running on time")

    # def getfare(self, fro,to):
    #     print(f"ticket fare in train no: {self.trainNo} from{fro} to{to} is"
    #           f"{randint(222, 5500)}")

# t = Train(12399)
# t.book("Jaipur", "Mumbai")
# t.getstatus()
# t.getfare("Jaipur", "Mumbai")

# problem6

from random import randint

class Train:

    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(harry, fro, to):
        print(f"Ticket is booked in train no: {harry.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12399)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")





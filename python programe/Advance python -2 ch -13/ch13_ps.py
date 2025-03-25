
# problem1
# problem2

# name = input("enter name :")
# marks = int(input("enter marks:"))
# phone = int(input("phone number :"))


# s = "the name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)

# print(s)


# problem3

# table = [str(7*i) for i in range(1,11)]

# s = "\n".join(table)
# print(s)

# problem4
# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False

# a = [1,2,34234,53,6234235,64343,65,754,45,55]
#
# f = list(filter(divisible5,a))
# print(f)

# problem5
# from functools import reduce
# l  = [111, 2, 65, 5553, 635, 65, 74, 45,55]


# def greater(a, b):
#     if (a>b):
#         return a
#     return b

# print(reduce(greater, l))

# problem6
# pip freeze > requirements.txt
# virtualenv harryenv

# problem7
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

app.run()




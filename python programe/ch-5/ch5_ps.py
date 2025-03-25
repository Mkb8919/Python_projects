# problem1

# words = {
   # "madad" : "help",
   # "kursi": "chair",
    # "billi" : "cat",
# }

# word = input("enter the word you want meaning of : ")

# print(words[word])

# problem2

# s = set()
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))
# n = input("enter number : ")
# s.add(int(n))

# print(s)

# problem 3

# s = set()
# s.add(18)
# s.add("18")

# print(s)

# problem 4

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))

# print(s)

# problem 5
s = {}
print(type(s))

# problem6

# d = {}
# name = input("enter friends name : ")
# lang = input("enter language name: ")

# d.update({name:lang})
# name = input("enter friends name : ")
# lang = input("enter language name: ")

# d.update({name:lang})
# name = input("enter friends name : ")
# lang = input("enter language name: ")

# d.update({name:lang})
# name = input("enter friends name : ")
# lang = input("enter language name: ")

# d.update({name:lang})

# print(d)

# problem 7

# the value entered later will be updated


# problem 8

# nothing will happen. The value can be same

# problem 9

# s = {8,7,12,"Harry",[1,2]}

# no it cannot be changed


# ps

# number = float(input("enter a number "))

# if number>0:
   # print("this number is positive ")
# else :
    # print("this number is not positive")





# Input: A year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a Leap Year.")
else:
    print("This is not a Leap Year.")

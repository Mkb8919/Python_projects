# problem1

# def greatest(a,b,c ):
#    if(a>b and a>c):
 #       return a
  #  elif(b>a and b>c):
  #      return b
  #  elif(c>b and c>a):
  #      return c

   # a = 1
   # b = 2
   # c = 3

# print(greatest(a, b, c))

# problem 2

# def f_to_c(f):
 #   return 5 * (f - 32) / 9

# f= int(input("enter temperature in f:"))
# print(f_to_c(f))
# print(f"{f_to_c(f)} degree C")
# c = f_to_c(f)
# print(f"{round(c,2)} degree C ")

#  problem 3
#print("a")
#print("b")
#print("c", end ="")
#print("d", end ="")

# problem4

'''

sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4....n-1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))

# problem 5

# def pattern(n):
 #   if(n==0):
    # return
  #  print("*" * n)
   # pattern(n-1)

# pattern(5)

# problem 6
# def inch_to_cms(inch):
   # return inch*2.54

# n = int(input("enter a number in inch:"))
# print(inch_to_cms(inch))
# print(f"the correspording value in cms is {inch_to_cms(n)}")

# problem 7

# def rem(l, word):
  #  n = []
  #  for item in l:
   #     if not(item == word):
    #        n.append(item.strip(word))
  #  return n


# l = ["Harry", "Rohan", "Shubham", "an"]

# print(rem(l, "an"))

# problem8

# def multiply(n):
#    for i in range(1,11):
  #     print(f"{n} X {i} = {n*i}")

 # multiply(5)


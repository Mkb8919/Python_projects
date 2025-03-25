try:
    a = int(input("hey, enter a number:"))
    print(a)


except Exception as e :
    print(e)


else:
    print("i am inside else")

# this is executed only if the try was successful

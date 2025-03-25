class Employee:
    # name = "mohit"
    language = "py"  # this is a class attribute
    salary = 1200000

mohit = Employee()
mohit.name = "mohit"  # this is an instance attribute
print(mohit.name,mohit.salary, mohit.language)


rohan = Employee()
rohan.name = "rohan roro robinson"
print(rohan.name,rohan.language, rohan.salary)

# here name is instance attribute and salary and language are class
#  attributes as they directly belong to the class


class Employee:
    language = "py"  # this is a class attribute
    salary = 1200000

mohit = Employee()
mohit.language = "javascript"  # this is an instance attribute
print(mohit.salary, mohit.language)

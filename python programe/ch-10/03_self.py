class Employee:
    language = "py"  # this is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"the language is {self.language}."
              f"the salary is {self.salary}")

    #def greet(self):
     #   print("good morning")

    @staticmethod
    def greet():
        print("good morning")




mohit = Employee()
# mohit.language = "javascript"  # this is an instance attribute
mohit.getInfo()
mohit.greet()
# Employee.getInfo(mohit)
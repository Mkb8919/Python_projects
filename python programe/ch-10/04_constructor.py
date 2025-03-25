class Employee:
    language = "py"  # this is a class attribute
    salary = 1200000

    def __init__(self, name,salary,language):  # dunder method which is
        # automatically called
        self.salary = 1300000
        self.name = "mohit"
        self.language = "javascript"
        print("i am creating an object")


    def getInfo(self):
        print(f"the language is {self.language}."
              f"the salary is {self.salary}")


    @staticmethod
    def greet():
        print("good morning")


mohit = Employee("mohit", 1300000, "javascript")
# mohit.name = "mohit"
# mohit.getInfo()
mohit.greet()
print(mohit.name,mohit.salary, mohit.language )
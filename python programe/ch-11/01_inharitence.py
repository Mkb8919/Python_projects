class Employee:
    company = "ITC" # base class or appearant class
    def show(self):
        print(f"the name of the Employee is {self.name} and the salary is {self.salary}")

# class programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"the name of is {self.name} and the salary is {self.salary}")
#
#     def showlanguage(self):
#         print(f"the name is {self.name} and he is good with {self.language} language")

class programmer(Employee):  # inharitance class
    company = "ITC infotech"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")


a = Employee()
b = programmer()

print(a.company, b.company)

# class Employee:
#     def __init__(self, salary, age):
#         self.salary = salary 
#         self.age = age
#     def display(self):
#         print(f"salary is {self.salary} and age is {self.age}")  
# e1 = Employee(24000, 28)
# e2 = Employee(30000, 25) 
# print(e1.salary) 
# print(e2.salary) 
# print(e1.age) 
# print(e2.age)
# e2.display() 
# e1.display()  



# built in class functions in OOPS: 
# getattr() , setattr() , delattr(), hasattr() 

# class Employee:
#     def __init__(self, name, age):
#         self.name=name 
#         self.age=age 
# e1 = Employee("ajay", 21) 
# e2 = Employee("jay", 22)  
# print(getattr(e1, "age")) # get attribute is used (here) to fetch the age of e1 
# setattr(e2, "name", "raj") # set attribute is used (here) to update of the name of e2 
# print(e2.__dict__) # e2 will be printed in the form of dictionary with updated version 
# delattr(e2, "age")  # del attribute used  (here) to delete the age attribute from e2 
# print(e2.__dict__) 
# print(hasattr(e2, "name")) # checks if e2 has name atribute or not (always returns boolean result) 

# built in class attributes in OOPS: 
# __dict__ , __doc__ , __name__ , __module__
# print(Employee.__doc__) 
# print(Employee.__dict__) 
# print(Employee.__name__) 
# print(Employee.__module__) 

# class Demo:
#     pass 
# d1 = Demo 
# print(isinstance(e1, Employee))       
# print(isinstance(d1, Employee))  



# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
#     def display(self):
#         print(self.name, self.marks)  
#     def change_data(self):
#         self.name= input("Enter name: ") 
#         self.marks = int(input("Enter marks: "))
# std1 = Student("akshay", 89)
# std2 = Student("aman", 87)
# std3 = Student("arun", 95) 
# del std1.name 
# print(std1.__dict__) 
# setattr(std1, "marks", 92) 
# print(std1.__dict__)  
# print(getattr(std2, "name")) 
# print(hasattr(std1, "name")) 
# std2.display() 
# std3.change_data() 
# print(std3.__dict__)  

# Class variables : 
class Employee:
    company_name = "infosys"  # class variable (must be same for all the attributes) 
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
e1 = Employee("jay", 30000)
e2 = Employee("vijay", 50000) 
print(Employee.company_name) 
print(e1.company_name)
print(e2.company_name) # all the three will print only "infosys" (as it is sme for all)

# Modification in class variable
# Employee.company_name = "TCS" # this will change company name for all (e1 and e2) 
e1.company_name = "TCS" # this will changw company name for only e1 
print(e1.__dict__) 
print(Employee.company_name)  



'''
class Class:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    def say_hi(self):
        print(f'Hello, my name is {self.name}')
    def tell_position(self):
        print(f'I am a {self.position}')
john = Class('Bach', 'Software Engineer')
john.say_hi()
john.tell_position()
'''
class employee:
    def __init__(self,name,age):
        self.name= name
        self.age =age

class fulltimes_employee(employee):
    def __init__(self,name,age,basic_salary,salary_multiplier):
        super().__init__(self,name,age)
        self.basic_salary= basic_salary
        self.salary_multiplier = salary_multiplier
    def tinhluong(self):
        print(self.basic_salary*self.salary_multiplier)
class Parttimes_employee(employee):
    def __init__(self,name,age,hours_worked,hourly_rate):
        super().__init__(self,name,age)
        self.hours_worked=hours_worked
        self.hourly_rate= hourly_rate
    def tinhluong(self):
        print(self.hours_worked*self.hourly_rate)
'''
a = input('Name nv1')
b = input('Name nv2')
Huy = Parttimes_employee("Huy", 20, 1, 1)
Bach =Parttimes_employee('Bach',20,3,2)

class Department(employee):
    def __init__(self, name):
        self.name = name
        self.employees = [] #Danh sach nhan vien
    def add_employee(self, employee):
        self.employees.append(employee)

it = Department("It")
it.add_employee(Huy)

def remove_employee(self,employee):
        self.employees.remove()
'''          
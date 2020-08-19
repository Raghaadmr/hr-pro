from datetime import datetime
class Employee:
  def __init__(self,name,age,salary,employment_year):
    self.name=name
    self.age=age
    self.salary=salary
    self.employment_year=employment_year
  def get_working_years(self):
    return datetime.now().year - self.employment_year
  def ___str___(self):
    return f"{self.name}, {self.age}, {self.salary}, {self.get_working_years()}"

class Manager(Employee):
  def __init__(self,name,age,salary,employment_year,bonus_percentage):
    Employee.__init__(self,name,age,salary,employment_year)
    self.bonus_percentage=bonus_percentage

  def get_bonus(self):
    return self.salary*self.bonus_percentage/100
  def ___str___(self):
    return super().___str___()+f", {self.get_bonus()}"


def main():
  print("Welcome to HR Pro 2020")
  print("""
  Options:
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit
  """)
  Employees=[]
  Managers=[]
  while(True):
    option = int(input("What would you like to do?"))

    if option == 1:
      for x in Employees:
        print(Employee.___str___(x))
    elif option == 2:
      for x in Managers:
        print(Manager.___str___(x))
    elif option == 3:
      name = input("Name: ")
      age = int(input("Age: "))
      salary = int(input("Salary: "))
      employment_year = int(input("Emplyment year: "))
      Employees.append(Employee(name,age,salary,employment_year))
    elif option == 4:
      name = input("Name: ")
      age = int(input("Age: "))
      salary = int(input("Salary: "))
      employment_year = int(input("Emplyment year: "))
      bonus_percentage = int(input("bonus_percentage: "))
      Managers.append(Manager(name,age,salary,employment_year,bonus_percentage))
    elif option == 5:
      break
    else:
      print("error")


if __name__ == '__main__':
	main()

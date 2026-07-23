class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")

    def compare(self, salary):
        if self.salary > 70000:
            print(f"{self.name} has a high salary.")
        elif self.salary > 40000 and self.salary <= 70000:
            print(f"{self.name} has a moderate salary.")
        else:
            print(f"{self.name} has a low salary.")

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print(f"Company: {self.name}")
        for emp in self.employees:
            emp.display_info()
            emp.compare(emp.salary)
            print("-" * 30)

employee1 = Employee("Alice", "Manager", 80000)
employee2 = Employee("Bob", "Developer", 60000)
company = Company("Tech Corp")
company.add_employee(employee1)
company.add_employee(employee2)
company.display_employees()
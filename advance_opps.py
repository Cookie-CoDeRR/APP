class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def display(self):
        print("Name    :", self.name)
        print("Salary  :", self.__salary)


class Manager(Employee):
    def __init__(self, name, salary, department, experience):
        super().__init__(name, salary)
        self.department = department
        self.experience = experience

    def display(self):
        super().display()
        print("Department :", self.department)
        print("Experience :", self.experience, "Years")

        if self.experience >= 10:
            level = "Senior Manager"
        elif self.experience >= 5:
            level = "Manager"
        else:
            level = "Assistant Manager"

        print("Level      :", level)


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language  :", self.language)


def run_demo():
    manager = Manager("Amit", 80000, "IT", 7)
    developer = Developer("Sneha", 60000, "Python")

    print("Manager Details")
    manager.display()

    print("\nDeveloper Details")
    developer.display()

    print("\nSalary of manager:", manager.get_salary())


if __name__ == "__main__":
    run_demo()
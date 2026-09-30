from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def show_role(self):
        pass


class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.__roll_no = roll_no
        self.__books = []

    def issue_book(self, book):
        self.__books.append(book)

    def get_books(self):
        return self.__books

    def show_role(self):
        print("Role: Student")

    def display(self):
        print(f"Name      : {self.name}")
        print(f"Roll No   : {self.__roll_no}")
        print(f"Books     : {self.__books}")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_role(self):
        print("Role: Teacher")

    def display(self):
        print(f"Name      : {self.name}")
        print(f"Subject   : {self.subject}")


def run_demo():
    student = Student("Gajanan", 101)
    teacher = Teacher("Sharma", "Python")

    student.issue_book("Python Programming")
    student.issue_book("Data Structures")

    people = [student, teacher]

    for person in people:
        person.show_role()
        person.display()
        print("-" * 30)

    print("Books issued to student:", student.get_books())


if __name__ == "__main__":
    run_demo()
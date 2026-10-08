from __future__ import annotations

from pathlib import Path
from typing import List, Optional


class Course:
    def __init__(self, course_name: str, duration: int, fee: float) -> None:
        course_name = course_name.strip()
        if not course_name:
            raise ValueError("Course name cannot be empty.")
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")
        if fee < 0:
            raise ValueError("Fee cannot be negative.")

        self.course_name = course_name
        self.duration = duration
        self.fee = fee

    @property
    def course_type(self) -> str:
        return "Short-Term" if self.duration <= 6 else "Long-Term"

    def to_file_line(self) -> str:
        return f"{self.course_name}|{self.duration}|{self.fee:.2f}\n"

    @classmethod
    def from_file_line(cls, line: str) -> "Course":
        course_name, duration, fee = line.strip().split("|", 2)
        return cls(course_name, int(duration), float(fee))

    def display_details(self) -> None:
        print(
            f"Course: {self.course_name} | Duration: {self.duration} month(s) | "
            f"Fee: ₹{self.fee:.2f} | Category: {self.course_type}"
        )


class Institute:
    def __init__(self, institute_name: str, data_file: str = "courses.txt") -> None:
        self.institute_name = institute_name
        self.data_file = Path(data_file)
        self.courses: List[Course] = []

    def add_course(self, course: Course) -> None:
        self.courses.append(course)

    def save_courses(self) -> None:
        with self.data_file.open("w", encoding="utf-8") as file:
            for course in self.courses:
                file.write(course.to_file_line())

    def load_courses(self) -> None:
        self.courses.clear()
        if not self.data_file.exists():
            return

        with self.data_file.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if not line.strip():
                    continue
                try:
                    self.courses.append(Course.from_file_line(line))
                except (ValueError, TypeError):
                    print(f"Skipping invalid course record on line {line_number}.")

    def display_courses(self, category: Optional[str] = None) -> None:
        matching_courses = self.courses
        if category:
            matching_courses = [course for course in self.courses if course.course_type == category]

        if not matching_courses:
            print("No courses found.")
            return

        print(f"\nCourses offered by {self.institute_name}")
        print("=" * 78)
        for course in matching_courses:
            course.display_details()
        print("=" * 78)

    def display_course_categories(self) -> None:
        self.display_courses("Short-Term")
        self.display_courses("Long-Term")


def read_positive_integer(message: str) -> int:
    while True:
        try:
            value = int(input(message).strip())
            if value > 0:
                return value
            print("Enter a number greater than zero.")
        except ValueError:
            print("Enter a valid whole number.")


def read_non_negative_fee(message: str) -> float:
    while True:
        try:
            value = float(input(message).strip())
            if value >= 0:
                return value
            print("Enter a fee that is zero or higher.")
        except ValueError:
            print("Enter a valid fee amount.")


def add_course_from_input(institute: Institute) -> None:
    course_name = input("Enter course name: ").strip()
    duration = read_positive_integer("Enter duration in months: ")
    fee = read_non_negative_fee("Enter course fee: ")
    try:
        institute.add_course(Course(course_name, duration, fee))
        institute.save_courses()
        print("Course added and saved successfully.")
    except ValueError as error:
        print(error)


def start_course_management() -> None:
    institute = Institute("Skill Development Institute")
    institute.load_courses()

    while True:
        print("\nCourse Management System")
        print("1. Add course")
        print("2. Display all courses")
        print("3. Display short-term courses")
        print("4. Display long-term courses")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_course_from_input(institute)
        elif choice == "2":
            institute.display_courses()
        elif choice == "3":
            institute.display_courses("Short-Term")
        elif choice == "4":
            institute.display_courses("Long-Term")
        elif choice == "5":
            institute.save_courses()
            print("Course information saved. Goodbye.")
            break
        else:
            print("Choose an option from 1 to 5.")


if __name__ == "__main__":
    start_course_management()

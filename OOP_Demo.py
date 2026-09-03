"""
Author: Ryon Connery
Date: September 3, 2026

Program: Object-Oriented Course Information Program

Purpose:
This program demonstrates object-oriented programming in Python by
defining a Course class, instantiating multiple Course objects from
hardcoded data, storing those objects in a collection, and using a loop
to print each object's attributes in a structured table.
"""


class Course:
    """Represent a course and its required attributes."""

    def __init__(self, course_code, credit_hours, enrollment, room_number):
        """Initialize a Course object with the required course data."""
        self.course_code = course_code
        self.credit_hours = credit_hours
        self.enrollment = enrollment
        self.room_number = room_number

    def display(self):
        """Return the course information formatted as one table row."""
        return (
            f"{self.course_code:<15}"
            f"{self.credit_hours:<12}"
            f"{self.enrollment:<15}"
            f"{self.room_number:<12}"
        )


def main():
    """Create Course objects and display their information."""

    courses = [
        Course("IT1006", 6, 45, "B28"),
        Course("IT4782", 3, 22, "C34"),
        Course("IT4789", 3, 34, "H05"),
        Course("IT4079", 6, 34, "K25"),
        Course("IT2230", 3, 18, "A17"),
        Course("IT3345", 3, 34, "B16"),
        Course("IT2249", 6, 4, "A20"),
    ]

    print("**** Object-Oriented Programming Demonstration by Ryon Connery *****")
    print()
    print(
        "This program demonstrates classes, objects, constructors, "
        "attributes, and iteration in Python."
    )
    print(
        "Each course is instantiated as an object of the Course class "
        "and displayed using a loop."
    )
    print()

    print(
        f"{'Course Code':<15}"
        f"{'Credits':<12}"
        f"{'Enrollment':<15}"
        f"{'Room Number':<12}"
    )
    print("-" * 54)

    for course in courses:
        print(course.display())

    print()
    print("Program ended. Have a good day.")


main()

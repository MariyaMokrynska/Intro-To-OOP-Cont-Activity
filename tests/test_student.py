import pytest
from school_schedule.student import Student

def test_student_attributes():
    #Assert
    name = "Marina"
    grade = "senior"
    classes = ["Precalculus", "Javascript"]

    #Act
    student = Student(name, grade, classes)

    #Assert
    assert student.name == name
    assert student.grade == grade
    assert len(student.classes) == 2
    assert "Precalculus" in student.classes

def test_add_class_to_student():
    #Assert
    name = "Mariya"
    grade = "junior"
    classes = ["Python", "PhP"]
    student = Student(name, grade, classes)
    class_name = "Java"

    #Act
    result = student.add_class(class_name)

    #Assert
    assert len(classes) == 3
    assert class_name in student.classes

def test_non_existing_attribute_raise_exception():
    #Assert
    name = "Anna"
    grade = "senior"
    classes = ["Bilogy", "Chemistry", "Pharmacy"]
    email = "xyz@gmail.com"

    with pytest.raises(TypeError, match="Student.__init__\(\) takes 4 positional arguments but 5 were given"):
        Student(name, grade, classes, email)
 
def test_passing_not_all_arg_raises_exception():
    #Assert
    name = "Mark"
    grade = "junior"

    with pytest.raises(TypeError, match="Student.__init__\(\) missing 1 required positional argument: 'classes'"):
        Student(name, grade)



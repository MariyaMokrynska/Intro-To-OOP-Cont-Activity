from school_schedule.student import Student
# Nominal cases
def test_student_attributes():
    #Arrange
    name = "Marina"
    grade = "senior"
    classes = ["Precalculus", "Javascript"]

    #Act
    student = Student(name, grade, classes) 

    #Assert
    assert student.name == name
    assert student.grade == grade
    assert student.get_num_classes() == 2
    assert "Precalculus" in student.classes

def test_add_class_to_student():
    #Arrange
    name = "Mariya"
    grade = "junior"
    classes = ["Python", "PhP"]
    student = Student(name, grade, classes)
    class_name = "Java"

    #Act
    result = student.add_class(class_name)

    #Assert
    assert len(result) == 3
    assert class_name in student.classes

def test_summary_method():
    # Arrange
    name = "Andrew"
    grade = "junior"
    classes = ["Intro to Computer Science", "Public Speaking"]
    student = Student(name, grade, classes)

    # Act
    result = student.summary()

    # Assert
    assert result == "Andrew is a junior enrolled in 2 classes: Intro to Computer Science, Public Speaking"

# Edge cases
# Based on the add_class() implementation, duplicates are NOT handled.
def test_add_duplicate_class():
    #Arrange
    name = "Anna"
    grade = "senior"
    classes = ["Math", "Sql"]
    student = Student(name, grade, classes)

    #Act
    result = student.add_class("Math")

    #Assert
    assert len(result) == 3
    assert "Math" in student.classes
    assert result == ["Math", "Sql", "Math"]

def test_return_zero_on_empty_class_list():
    #Arrange
    name = "Mark"
    grade = "junior"
    classes = []
    student = Student(name, grade, classes)

    #Act
    result = student.get_num_classes()

    #Assert
    assert result  == 0




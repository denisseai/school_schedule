from school_schedule.student import Student

def test_valid_params():
    # Arrange
    # Create an instance of the class
    # and set up any other necessary test variables

    # Act
    # Call the method that we are testing

    # Assert
    # Verify all relevant return values and state changes

    # Arrange
    name = "Quinn"
    grade = "junior"
    classes = [
                "Pre-Calc", 
                "English III", 
                "World History", 
                "Gym", 
                "Chemistry", 
                "Music Composition"
                ]
    # Act
    student = Student(name=name, grade=grade, classes=classes)

    # Assert
    assert student.name == name
    assert student.grade == grade
    assert len(student.classes) == 6


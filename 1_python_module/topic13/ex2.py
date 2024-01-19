class InvalidGradeError(Exception):
    def __init__(self, message):
        super().__init__(message)
        print("В деле пользовательское исключение!")


class SubjectGrade:
    def __init__(self, name, grade):
        self.name = name
        if grade > 100 or grade < 0:
            raise InvalidGradeError("Балл не может быть больше 100 или меньше 0!")
        self.grade = grade


try:
    math = SubjectGrade('Ulan', 78)
    geog = SubjectGrade('Ulan', 110)
except InvalidGradeError as e:
    print(e)






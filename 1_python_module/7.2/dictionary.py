
students = [
    {
        "name": "Ulan",
        "age": 23,
        "gender": "male",
        "stage": 1
    }, {
        "name": "Gulzat",
        "age": 21,
        "gender": "female",
        "stage": 2
    }, {
        "name": "Amir",
        "age": 25,
        "gender": "male",
        "stage": 2
    }

]

# age_sum = 0
for student in students:
    # age_sum = age_sum + student['age']
    if student['gender'] == 'male':
        print(student['name'])

# print(age_sum/len(students))


# a = ('name', 'Ulan')
# print(a)
# a, b = ('name', 'Ulan')
# print(a, b)


# age = d.get("age")
# if age:
#     print(f"age is {age}")
# else:
#     print("false edede")

# print("Program be slomalsya!")

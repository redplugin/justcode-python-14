from people_class import People
# a = "hello"
# b = "30"

a = People("Amir", 24, 180)
b = People("Alex", 28, 170)


if a > b:
    print(f"{a} > {b}")
elif a < b:  # b > a
    print(f"{a} < {b}")
else:
    print(f"{a} равны {b}")

print("What is your age")
age = int(input())

if age < 5:
    print("free")

if age >= 5 and age <= 12:
    print("5$")

if age >= 12 and age <= 64:
    print("12$")

if age >= 65:
    print("8$")

height = int(input("What is your height: "))
weight = int(input("What is your weight: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underweight")

if bmi >= 18.5 and bmi <= 24.9:
    print("normal")

if bmi >= 25 and bmi <= 29.9:
    print("overweight")

if bmi >= 30:
    print("obese")

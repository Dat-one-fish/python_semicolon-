print("Enter 2 integers x and y")

x = int(input("x: "))
y = int(input("y: "))

if x > 0 and y > 0:
    print("Q1")

if x < 0 and y > 0:
    print("Q2")

if x < 0 and y < 0:
    print("Q3")

if x > 0 and y < 0:
    print("Q4")

if y == 0 and x != 0:
    print("x-axis")

if y != 0 and x == 0:
    print("y-axis")

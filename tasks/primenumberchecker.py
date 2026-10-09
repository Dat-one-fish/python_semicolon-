number = int (input ("input a number:   "))
i = 2
counter = 0
while (i < number):
    if (number % i == 0):
       counter = counter + 1 
    i = i + 1


if (counter == 0):
    print ( True )
else:
    print ( False)

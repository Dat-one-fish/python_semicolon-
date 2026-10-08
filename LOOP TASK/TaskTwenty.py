number = int (input("Enter a number: "))

smallestnum = 10

while number > 0 :
    digit = number % 10

    if smallestnum > digit:
        smallestnum = digit

    number = number // 10
    
print ( smallestnum)
    

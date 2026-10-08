number = int (input("Enter a number: "))
largestnum = 0


while number > 0 :
    digit = number % 10
    
    if largestnum < digit:
        largestnum = digit


    number = number // 10
    

print ( largestnum)

    
    


   

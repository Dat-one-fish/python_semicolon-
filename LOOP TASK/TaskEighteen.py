number = int (input("Enter a number: "))
numbersum = 0

while number > 0 :
    digit = number % 10
    numbersum += digit
    number = number // 10

print (numbersum) 
   

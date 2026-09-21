

first_num = int(input('enter 1st num: '))
second_num = int(input('enter 2nd num: '))
third_num = int(input('enter 3rd num: '))
four_num = int(input('enter 4th num: '))
fifth_num = int(input('enter 5th num: '))


int evennumber = 0
int oddnumber = 0


if (first_num % 2) == 0:
    evennumber = evennumber + first_num
else:
    oddnumber = oddnumber + first_num


if (second_num % 2) == 0:
    evennumber = evennumber + second_num
else:
    oddnumber = oddnumber + second_num


if (third_num % 2) == 0:
    evennumber = evennumber + third_num
else:
    oddnumber = oddnumber + third_num


if (four_num % 2) == 0:
    evennumber = evennumber + four_num
else:
    oddnumber = oddnumber + four_num


if (fifth_num % 2) == 0:
    evennumber = evennumber + fifth_num
else:
    oddnumber = oddnumber + fifth_num


print(oddnumber, "is the sum of all odd numbers in the set")
print(evennumber, "is the sum of all even numbers in the set")

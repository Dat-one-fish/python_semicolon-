print("Enter a sentence: ")
word = input(":    ")
E = 'E'
e = 'e' 
A = 'A'
a = 'a'
I = 'I'
i = 'i'
O = 'O'
o = 'o'
U = 'U'
u = 'u'
counter = 0

for chr in word:
    if ( chr == E):
        counter = counter + 1
    if ( chr == e):
        counter = counter + 1

    if ( chr == A):
        counter = counter + 1
    if ( chr == a):
        counter = counter + 1

    if ( chr == I):
        counter = counter + 1
    if ( chr == i):
        counter = counter + 1

    if ( chr == O):
        counter = counter + 1
    if ( chr == o):
        counter = counter + 1

    if ( chr == U):
        counter = counter + 1
    if ( chr == u):
        counter = counter + 1

print (counter)

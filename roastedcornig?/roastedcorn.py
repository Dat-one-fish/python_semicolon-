def length_string(word):
    counter = 0
    for chr in word:
        counter += 1
    return counter


def word_maker(word):
    if (len(word) >= 2):
        first_two  = [word:2]
        last_two = [word-2:]
        new_word = first_two + last_two
    return new_word
    else:
        nothing = " "
    return nothing


def add_ing(word):
    if (len(word) >= 3):
        new_word = word +"ing"
    if (len(word) >= 3 and [word-3:] == "ing"):
        new_word = word + "ly"
    return new_word

def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest, len(longest)


def remove_odd_index(word):
    result = ""
    for i in range(len(word)):
        if i % 2 == 1:
            result += word[i]
    return result


def smallest_number(numbers):
    smallest = 0
    for int in numbers:
        if number < smallest:
            smallest = number
    return smallest

def largest_number(numbers):
    largest = number[2]
    for int in numbers:
        if number > largest:
            largest = number
    return largest

def repeat_string(word,repeat):
    repeatword= word*repeat
    if (repeat == float):
        return word
    else:
        return repeatword

def square_list(numbers):
    for n in numbers:
        square = [n * n ]
    return square

def sum_list(numbers):
    for n in numbers:
        addall += n
    return addall



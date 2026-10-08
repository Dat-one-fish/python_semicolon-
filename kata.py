

def is_even(number):
    return number % 2 == 0


def is_prime_number(number):
    if number < 2:
        return False

    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1

    return True


def subtract(first_number, second_number):
    return (first_number - second_number)


def divide(numerator, denominator):
    if denominator == 0:
        return 0

    return numerator / denominator


def factor_of(number):
    factor_count = 0

    for candidate in range(1, number + 1):
        if number % candidate == 0:
            factor_count += 1

    return factor_count


def is_square(number):
    if number < 0:
        return False

    root = 0
    while root * root < number:
        root += 1

    return root * root == number


def reverse_digits(number):
    reversed_number = 0

    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number //= 10

    return reversed_number


def is_palindrome(number):
    MIN_FIVE_DIGIT_NUMBER = 10000
    MAX_FIVE_DIGIT_NUMBER = 99999
    if not MIN_FIVE_DIGIT_NUMBER <= number <= MAX_FIVE_DIGIT_NUMBER:
        return False

    return number == reverse_digits(number)


def factorial_of(number):
    factorial = 1

    for multiplier in range(2, number + 1):
        factorial *= multiplier

    return factorial


def square_of(number):
    return number * number

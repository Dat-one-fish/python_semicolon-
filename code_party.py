from functools import reduce


def append_to_tuple(original_tuple, new_value):
    return original_tuple + (new_value,)


def set_nested_list_value(numbers, outer_index, inner_index, new_value):
    numbers[outer_index][inner_index] = new_value
    return numbers


def add_item_via_list(fruit_tuple, new_fruit):
    fruit_list = list(fruit_tuple)
    fruit_list.append(new_fruit)
    return tuple(fruit_list)


def unpack_first_two_and_rest(values):
    first = values[0]
    second = values[1]
    rest = list(values[2:])
    return first, second, rest


def sum_each_row(matrix):
    return list(map(sum, matrix))


def sum_each_column(matrix):
    if not matrix:
        return []

    column_sums = []
    num_columns = len(matrix[0])

    for col_index in range(num_columns):
        total = 0
        for row in matrix:
            total += row[col_index]
        column_sums.append(total)

    return column_sums


def is_even(number):
    return number % 2 == 0


def is_longer_than_five(word):
    return len(word) > 5


def has_first_value_greater_than_two(pair):
    return pair[0] > 2


def is_divisible_by_three_and_five(number):
    return number % 3 == 0 and number % 5 == 0


def is_palindrome(word):
    return word == word[::-1]


def get_even_numbers(numbers):
    return list(filter(is_even, numbers))


def get_long_words(words):
    return list(filter(is_longer_than_five, words))


def keep_pairs_with_large_first_value(pairs):
    return list(filter(has_first_value_greater_than_two, pairs))


def get_divisible_by_three_and_five(numbers):
    return list(filter(is_divisible_by_three_and_five, numbers))


def get_palindromes(words):
    return list(filter(is_palindrome, words))


tax_multiplier = 1.10


def square(number):
    return number ** 2


def add_tax(price):
    return price * tax_multiplier


def convert_to_uppercase(words):
    return list(map(str.upper, words))


def square_all(numbers):
    return list(map(square, numbers))


def capitalize_all(names):
    return list(map(str.capitalize, names))


def add_tax_to_all(prices):
    return list(map(add_tax, prices))


def add_numbers(first_number, second_number):
    return first_number + second_number


def multiply_numbers(first_number, second_number):
    return first_number * second_number


def join_with_space(left_text, right_text):
    return left_text + " " + right_text


def larger_of(first_number, second_number):
    return first_number if first_number > second_number else second_number


def sum_of_numbers(numbers):
    return reduce(add_numbers, numbers)


def maximum_number(numbers):
    return reduce(larger_of, numbers)


def concatenate_with_spaces(words):
    return reduce(join_with_space, words)


def product_of_squares(numbers):
    squared_numbers = map(square, numbers)
    return reduce(multiply_numbers, squared_numbers)


def is_greater_than_five(number):
    return number > 5


def sum_each_tuple_above_five(tuples_list):
    sums = map(sum, tuples_list)
    return list(filter(is_greater_than_five, sums))


def total_of_numeric_strings(data):
    numeric_strings = filter(str.isdigit, data)
    integers = map(int, numeric_strings)
    return sum(integers)

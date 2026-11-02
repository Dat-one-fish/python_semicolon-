import random

list_size = 10
lowest_number = 1
highest_number = 50


def create_random_numbers():
    numbers = []
    for position in range(list_size):
        numbers.append(random.randint(lowest_number, highest_number))
    return numbers


def get_length(numbers):
    length = 0
    for number in numbers:
        length += 1
    return length


def sum_at_even_positions(numbers):
    return sum(numbers[0::2])


def sum_at_odd_positions(numbers):
    return sum(numbers[1::2])


def multiply_every_third_position(numbers):
    product = 1
    for number in numbers[2::3]:
        product *= number
    return product


def average_of(numbers):
    if not numbers:
        return 0
    return sum(numbers) / get_length(numbers)


def largest_number(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest


def smallest_number(numbers):
    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number
    return smallest


def has_same_first_and_last_character(word):
    return len(word) >= 2 and word[0] == word[-1]


def get_strings_with_same_ends(words):
    return list(filter(has_same_first_and_last_character, words))


def count_strings_with_same_ends(words):
    return len(get_strings_with_same_ends(words))


def create_one_to_fifteen():
    return list(range(1, 16))


def sum_every_third_element(numbers):
    return sum(numbers[2::3])


def get_middle_value(numbers):
    middle_index = len(numbers) // 2
    if len(numbers) % 2 == 1:
        return numbers[middle_index]
    return (numbers[middle_index - 1] + numbers[middle_index]) / 2


def sum_first_middle_and_last(numbers):
    if not numbers:
        return 0
    return numbers[0] + get_middle_value(numbers) + numbers[-1]


if __name__ == "__main__":
    random_numbers = create_random_numbers()
    print("Random numbers:", random_numbers)
    print("Length:", get_length(random_numbers))
    print("Sum at even positions:", sum_at_even_positions(random_numbers))
    print("Sum at odd positions:", sum_at_odd_positions(random_numbers))
    print("Product of every third position:", multiply_every_third_position(random_numbers))
    print("Average:", average_of(random_numbers))
    print("Largest:", largest_number(random_numbers))
    print("Smallest:", smallest_number(random_numbers))

    words = ["level", "hello", "abca", "a", "noon", "xyz"]
    print("\nStrings with same first and last character:", get_strings_with_same_ends(words))
    print("How many:", count_strings_with_same_ends(words))

    one_to_fifteen = create_one_to_fifteen()
    print("\nList:", one_to_fifteen)
    print("Sum of every third element:", sum_every_third_element(one_to_fifteen))
    print("Sum of first, middle and last:", sum_first_middle_and_last(one_to_fifteen))
    print("Even-length example [1, 2, 3, 4]:", sum_first_middle_and_last([1, 2, 3, 4]))
